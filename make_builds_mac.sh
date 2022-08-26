#!/bin/bash
pyinstaller SD-desktop.py -w --noconfirm --onefile --icon ./assets/stock.png \
                           --add-data "assets:assets" --hidden-import=pytorch \
                          --hidden-import=huggingface_hub.repository  \
                          --copy-metadata torch --copy-metadata tqdm --copy-metadata regex \
                          --copy-metadata requests --copy-metadata packaging --copy-metadata filelock \
                          --copy-metadata tokenizers --copy-metadata importlib_metadata --copy-metadata numpy
./dist/SD-desktop                          