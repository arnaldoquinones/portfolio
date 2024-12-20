import reflex as rx
import os
from openai import AsyncOpenAI



class State(rx.State):
    # The current question being asked
    question: str
    # Chat history as (question, answer) tuples
    chat_history: list[tuple[str, str]]

    async def answer(self):
        client = AsyncOpenAI(
            api_key=os.environ["OPENAI_API_KEY"]
        )

        session = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to chat history
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear question input
        self.question = ""
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (
                    self.chat_history[-1][0],
                    answer,
                )
                yield

def chat():
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )

def action_bar():
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
        ),
    )

def index():
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )

# export OPENAI_API_KEY="your-api-key-here"

app = rx.App()
app.add_page(index)