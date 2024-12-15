import reflex as rx
import asyncio
from rxconfig import config
from .modulos import sidebar_bottom_profile
from .modulos import top_banner_gradient
from .modulos import top_banner_signup

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

# Con más de 24 años de experiencia en el Banco ICBC, he desempeñado roles tanto en el área administrativa como en el comercial.

def index() -> rx.Component:
    """Componente principal que renderiza la vista principal de la app."""
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),
            rx.container(
                rx.color_mode.button(position="top-right"),
                rx.vstack(
                    rx.heading("Data scientist & Data analyst. ", size="9"),
                    rx.image(
                        src="https://github.com/arnaldoquinones/portfolio/blob/master/assets/foto_perfil.png?raw=true",
                        width="150px",
                        height="auto",
                        border_radius="50%",
                        alt="Foto de perfil",
                    ),
                    top_banner_gradient(),
                    top_banner_signup(),
                    rx.link(
                        rx.button("Go to my GitHub!",
                                  border_radius="20px"),
                        href="https://github.com/arnaldoquinones",
                        is_external=True,
                    ),
                    spacing="5",
                    justify="center",
                ),
                padding="1em",
                flex="1",
            ),
        ),
        min_height="100vh",
        width="100vw",
        background="linear-gradient(to bottom, #000066, #000000)",
        overflow_y="auto",
    )


app = rx.App()
app.add_page(index)  # Agregar la página principal
