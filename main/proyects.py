import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile


def proyects() -> rx.Component:
    """Página Poryects."""
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),  # Barra lateral
            rx.container(
                rx.vstack(
                    rx.heading("Proyects Page", size="3xl", color="white"),
                    rx.text(
                        "Those are my works.",
                        size="lg",
                        color="gray.200",
                        text_align="center",
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
        background="linear-gradient(to bottom, #002266, #001122)",
        overflow_y="auto",
    )