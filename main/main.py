import reflex as rx
from rxconfig import config
from .modulos import sidebar_bottom_profile
from .about_me import about
from .skills import skills
from .proyects import proyects


class State(rx.State):
    # Controla la visibilidad del modal
    show_popup: bool = False  

    @staticmethod
    def set_show_popup(value: bool):
        """Actualiza la visibilidad del modal."""
        State.show_popup = value


def index() -> rx.Component:
    """Componente principal que renderiza la vista principal de la app."""
    return rx.box(
        rx.hstack(
            sidebar_bottom_profile(),
            rx.container(
                rx.vstack(
                    rx.heading(
                        rx.fragment(
                            rx.text("Data scientist"), 
                            rx.text("& Data analyst"),
                        ),
                        size="6"
                    ),
                    rx.image(
                        src="https://github.com/arnaldoquinones/portfolio/blob/master/assets/foto_perfil.png?raw=true",
                        width="150px",
                        height="auto",
                        border_radius="50%",
                        alt="Foto de perfil",
                    ),
                    rx.text(
                        """ "...Scientia est potentia..." """,
                        font_size="2em",
                        font_style="italic",
                        text_align="center",
                        color="white",
                    ),  # Texto añadido aquí
                    rx.hstack(
                        rx.link(
                            rx.button("GitHub", border_radius="20px", width="120px"),
                            href="https://github.com/arnaldoquinones",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button("Linkedin", border_radius="20px", width="120px"),
                            href="https://www.linkedin.com/in/apquinones/",
                            is_external=True,
                        ),
                        rx.button(
                            "Messages",
                            border_radius="20px",
                            width="120px",
                            on_click=lambda: State.set_show_popup(True),  # Abre el modal
                        ),
                        spacing="4",
                        align="center",
                    ),
                    spacing="5",
                    justify="center",
                ),
                padding="1em",
                flex="1",
            ),
        ),
        contact_popup(),  # Incluye el modal aquí
        min_height="100vh",
        width="100vw",
        background="linear-gradient(to bottom, #000066, #000000)",
        overflow_y="auto",
    )



app = rx.App()

def contact_popup() -> rx.Component:
    """Ventana emergente de contacto."""
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header("Envíanos un mensaje"),
                rx.modal_body(
                    rx.form(
                        rx.input(placeholder="Nombre", id="name"),
                        rx.input(placeholder="Email", id="email", type="email"),
                        rx.text_area(placeholder="Mensaje", id="message"),
                        rx.button("Enviar", type="submit"),
                        on_submit=lambda form_data: print("Formulario enviado:", form_data),  # Cambia esto por tu lógica de envío
                    )
                ),
                rx.modal_footer(
                    rx.button("Cerrar", on_click=lambda: State.set_show_popup(False))
                ),
            )
        ),
        is_open=State.show_popup,  # Controla la visibilidad con el estado
    )

# ---------------------------
# -- ENLACES A LAS PAGINAS --
# ---------------------------
def main_page() -> rx.Component:
    return rx.box(
        rx.link("About Me", href="./about_me"),
        rx.link("Skills", href="./skills"),
        rx.link("Projects", href="./proyects"),
        rx.text("Welcome to my Portfolio", size="3xl", font_weight="bold"),
        spacing="4",
        align="center",
        justify="center",
        height="100vh",
        bg="teal.100",
    )

# Add routes for the main page and subpages.
app.add_page(main_page)
app.add_page(about)
app.add_page(skills)
app.add_page(proyects)

app.add_page(index)  # Agregar la página principal.
