import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile  # Importa form_contact

def skills() -> rx.Component:
    """Página Skills."""
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),  # Barra lateral
            rx.container(
                rx.vstack(
                    rx.heading("Skills Page", size="3", color="white"),
                    rx.text(
                        "Let me show you my skills.",
                        size="5",
                        color="gray.200",
                        text_align="center",
                    ),
                ),
                width="100%",  # Añadí esto para que el contenedor ocupe todo el ancho
            ),
            width="100%",
            align_items="start",
        ),
        min_height="100vh",
        width="100vw",
        background="linear-gradient(to bottom, #002266, #001122)",
        overflow_y="auto",
    )
