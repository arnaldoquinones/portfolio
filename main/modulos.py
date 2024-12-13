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
    """Crea la lista principal de elementos del menú lateral."""
    return rx.vstack(
        sidebar_item("About me", "layout-dashboard", href="./about"),
        sidebar_item("Proyects", "square-library", href="./proyects"),
        sidebar_item("Skills", "bar-chart-4", href="./skills"),
        sidebar_item("Messages", "mail", on_click=MessageFormState.toggle_popover),
        spacing="3",  # Espaciado ajustado
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

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data



def form_example():
    return rx.cond(
        MessageFormState.is_popover_open,  # Condición para mostrar el pop-up
        rx.popover.root(
            rx.popover.trigger(
                rx.button("Popover"),
            ),
            rx.popover.content(
                rx.form(
                    rx.vstack(
                        rx.heading("Send a message", size="1xl", color="white"),
                        rx.input(
                            placeholder="First Name",
                            name="first_name",
                        ),
                        rx.input(
                            placeholder="Last Name",
                            name="last_name",
                        ),
                        rx.input(
                            placeholder="email",
                            name="email",
                        ),
                        rx.input(
                            placeholder="write your message",
                            name="message",
                        ),
                        rx.hstack(
                            rx.checkbox("Checked", name="check"),
                            rx.switch("Switched", name="switch"),
                        ),
                        rx.button("Submit", type="submit"),
                    ),
                    on_submit=MessageFormState.handle_submit,
                    reset_on_submit=True,
                ),
                rx.divider(),
                rx.heading("Results"),
                rx.text(MessageFormState.form_data.to_string()),
            ),
        ),
    )





# -------------------
# -- MENU DE LOGIN --
# -------------------


def login_multiple_thirdparty() -> rx.Component:
    return rx.card(
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
        size="4",
        max_width="28em",
        width="100%",
    )


# ----------------
# -- BANNER UNO --
# ----------------

class TopBannerGradient(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
            rx.flex(
                rx.text(
                    "The new Reflex version is now available! ",
                    rx.link(
                        "Read the release notes",
                        href="#",
                        underline="always",
                        display="inline",
                        underline_offset="2px",
                    ),
                    align_items=["start", "center"],
                    margin="auto",
                    spacing="3",
                    weight="medium",
                ),
                rx.icon(
                    "x",
                    cursor="pointer",
                    justify="end",
                    flex_shrink=0,
                    on_click=cls.toggle,
                ),
                wrap="nowrap",
                # position="fixed",
                justify="between",
                width="100%",
                # top="0",
                align="center",
                left="0",
                # z_index="50",
                padding="1rem",
                background=f"linear-gradient(99deg, {rx.color('blue', 4)}, {rx.color('pink', 3)}, {rx.color('mauve', 3)})",
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
        )
top_banner_gradient = TopBannerGradient.create



# -----------------
# -- BANNER TRES --
# -----------------
class TopBannerSignup(rx.ComponentState):
    hide: bool = False

    @rx.event
    def toggle(self):
        self.hide = not self.hide

    @classmethod
    def get_component(cls, **props):
        return rx.cond(
            ~cls.hide,
            rx.flex(
                rx.image(
                    src="/logo.jpg",   
                    width="2em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.text(
                    "Web apps in pure Python. Deploy with a single command.",
                    weight="medium",
                ),
                rx.flex(
                    rx.button(
                        "Sign up",
                        cursor="pointer",
                        radius="large",
                    ),
                    rx.icon(
                        "x",
                        cursor="pointer",
                        justify="end",
                        flex_shrink=0,
                        on_click=cls.toggle,
                    ),
                    spacing="4",
                    align="center",
                ),
                wrap="nowrap",
                # position="fixed",
                flex_direction=["column", "column", "row"],
                justify_content=["start", "space-between"],
                width="100%",
                # top="0",
                spacing="2",
                align_items=["start", "start", "center"],
                left="0",
                # z_index="50",
                padding="1rem",
                background=rx.color("accent", 4),
                border_radius="10px",
                **props,
            ),
            # Remove this in production
            rx.icon_button(
                rx.icon("eye"),
                cursor="pointer",
                on_click=cls.toggle,
            ),
            
        )

top_banner_signup = TopBannerSignup.create





def suma(a,b):
    c=a+b
    return print (c)

if __name__ == "__main__":
    suma(7,8)
