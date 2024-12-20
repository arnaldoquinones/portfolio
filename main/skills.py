import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile, pop_up_message

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
                    spacing="5",  # Añadido para consistencia con `proyects`
                    justify="center",  # Centra el contenido verticalmente
                ),
                padding="1em",  # Añadido para margen interno
                flex="1",  # Permite que el contenedor ocupe el espacio disponible
            ),
            pop_up_message(),  # Mueve el pop-up fuera del contenedor principal
        ),
        min_height="100vh",
        width="100vw",
        background="linear-gradient(to bottom, #002266, #001122)",
        overflow_y="auto",
    )
