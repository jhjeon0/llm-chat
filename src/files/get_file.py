import os
import pandas as pd
from enums.file_extension_enum import FileExtensionEnum


def get_file_path(base_path: str):
    try:
        _, extension = os.path.splitext(os.listdir(base_path)[0])
        if extension.lower() in FileExtensionEnum.list():
            return (
                os.path.join(base_path, (os.listdir(base_path)[0])),
                extension.lower(),
            )
        return "", None
    except Exception:
        return "", None


def get_csv_file(file_path: str):
    df = pd.read_csv(file_path)
    return [df.to_string()]
