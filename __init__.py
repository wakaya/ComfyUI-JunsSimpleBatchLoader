import locale
from .juns_simple_batch_loader import JunsSimpleBatchLoader

# システム言語を取得
lang = locale.getdefaultlocale()[0]

# 言語に応じた表示名を定義
if lang == "ja_JP":
    display_name = "📁一括画像読み込み (Jun Wakaya's Simple Batch Loader)"
else:
    display_name = "📁Jun Wakaya's Simple Batch Loader"

NODE_CLASS_MAPPINGS = {
    "JunsSimpleBatchLoader": JunsSimpleBatchLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JunsSimpleBatchLoader": display_name
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
