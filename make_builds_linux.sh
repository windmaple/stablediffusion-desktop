#!/bin/bash
pyinstaller SD-desktop.py --noconsole --noconfirm --onefile --icon ./assets/stock.png \
                          --add-data "assets:assets" --hidden-import=huggingface_hub.repository \
                          --copy-metadata torch --copy-metadata tqdm --copy-metadata regex \
                          --copy-metadata requests --copy-metadata packaging --copy-metadata filelock \
                          --copy-metadata numpy --copy-metadata tokenizers --copy-metadata importlib_metadata