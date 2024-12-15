import reflex as rx
import asyncio
from rxconfig import config

# ---------------------------
# -- EFECTO TYPE WRITTING. --
# ---------------------------
class State(rx.State):
    """The main application state."""
    landingpage_text: str = ""

    async def landingpage_update(self):
        """Simulación de efecto de texto con animación de tipo escritura."""
        while True:
            for service in ["Music", "Poems", "Art", "Pictures"]:
                if self.landingpage_text != "Discover my ":
                    self.landingpage_text = "Discover my"
                for char in service:
                    await asyncio.sleep(0.2)
                    self.landingpage_text += char
                    yield
                self.landingpage_text += "."
                yield
                await asyncio.sleep(1)
                for char in range(len(service) + 1):
                    await asyncio.sleep(0.09)
                    self.landingpage_text = self.landingpage_text[:-1]
                    yield