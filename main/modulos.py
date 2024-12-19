import reflex as rx
from rxconfig import config


# -------------------------
# -- BARRA SIDEBAR  MENU --
# -------------------------
class MessageFormState(rx.State):
    form_data: dict = {}
    is_popover_open: bool = False  # Estado para controlar la visibilidad del pop-up

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.is_popover_open = False  # Cierra el pop-up después de enviar el formulario

    @rx.event
    def toggle_popover(self):
        """Toggle the popover visibility."""
        self.is_popover_open = not self.is_popover_open

def sidebar_item(text: str, icon: str, href: str = None, on_click: rx.EventHandler = None) -> rx.Component:
    """Crea un elemento del menú lateral."""
    link_props = {"href": href} if href else {"on_click": on_click}

    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="90%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        **link_props,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("About me", "layout-dashboard", href="./about"),
        sidebar_item("Projects", "square-library", href="./proyects"),
        sidebar_item("Skills", "bar-chart-4", href="./skills"),
        sidebar_item("Messages", "mail", on_click=MessageFormStateV2.toggle_popover),  # Alterna el pop-up
        spacing="3",
        width="12em",
    )




def sidebar_bottom_profile() -> rx.Component:
    """Crea el perfil inferior de la barra lateral."""
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/logo.png",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href="./",  # Ruta a la página principal (main)
                    ),
                    rx.link(
                        rx.heading(
                            "My portfolio.", size="5", weight="bold"
                        ),
                        href="./",  # Ruta a la página principal (main)
                        style={
                            "color": "white",  # Mantiene el color del texto en blanco
                            "text-decoration": "none",  # Elimina subrayados
                            "_hover": {
                                "color": "white",  # Mantiene blanco al pasar el mouse
                            },
                        },
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.divider(margin_y="2"),  # Ajustado a un valor válido
                rx.vstack(
                    rx.hstack(
                            rx.vstack(
                            rx.box(
                                rx.text(
                                    "Made by",
                                    size="3",
                                    weight="bold",
                                ),
                                rx.link(
                                    "Arnaldo Quiñones",
                                    href="https://github.com/arnaldoquinones",
                                    size="2",
                                    weight="medium",
                                    color="blue.500",
                                    is_external=True,
                                ),
                                width="100%",
                            ),
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    width="100%",
                    spacing="2",  # Espaciado entre elementos inferiores
                ),
                spacing="3",  # Espaciado general ajustado
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                height="650px",
                width="12em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.divider(margin_y="2"),  # Ajustado a un valor válido
                            rx.hstack(
                                rx.icon_button(
                                    rx.icon("user"),
                                    size="3",
                                    radius="full",
                                ),
                                rx.vstack(
                                    rx.box(
                                        rx.text(
                                            "Made by",
                                            size="3",
                                            weight="bold",
                                        ),
                                        rx.link(
                                            "Arnaldo Quiñones",
                                            href="https://github.com/arnaldoquinones",
                                            size="2",
                                            weight="medium",
                                            color="blue.500",
                                            is_external=True,
                                        ),
                                        width="100%",
                                    ),
                                    justify="start",
                                    width="100%",
                                ),
                                padding_x="0.5rem",
                                align="center",
                                justify="start",
                                width="100%",
                            ),
                            spacing="2",  # Espaciado entre los elementos inferiores
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )

# -------------------------
# -- POP UP WINDOW EMAIL --
# -------------------------

class MessageFormStateV2(rx.State):
    is_popover_open: bool = False  # Controla la visibilidad del pop-up
    form_data: dict = {}          # Almacena los datos enviados del formulario

    @rx.event
    def toggle_popover(self):
        """Alterna la visibilidad del pop-up."""
        self.is_popover_open = not self.is_popover_open

    @rx.event
    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario y cierra el pop-up."""
        self.form_data = form_data
        self.is_popover_open = False  # Cierra el pop-up tras el envío



def pop_up_message():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.heading("Contact me", size="2", color="white"),
                rx.dialog.close(  # Coloca el botón con el ícono de cierre en la esquina superior derecha
                    rx.button(
                        rx.icon("x"),  # Usamos el ícono de la cruz
                        size="1",  # Hace el ícono más pequeño
                        on_click=MessageFormStateV2.toggle_popover,  # Cierra el pop-up
                        style={
                            "position": "absolute",
                            "top": "0",
                            "right": "0",
                            "background": "transparent",  # Hace el fondo transparente
                            "border": "transparent",  # Elimina el borde
                            "color": "white",  # Color blanco para la cruz
                            "padding": "0",  # Elimina el padding
                            "font-size": "1px",  # Ajusta el tamaño del ícono
                            }
                    )
                ),
            ),
            rx.dialog(
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="First Name", name="first_name"),
                        rx.input(placeholder="Last Name", name="last_name"),
                        rx.input(placeholder="Email", name="email"),
                        rx.text_area(
                            placeholder="Write your message", 
                            name="message",
                            style={  # Estilos de redimensionado para el input de mensaje
                                # "padding-top": "10px",  # Ajusta la distancia desde la parte superior
                                # "padding-left": "10px",  # Ajusta la distancia desde el lado izquierdo
                                "text-align": "left",  # Asegura que el texto esté alineado a la izquierda
                                # "height": "150px", 
                                "resize": "vertical",  # Habilita redimensionamiento en ambas direcciones
                                "overflow": "auto",  # Activa el desplazamiento si el contenido excede el tamaño
                                "min_height": "50px",  # Altura mínima para el input
                                "min_width": "170px",  # Ancho mínimo para el input
                                "white-space": "pre-wrap",  # Permite saltos de línea automáticamente
                                "word-wrap": "break-word",  # Asegura que las palabras largas se ajusten
                            }
                        ),
                        rx.button("Submit", type="submit"),
                    ),
                    on_submit=MessageFormStateV2.handle_submit,  # Maneja el envío
                    reset_on_submit=True,
                )
            ),
            style={
                "max-width": "200px",  # Establece un ancho máximo
                "width": "auto",  # Ajusta el ancho al contenido
                "padding": "1rem",  # Agrega un pequeño espacio alrededor del contenido
                "position": "relative",
                "background": rx.color("accent", 3)  # Para asegurar que el ícono se posicione correctamente
            }
        ),
        open=MessageFormStateV2.is_popover_open,  # Vincula directamente el estado
    )



# class FormState(rx.State):
#     form_data: dict = {}

#     @rx.event
#     def handle_submit(self, form_data: dict):
#         """Handle the form submit."""
#         self.form_data = form_data

# def form_example():
#     return rx.vstack(
#         rx.form(
#             rx.vstack(
#                 rx.input(
#                     placeholder="Email Address",
#                     name="email",
#                     type="email",
#                 ),
#                 rx.button("Submit", type="submit"),
#             ),
#             on_submit=FormState.handle_submit,
#             reset_on_submit=True,
#         ),
#     )


# -------------------
# -- LOG IN WINDOW --
# -------------------



def login_multiple_thirdparty() -> rx.Component:
    return rx.center(  # Asegura que la tarjeta esté centrada
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.image(
                        src=("https://github.com/arnaldoquinones/my_portfolio/blob/master/assets/foto_perfil.png?raw=true"),
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Sign in to your account",
                        size="6",
                        as_="h2",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text(
                            "New here?",
                            size="3",
                            text_align="left",
                        ),
                        rx.link("Sign up", href="#", size="3"),
                        spacing="2",
                        opacity="0.8",
                        width="100%",
                    ),
                    justify="start",
                    direction="column",
                    spacing="4",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    justify="start",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Forgot password?",
                            href="#",
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%"),
                rx.hstack(
                    rx.divider(margin="0"),
                    rx.text(
                        "Or continue with",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    rx.divider(margin="0"),
                    align="center",
                    width="100%",
                ),
                rx.center(
                    rx.icon_button(
                        rx.icon(tag="github"),
                        variant="soft",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="facebook"),
                        variant="soft",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="twitter"),
                        variant="soft",
                        size="3",
                    ),
                    spacing="4",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            size="2",
            max_width="24em",  # Tamaño ajustado para que no sea tan ancho
            width="50%",       # Ajusta el porcentaje del ancho
            background_color="#4a90e2",  # Fondo azul
            padding="2em",     # Espaciado interno
            border_radius="1em",  # Bordes redondeados
            shadow="5",       # Añade sombra para profundidad
        ),
        height="100vh",  # Asegura que el contenedor use toda la altura disponible
        align_items="center",
        justify_content="center",
    )






def suma(a,b):
    c=a+b
    return print (c)

if __name__ == "__main__":
    suma(7,8)
