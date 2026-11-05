# Contador interactivo con Flet

Aplicación mínima hecha con **Flet** para la asignatura de Programación
Orientada a Objetos (tema: interfaces gráficas y eventos).

## ¿Qué es Flet?
Framework de Python para crear aplicaciones de escritorio, web y móvil
usando controles basados en Flutter, sin necesidad de programar frontend.

## Instalación
```bash
git clone https://github.com/Eidy19pertuz/contador-flet.git
cd contador-flet
python -m venv venv
venv\Scripts\activate      # En Linux/Mac: source venv/bin/activate
pip install -r requerimientos.txt
```

## Ejecución
```bash
flet run main.py
```
(Con `--web` se abre en el navegador.)

## Explicación del ejemplo
Muestra un contador en cero. Cada clic en el botón "+" lo incrementa;
el botón de reinicio lo vuelve a cero. La barra espaciadora también suma.

## Funcionamiento de los eventos
- `on_click` de los `IconButton` llama a `incrementar` y `reiniciar`.
- `page.on_keyboard_event` llama a `tecla_presionada`.
- Los métodos modifican `texto.value` y llaman a `page.update()`.

## Diseño orientado a objetos
`ContadorApp` guarda el estado, construye los componentes y maneja los eventos.

## Evidencia
![Captura](capturas/contador.png)

## Fuentes consultadas
https://flet.dev/
https://flet.dev/docs/getting-started/installation
https://pypi.org/project/flet/