# 📂 Download Folder Organizer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

**Download Folder Organizer** is an automation script developed in Python designed to end the chaos in your Downloads folder.

## 💡 What does this project do?
This script scans your Downloads folder and automatically organizes files by moving them to specific subfolders (such as Pictures, Documents, Installers, etc.) based on their extension.

It uses the system's native `os` and `shutil` libraries for fast and efficient file management.

## 🚧 Project Status
**Version: 1.0 (Prototype)**
This project is in its first working version. Currently, it functions as a manually executed script. It is recommended to test with non-critical files before using it on a large scale.

## ⚙️ How the Organization Works
The script identifies the extension of each file and automatically moves it to its corresponding folder according to the following list:

- '.jpg','.jpeg','.png','.gif','.webp' --> Images
- '.doc','.docx','.xls','.xlsx','.ptt','.pttx','.txt' --> Documents
- '.pdf' --> PDFs
- '.mp4','.mkv','.avi','.mov','.webm' --> Videos
- '.zip','.rar' --> Compressed
- '.exe','.msi','.bat' --> Installers
- Other type of filde --> Others

> **Note** If the destination folder does not exist, the script will automatically create it before moving the files.

## 📋 Requirements

* **Python 3.x** installed on your system.
* **No external dependencies:** This project uses the standard Python libraries (`os` and `shutil`), so you **don't need to install anything** with `pip`. Download and use!

## 🚀 Instructions for Use

1. Download the code or clone the repository.
2. Open a terminal in the project folder.
3. Run the main script:
```bash
`` python main.py
``
*(Make sure to replace `main.py` with the actual name of your file if it's different.)*
4. Check your downloads folder: The chaos will be gone!

## 🔧 Customization

The script is configured to search the **Downloads** folder by default. If you want to change the source path or destination folders, open the `main.py` file (or whatever your script is called) and look for the configuration variables at the beginning:

```python
# Example configuration
source_dir = "C:/Users/YourUsername/Downloads"
