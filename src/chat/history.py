from langchain_core.messages import HumanMessage, AIMessage
import mesop.labs as mel
from enums.role_enum import RoleEnum


def get_history(history: list[mel.ChatMessage]):
    history_list = []
    for content in history:
        if content.role == RoleEnum.USER:
            history_list.append(HumanMessage(content=content.content))
        elif content.role == RoleEnum.ASSISTANT:
            history_list.append(AIMessage(content=content.content))

    return history_list
