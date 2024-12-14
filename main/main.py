"""Pagina profesional de mis trabajos  Data Tech y resumen curricular."""

import reflex as rx

from rxconfig import config
from .modulos import sidebar_item
# from .modulos TopBannerSignup
# from .modulos top_banner_signup

from .modulos import sidebar_bottom_profile # Importar la barra lateral
from .modulos import top_banner_gradient
from .modulos import top_banner_signup

class State(rx.State):
    """The app state."""
    ...


def index() -> rx.Component:
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),
            rx.container(
                rx.color_mode.button(position="top-right"),
                rx.vstack(
                    rx.heading("Welcome to my Professional web page!", size="9"),
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
                        rx.button("Go to my GitHub!"),
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
        min_height="100vh",  # Asegura que el fondo cubra al menos la pantalla completa
        width="100vw",
        background="linear-gradient(to bottom, #000066, #000000)",  # Fondo degradado
        overflow_y="auto",  # Permite desplazamiento vertical si es necesario
    )





app = rx.App()
app.add_page(index)  # Agregar la página principal