import os
import json
import torch
import numpy as np
from PIL import Image, ImageOps
import locale

class JunsSimpleBatchLoader:
    def __init__(self):
        self.messages = self._load_i18n()

    def _load_i18n(self):
        # 自分のファイルの場所からi18nフォルダを探す
        base_path = os.path.dirname(os.path.realpath(__file__))
        lang = locale.getdefaultlocale()[0] or "en_US"
        
        # ja_JP か en_US 以外は英語にする
        if lang != "ja_JP":
            lang = "en_US"
            
        json_path = os.path.join(base_path, "i18n", f"{lang}.json")
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            # 万が一読み込めなかった時のフォールバック
            return {
                "no_images": "No images found: ",
                "out_of_range": "No images found within the specified range.",
                "complete": "All images processed (Total {}). Batch finished.",
                "processing": "Processing"
            }

    def get_msg(self, key):
        return self.messages.get(key, key)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory_path": ("STRING", {"default": ""}),
                "extensions": ("STRING", {"default": ".png,.jpg,.jpeg"}),
                "index": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "forceInput": True}),
                "reset_to_start": ("BOOLEAN", {"default": False}),
                "process_until_last": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "start_index": ("INT", {"default": 0, "min": 0}),
                "end_index": ("INT", {"default": 0, "min": 0}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING", "STRING", "INT")
    RETURN_NAMES = ("image", "full_path", "filename_no_ext", "total_count")
    FUNCTION = "load_batch_image"
    CATEGORY = "Jun's Nodes"

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return float("nan")

    def load_batch_image(self, directory_path, extensions, index, reset_to_start, process_until_last, start_index=0, end_index=0):
        ext_list = [e.strip().lower() for e in extensions.split(",")]
        all_files = []
        if os.path.isdir(directory_path):
            for f in os.listdir(directory_path):
                if any(f.lower().endswith(ext) for ext in ext_list):
                    all_files.append(os.path.join(directory_path, f))
        all_files = sorted(list(set(all_files)))
        
        if not all_files:
            raise FileNotFoundError(self.get_msg("no_images") + directory_path)

        if process_until_last:
            target_files = all_files[start_index:]
        else:
            effective_end = min(end_index + 1, len(all_files))
            target_files = all_files[start_index:effective_end]

        num_targets = len(target_files)
        if num_targets == 0:
            raise IndexError(self.get_msg("out_of_range"))

        if reset_to_start:
            actual_index = 0
        else:
            if index >= num_targets:
                raise IndexError(self.get_msg("complete").format(num_targets))
            actual_index = index

        current_file_path = target_files[actual_index]
        filename_no_ext = os.path.splitext(os.path.basename(current_file_path))[0]

        img = Image.open(current_file_path).convert("RGB")
        img = ImageOps.exif_transpose(img)
        img_np = np.array(img).astype(np.float32) / 255.0
        img_tensor = torch.from_numpy(img_np).unsqueeze(0)

        print(f"JunsSimpleBatchLoader: [{actual_index + 1}/{num_targets}] {self.get_msg('processing')}: {current_file_path}")

        return (img_tensor, current_file_path, filename_no_ext, num_targets)
