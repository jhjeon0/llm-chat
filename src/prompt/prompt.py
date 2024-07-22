from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)


SYSTEM_PROMPT = """You're a trustworthy AI assistant. Answer the question based on <related_documents>\n
If your don't know, just say you don't know it.
<related_documents>: {related_documents}
"""


def base_prompt(image_content_list: list | None = None):
    content_list = [{"type": "text", "text": "\n<human>: {question}"}]

    if image_content_list is not None:
        content_list.extend(image_content_list)

    human_template = HumanMessagePromptTemplate.from_template(content_list)

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_PROMPT,
            ),
            MessagesPlaceholder(variable_name="history"),
            human_template,
        ]
    )
