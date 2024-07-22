from enum import StrEnum


class FileExtensionEnum(StrEnum):
    TXT = ".txt"
    DOCX = ".docx"
    DOC = ".doc"
    PDF = ".pdf"
    PNG = ".png"
    JPG = ".jpg"
    JPEG = ".jpeg"
    CSV = ".csv"

    @classmethod
    def list(cls) -> list:
        return [c.value for c in cls]


class ImageExtensionEnum(StrEnum):
    PNG = ".png"
    JPG = ".jpg"
    JPEG = ".jpeg"

    @classmethod
    def list(cls) -> list:
        return [c.value for c in cls]
