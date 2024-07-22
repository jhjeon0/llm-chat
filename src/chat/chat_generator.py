import os
from langchain_community.chat_models import ChatOpenAI
from prompt.prompt import base_prompt
from prompt.create_image_content import create_image_content
from files.get_file import get_file_path, get_csv_file
from enums.file_extension_enum import FileExtensionEnum, ImageExtensionEnum


def chat_completions(question: str, history: list):
    file_path, extension = get_file_path(os.getenv("BASE_PATH"))

    related_documents = []
    image_content = None
    if extension == FileExtensionEnum.CSV:
        related_documents = get_csv_file(file_path)
    if extension in ImageExtensionEnum.list():
        image_content = create_image_content(file_path)

    template = base_prompt(image_content)
    chain = _make_chain(template)
    try:
        for chunk in chain.stream(
            {
                "question": question,
                "history": history,
                "related_documents": related_documents,
            }
        ):
            yield chunk.content
    except Exception as exc:
        raise ValueError("check logic") from exc
    finally:
        if file_path != "":
            os.remove(file_path)


def _make_chain(template):
    model = ChatOpenAI(model_name="gpt-4o")
    return template | model
