import os
from enums.file_extension_enum import FileExtensionEnum


def save_file(file_name: str, file: bytes):
    _, extension = os.path.splitext(file_name)
    if extension.lower() in FileExtensionEnum.list():
        save_path = os.path.join(os.getenv("BASE_PATH"), file_name)

        with open(save_path, "wb") as f:
            f.write(file)
