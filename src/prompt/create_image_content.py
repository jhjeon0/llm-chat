import base64


def create_image_content(file_path: str):
    content_list = []
    base64_image = _encode_image(file_path)
    image_url = f"{base64_image}"
    content_list.append(
        {"type": "image_url", "image_url": {"url": image_url}}  # type: ignore
    )
    return content_list


def _encode_image(image_path: str):
    with open(image_path, "rb") as image_file:
        img = base64.b64encode(image_file.read()).decode("utf-8")

    return f"data:image/jpeg;base64,{img}"
