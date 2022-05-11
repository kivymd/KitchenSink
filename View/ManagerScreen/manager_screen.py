import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from View.screens import screens


class ManagerScreen(ScreenManager):
    dialog_wait = None
    _screen_names = []

    def create_screen(self, name_screen, app):
        if name_screen not in self._screen_names:
            self._screen_names.append(name_screen)
            self.load_common_package(app, name_screen)
            exec(f"import View.{screens[name_screen]}")
            app.load_all_kv_files(
                os.path.join(app.directory, "View", screens[name_screen].split(".")[0])
            )
            view = eval(
                f'View.{screens[name_screen]}.{screens[name_screen].split(".")[0]}View()'
            )
            view.name = name_screen
            return view

    def load_common_package(self, app, name_screen) -> None:
        def _load_kv(path_to_kv):
            kv_loaded = False
            for loaded_path_kv in Builder.files:
                if path_to_kv in loaded_path_kv:
                    kv_loaded = True
                    break
            if not kv_loaded:
                if name_screen in ["list"]:
                    from kivy.factory import Factory

                    Factory.register(
                        "OneLineItem",
                        module="View.common.onelinelistitem.one_line_list_item",
                    )
                Builder.load_file(path_to_kv)

        one_line_list_item_path = os.path.join(
            "View", "common", "onelinelistitem", "one_line_list_item.kv"
        )

        if name_screen in ["list"]:
            _load_kv(one_line_list_item_path)

    def switch_screen(self, screen_name: str) -> None:
        def switch_screen(*args):
            if screen_name not in self._screen_names:
                self.open_dialog()
                screen = self.create_screen(screen_name, MDApp.get_running_app())
                self.add_screen(screen)

            self.current = screen_name
            self.dialog_wait.dismiss()

        if screen_name not in self._screen_names:
            self.open_dialog()
            Clock.schedule_once(switch_screen)
        else:
            self.current = screen_name

    def open_dialog(self) -> None:
        if not self.dialog_wait:
            content = FloatLayout()
            image = Image(
                source="assets/images/loading.gif",
                size_hint=(0.15, 0.15),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            content.add_widget(image)
            self.dialog_wait = ModalView(background_color=(0, 0, 0, 0))
            self.dialog_wait.add_widget(content)
        self.dialog_wait.open()

    def add_screen(self, view) -> None:
        self.add_widget(view)
