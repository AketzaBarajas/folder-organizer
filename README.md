# Folder Organizer

A Python script that sorts the files in your Downloads folder into subfolders by file type.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

Downloads folders fill up with installers, PDFs and images all mixed together. This script reads every file in `~/Downloads`, looks at its extension and moves it into a matching subfolder, creating the subfolder if it does not exist yet.

It uses only the Python standard library (`os` and `shutil`). The folder names it creates and the messages it prints are in Spanish.

## Features

- **Sorts by extension** into seven folders:

  | Folder         | Extensions                                                |
  | -------------- | --------------------------------------------------------- |
  | `Imagenes`     | `.jpg` `.jpeg` `.png` `.gif` `.webp`                      |
  | `Documentos`   | `.doc` `.docx` `.xls` `.xlsx` `.ppt` `.pptx` `.txt`       |
  | `PDFs`         | `.pdf`                                                    |
  | `Videos`       | `.mp4` `.mkv` `.avi` `.mov` `.webm`                       |
  | `Comprimidos`  | `.zip` `.rar`                                             |
  | `Instaladores` | `.exe` `.msi` `.bat`                                      |
  | `Otros`        | anything else                                             |

- **Finds the folder on its own:** the path is built from the current user's home directory, so there is nothing to configure.
- **Skips hidden files** (names starting with a dot).
- **Keeps going on errors:** a file that cannot be moved is reported and the rest are still processed.

## Getting started

Requires Python 3. There is nothing to install.

```bash
git clone https://github.com/AketzaBarajas/folder-organizer.git
cd folder-organizer
python src/organizar_descargas.py
```

The script moves files as soon as it runs and has no preview or undo, so try it first on a Downloads folder you do not mind reorganising.

If it reports that the path was not found, your system uses a different name for the Downloads folder. `python src/encontrar_ruta.py` prints your home directory and the folders in it that look like a downloads folder.

To change the categories, edit the `extensiones` dictionary at the top of `src/organizar_descargas.py`.

## Status

A working first version, run by hand. Known limits: it only handles a folder named `Downloads`, it treats subfolders like any other entry, so a second run moves the category folders themselves into `Otros`, and it has no automated tests.

## License

[MIT](LICENSE)
