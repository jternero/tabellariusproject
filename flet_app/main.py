import flet as ft
import requests

API_URL = "http://localhost:8000"


def main(page: ft.Page):
    page.title = "Scripts Runner"
    scripts_container = ft.Column()

    def load_scripts():
        resp = requests.get(f"{API_URL}/scripts")
        if resp.ok:
            scripts = resp.json()
            scripts_container.controls.clear()
            for script_name in scripts:
                scripts_container.controls.append(
                    ft.ElevatedButton(
                        text=f"Run {script_name}",
                        on_click=lambda e, s=script_name: run_script(s)
                    )
                )
            page.update()

    def run_script(script_name: str):
        requests.post(f"{API_URL}/scripts/{script_name}/run")

    page.add(
        ft.AppBar(title=ft.Text("Scripts Runner"), center_title=True),
        scripts_container,
    )
    load_scripts()


ft.app(target=main)
