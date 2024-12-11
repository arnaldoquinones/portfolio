"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .modulos import sidebar_item


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Professional web page!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            # top_banner_gradient(), 
            # top_banner_signup(),
            rx.image(
    src=("https://github.com/arnaldoquinones/my_portfolio/blob/master/assets/foto_perfil.png?raw=true"),  # Ruta relativa al archivo en 'assets'
    width="150px",  # Ajusta el tamaño según sea necesario
    height="auto",
    border_radius="50%",  # Para hacerlo circular, si lo deseas
    alt="Foto de perfil",
),
    #          login_multiple_thirdparty(),rx.image(
    #     src="./foto_perfil.png",  # Ruta relativa al archivo en 'assets'
    #     width="150px",  # Ajusta el tamaño según sea necesario
    #     height="auto",
    #     border_radius="50%",  # Para hacerlo circular, si lo deseas
    #     alt="Foto de perfil",
    # ),
            # top_banner_newsletter(), # Uso correcto del componente
            rx.link(
                rx.button("Go to my GitHub!"),
                href="https://github.com/arnaldoquinones",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        # rx.logo(),
    )


app = rx.App()
app.add_page(index)
