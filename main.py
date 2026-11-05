import flet as ft


class ContadorApp:
    """Construye la interfaz y responde a los eventos del usuario."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.valor = 0  # estado del contador

        # Componentes gráficos
        self.texto = ft.Text(str(self.valor), size=60)
        self.boton_mas = ft.IconButton(ft.Icons.ADD, on_click=self.incrementar)
        self.boton_reset = ft.IconButton(ft.Icons.REFRESH, on_click=self.reiniciar)

        self._configurar_pagina()
        self._construir_interfaz()

    def _configurar_pagina(self):
        self.page.title = "Contador interactivo"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # Evento de teclado: la barra espaciadora también suma
        self.page.on_keyboard_event = self.tecla_presionada

    def _construir_interfaz(self):
        self.page.add(
            self.texto,
            ft.Row(
                [self.boton_mas, self.boton_reset],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

    # ----- Manejadores de eventos -----
    def incrementar(self, e):
        self.valor += 1
        self._actualizar()

    def reiniciar(self, e):
        self.valor = 0
        self._actualizar()

    def tecla_presionada(self, e: ft.KeyboardEvent):
        if e.key == " ":
            self.incrementar(e)

    def _actualizar(self):
        self.texto.value = str(self.valor)
        self.page.update()  # refresca la interfaz


def main(page: ft.Page):
    ContadorApp(page)


ft.run(main)