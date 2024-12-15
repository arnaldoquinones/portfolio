import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile


def proyects() -> rx.Component:
    """Página About Me."""
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading("About Me Page", size="3xl", color="white"),
                rx.text(
                    "Those are my works.",
                    size="lg",
                    color="gray.200",
                    text_align="center",
                ),
            ),
            padding="2em",
        ),
        min_height="100vh",
        background="linear-gradient(to bottom, #002266, #001122)",
    )