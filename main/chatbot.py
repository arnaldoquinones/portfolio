# import reflex as rx
# import os
# import openai
# from dotenv import load_dotenv

# class State(rx.State):
#     # The current question being asked
#     question: str = ""
#     # Chat history as (question, answer) tuples
#     chat_history: list[tuple[str, str]] = []

#     async def answer(self):
#         """Fetch an answer from the OpenAI API and update the chat history."""
#         try:
#             # Validate that the question is not empty
#             if not self.question.strip():
#                 return
            
#             # Add question to chat history with a placeholder for the answer
#             self.chat_history.append((self.question, ""))
#             question_index = len(self.chat_history) - 1

#             # Set the OpenAI API key
#             openai.api_key = ("xxx")
#             if not openai.api_key:
#                 raise ValueError("API key is not set. Please check your environment variables.")

#             # Send the question to OpenAI
#             response = await openai.ChatCompletion.acreate(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": self.question}],
#                 temperature=0.7,
#                 stream=True,
#             )

#             # Process the streaming response
#             answer = ""
#             async for chunk in response:
#                 # Debugging: Log each chunk
#                 print(f"Chunk received: {chunk}")
#                 delta = chunk.get("choices", [{}])[0].get("delta", {})
#                 content = delta.get("content", os.getenv("OPENAI_API_KEY"))
#                 if content:
#                     answer += content
#                     self.chat_history[question_index] = (self.chat_history[question_index][0], answer)
#                     yield

#             # Clear the input question after processing
#             self.question = ""

#         except Exception as e:
#             # Log the error and display a message in the chat
#             error_message = f"Error: {str(e)}"
#             print(error_message)  # Log the error for debugging
#             self.chat_history.append(("System", error_message))
#             yield

# def qa(question, answer):
#     """Render a question-answer pair."""
#     return rx.box(
#         rx.text(f"Q: {question}", style={"font-weight": "bold"}),
#         rx.text(f"A: {answer}", style={"margin-left": "10px", "color": "gray"}),
#         style={"margin-bottom": "10px"},
#     )

# def chat():
#     """Render the chat history."""
#     return rx.box(
#         rx.foreach(
#             State.chat_history,
#             lambda messages: qa(messages[0], messages[1]),
#         ),
#         style={
#             "max-height": "300px",
#             "overflow-y": "auto",
#             "padding": "10px",
#             "border": "1px solid #ccc",
#             "background-color": "white",
#             "color": "black",
#         },
#     )

# def action_bar():
#     """Render the input field and ask button."""
#     return rx.hstack(
#         rx.input(
#             value=State.question,
#             placeholder="Ask a question...",
#             on_change=State.set_question,
#             style={"flex": 1, "margin-right": "10px"},
#         ),
#         rx.button(
#             "Ask",
#             on_click=State.answer,
#             style={"background-color": "#007BFF", "color": "white"},
#         ),
#         style={"margin-top": "10px"},
#     )

# def index():
#     """Render the main application."""
#     return rx.center(
#         rx.vstack(
#             chat(),
#             action_bar(),
#             align="center",
#             style={"width": "50%", "margin-top": "20px"},
#         ),
#     )

# # Initialize the Reflex app
# app = rx.App()
# app.add_page(index)


# import openai
# import os

# # Configurar la API key (manteniendo la original intacta)
# openai.api_key = "xxx"
# def get_answer(question):
#     """
#     Obtiene la respuesta de OpenAI para la pregunta dada.
#     """
#     try:
#         # Validar que la pregunta no esté vacía
#         if not question.strip():
#             print("La pregunta no puede estar vacía.")
#             return None

#         # Enviar la pregunta a OpenAI
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": question}],
#             temperature=0.7,
#         )
        
#         # Obtener la respuesta
#         answer = response["choices"][0]["message"]["content"]
#         return answer
#     except Exception as e:
#         print(f"Error al obtener la respuesta: {str(e)}")
#         return None

# def main():
#     """
#     Función principal para interactuar con el bot desde la terminal.
#     """
#     print("Bienvenido al chatbot interactivo. Escribe 'salir' para terminar.")
#     chat_history = []

#     while True:
#         # Solicitar pregunta al usuario
#         question = input("Tú: ")
        
#         # Salir si el usuario lo indica
#         if question.lower() == "salir":
#             print("¡Adiós!")
#             break
        
#         # Obtener respuesta del modelo
#         answer = get_answer(question)
#         if answer:
#             chat_history.append((question, answer))
#             print(f"Bot: {answer}")

# if __name__ == "__main__":
#     main()


