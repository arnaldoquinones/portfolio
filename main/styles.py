import reflex as rx
import asyncio
from dotenv import load_dotenv
import os
# from rxconfig import config

# ---------------------------
# -- EFECTO TYPE WRITTING. --
# # ---------------------------
# class State(rx.State):
#     """The main application state."""
#     landingpage_text: str = ""

#     async def landingpage_update(self):
#         """Simulación de efecto de texto con animación de tipo escritura."""
#         while True:
#             for service in ["Music", "Poems", "Art", "Pictures"]:
#                 if self.landingpage_text != "Discover my ":
#                     self.landingpage_text = "Discover my"
#                 for char in service:
#                     await asyncio.sleep(0.2)
#                     self.landingpage_text += char
#                     yield
#                 self.landingpage_text += "."
#                 yield
#                 await asyncio.sleep(1)
#                 for char in range(len(service) + 1):
#                     await asyncio.sleep(0.09)
#                     self.landingpage_text = self.landingpage_text[:-1]
#                     yield


import requests

import openai

# Configuración de la API
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.goose.ai/v1"



def generar_respuesta(prompt):
    try:
        # Crear una solicitud de completado
        completion = openai.Completion.create(
            engine="gpt-j-6b",  # Cambiamos 'model' por 'engine'
            prompt=prompt,
            max_tokens=120,
            temperature=0.3,    # Añadimos temperature para controlar la creatividad
            stop=None          # Podemos especificar tokens de parada si lo deseamos
        )

        print("Respuesta generada:")
        print(completion.choices[0].text.strip())

    except Exception as e:
        print(f"Error: {e}")

# Solicitar el prompt al usuario
mi_prompt = input("Introduce tu prompt: ")
generar_respuesta(mi_prompt)

