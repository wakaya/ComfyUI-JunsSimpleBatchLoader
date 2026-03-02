# ComfyUI Simple Batch Loader

*(Auto-Stop Support / 自動停止機能付き)*

A lightweight batch image loading node for ComfyUI that incorporates 
a feature to simulate batch termination with “realistic-looking” error messages.

Designed for safe, unattended batch workflows such as high-resolution
upscaling with AI models.


「それっぽい」エラーメッセージでバッチ終了を演出する機能を組み込んだ、軽量な 
ComfyUI用バッチ画像読み込みノードです。

AIモデルを用いた連続アップスケール処理など、無人バッチ運用のために設計されています。

------------------------------------------------------------------------

## ✨ Features / 特徴

-   **Auto-Stop Logic / 自動停止機能**\
    After all images in the folder are processed, the node safely stops
    the ComfyUI queue by raising a controlled error.

    指定したフォルダの全画像を処理し終えると、自動的にメッセージを表示してエラー終了します。

-   **i18n Support / 国際化対応**\
    Messages automatically switch between English and Japanese based on
    OS language settings.

    OSの言語設定に合わせてメッセージが日本語/英語に切り替わります。

-   **High Compatibility Output / 高互換Tensor出力**\
    Outputs standard tensor format compatible with upscalers,
    FaceDetailer, and other processing nodes.

    各種アップスケーラーやFaceDetailerでそのまま使えるTensor形式を出力します。

## ⚙ Requirements / 依存関係

-   ComfyUI (latest recommended)
-   Python 3.9+
-   No additional external dependencies

    ComfyUIに必須のパッケージを除けば標準のpythonだけでまかなえているはずなので、
    通常のComfyUI環境であれば追加インストールは不要です。

------------------------------------------------------------------------

## 💡 Why This Node? / なぜこのノードが必要なのか？

When performing batch processing, unless the queue is run with the 
correct number of files, ComfyUI will attempt to process the next 
file after finishing the last image and terminate with an error.

This node provides:

-   Safe unattended execution
-   When a file cannot be found, output a “termination message” as an error message to reassure the user.
-   Reliable batch iteration using `Integer` node increment control

Ideal for overnight processing workflows.

バッチ処理を実行する場合、正しいファイル数でキューを回さない限り、 
ComfyUIは最後の画像を処理し終えた次のファイルを処理しようとしてエラー終了します。

このノードは次の機能を提供します：

-   無人実行でも安全に処理を継続
-   ファイルが見つからなかったときに「終了メッセージ」をエラーメッセージとして出力し、ユーザーを安心させる
-   「数値」ノードの「increment」でインデックス値を指定する確実なバッチ動作

夜間や長時間の連続処理に最適です。

------------------------------------------------------------------------

## 📦 Installation / インストール

1.  Download or clone this repository into "ComfyUI/custom_nodes/".

2.  Restart ComfyUI.

1.  このリポジトリを「ComfyUI/custom_nodes/」以下クローンするか、あるいはダウンロードしてください。

2.  あとはComfyUIを再起動するだけ。


------------------------------------------------------------------------

## 🛠 Usage / 使い方

1.  Add a `Integer` node.
2.  Set its value to `0`.
3.  Set `control_after_generate` to `increment`.
4.  Connect the `Integer` output to this node's `index` input.
5.  Set `Batch count` to the desired number (or a sufficiently large number).
6.  Run the queue.

The node will automatically stop after processing all images in the
target folder.

1.  このノードのほかに「整数」ノードを追加します。
2.  「値」を 0 に設定します。
3.  「生成後の制御」 を increment(増分) に設定します。
4.  「整数」ノードの出力を、本ノードの index 入力に接続します。
5.  「バッチ数」を処理したい枚数（または十分に大きな数値）に設定します。

キューを実行します。

指定したフォルダ内のすべての画像を処理し終えると、ノードが自動的にキューを停止します。


------------------------------------------------------------------------

## 🌍 Internationalization / 国際化

i18n directory structure:

    i18n/
     ├── en_US.json
     └── ja_JP.json

Messages are automatically selected based on your operating system
language.

メッセージの言語は自動的にOS設定に合わせて日英で切り替わります。

------------------------------------------------------------------------

## 🧩 File Structure / ファイル構成

    ComfyUI-Simple-Batch-Loader/
    ├── __init__.py
    ├── simple_batch_loader.py
    ├── README.md
    ├── LICENSE
    └── i18n/
        ├── en_US.json
        └── ja_JP.json

------------------------------------------------------------------------

## 🛡 License

MIT License

This project is released under the MIT License.
You are free to use, modify, distribute, and include it in commercial
projects.

------------------------------------------------------------------------

## 🤝 Contribution

Pull requests and suggestions are welcome.
If you encounter issues, feel free to open an issue on GitHub.

------------------------------------------------------------------------

## 🧘 Author Notes / 作者より

Created to simplify safe batch workflows in ComfyUI.
If it helps your pipeline, feel free to use and adapt it.
Enjoy 🙂

使いやすいバッチローダーが欲しかったので自作しました。
役立ちそうなら、ご自由に使ったり改造したりしてください。

