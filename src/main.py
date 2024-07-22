import base64
import mesop as me
import mesop.labs as mel

from chat.history import get_history
from chat.chat_generator import chat_completions
from files.save_file import save_file


@me.stateclass
class State:
    name: str
    size: int
    mime_type: str
    contents: str
    sidenav_open: bool


SIDENAV_WIDTH = 500


@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/chat",
    title="Chat Demo",
)
def page():
    state = me.state(State)

    # sidenav
    with me.sidenav(opened=state.sidenav_open, style=me.Style(width=SIDENAV_WIDTH)):
        me.markdown("## Upload Files")
        with me.box(style=me.Style(padding=me.Padding.all(15))):
            me.uploader(
                label="Upload Files",
                accepted_file_types=["*"],
                on_upload=handle_upload,
                type="flat",
                color="primary",
                style=me.Style(font_weight="bold"),
            )

        if state.contents:
            with me.box(style=me.Style(margin=me.Margin.all(10))):
                me.text(f"File name: {state.name}")
                me.text(f"File size: {state.size}")
                me.text(f"File type: {state.mime_type}")

            with me.box(style=me.Style(margin=me.Margin.all(10))):
                me.image(src=state.contents)

    # sidenav content
    with me.box(
        style=me.Style(
            margin=me.Margin(left=SIDENAV_WIDTH if state.sidenav_open else 0),
        ),
    ):
        with me.content_button(on_click=on_click):
            with me.tooltip(message="Upload Files"):
                me.icon("menu")

    # chat-demo
    mel.chat(transform, title="Chat Demo", bot_user="JH-bot")


def handle_upload(event: me.UploadEvent):
    state = me.state(State)
    state.name = event.file.name
    state.size = event.file.size
    state.mime_type = event.file.mime_type
    state.contents = f"data:{event.file.mime_type};base64,{base64.b64encode(event.file.getvalue()).decode()}"

    save_file(state.name, event.file.getvalue())


def on_click(e: me.ClickEvent):
    s = me.state(State)
    s.sidenav_open = not s.sidenav_open


def transform(question: str, history: list[mel.ChatMessage]):
    history_list = get_history(history)
    return chat_completions(question, history_list)
