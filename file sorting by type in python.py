import os
import shutil

folder_path = "C:/Users/adam/Downloads"  

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

for file in os.listdir(folder_path):
    filename, ext = os.path.splitext(file)
    ext = ext.lower()
    
    for folder, extensions in file_types.items():
        if ext in extensions:
            folder_location = os.path.join(folder_path, folder)
            if not os.path.exists(folder_location):
                os.makedirs(folder_location)
            source = os.path.join(folder_path, file)
            destination = os.path.join(folder_location, file)
            shutil.move(source, destination)
            print(f"Moved {file} to {folder}/")
