import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.utils.set_bars_colors import set_bars_colors
from kivymd.color_definitions import colors

from View.screens import screens


class ManagerScreen(ScreenManager):
    dialog_wait = None
    _screen_names = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.transition = NoTransition()

    def on_current(self, *args):
        super().on_current(*args)
        self.set_bars_colors(self.app.theme_cls, self.current)

    def set_bars_colors(self, instance_theme_cls, name_screen: str) -> None:
        primary_color = instance_theme_cls.primary_color
        bg_normal = instance_theme_cls.bg_normal

        panel_colors = {
            "menu": {
                "status_bar_color": primary_color,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Light",
            },
            "card": {
                "status_bar_color": primary_color,
                "navigation_bar_color": primary_color,
                "navigation_icon_color": "Light",
            },
            "button": {
                "status_bar_color": get_color_from_hex("#b88bf8"),
                "navigation_bar_color": get_color_from_hex("#b88bf8"),
                "navigation_icon_color": "Light",
            },
            "button_0": {
                "status_bar_color": get_color_from_hex("#b88bf8"),
                "navigation_bar_color": get_color_from_hex("#b88bf8"),
                "navigation_icon_color": "Light",
            },
            "button_1": {
                "status_bar_color": get_color_from_hex(colors["Green"]["800"]),
                "navigation_bar_color": get_color_from_hex(colors["Green"]["800"]),
                "navigation_icon_color": "Light",
            },
            "field": {
                "status_bar_color": primary_color,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Light",
            },
            "field_0": {
                "status_bar_color": primary_color,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Light",
            },
            "field_1": {
                "status_bar_color": primary_color,
                "navigation_bar_color": primary_color,
                "navigation_icon_color": "Light",
            },
            "field_2": {
                "status_bar_color": bg_normal,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Dark",
            },
            "chip": {
                "status_bar_color": bg_normal,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Dark",
            },
            "list": {
                "status_bar_color": bg_normal,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Dark",
            },
            "sliver": {
                "status_bar_color": get_color_from_hex("#90d1f0"),
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Dark",
            },
            "tile": {
                "status_bar_color": primary_color,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Light",
            },
            "rail": {
                "status_bar_color": get_color_from_hex("#fffcf4"),
                "navigation_bar_color": get_color_from_hex("#fffcf4"),
                "navigation_icon_color": "Dark",
            },
            "hero": {
                "status_bar_color": primary_color,
                "navigation_bar_color": bg_normal,
                "navigation_icon_color": "Light",
            },
        }

        if name_screen in panel_colors:
            set_bars_colors(
                panel_colors[name_screen]["status_bar_color"],
                panel_colors[name_screen]["navigation_bar_color"],
                panel_colors[name_screen]["navigation_icon_color"],
            )

    def create_screen(self, name_screen):
        if name_screen not in self._screen_names:
            self._screen_names.append(name_screen)
            self.load_common_package(name_screen)
            exec(f"import View.{screens[name_screen]}")
            self.app.load_all_kv_files(
                os.path.join(self.app.directory, "View", screens[name_screen].split(".")[0])
            )
            view = eval(
                f'View.{screens[name_screen]}.{screens[name_screen].split(".")[0]}View()'
            )
            view.name = name_screen
            return view

    def load_common_package(self, name_screen) -> None:
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
        dots_path = os.path.join("View", "common", "dots", "dots.kv")

        if name_screen in ["list"]:
            _load_kv(one_line_list_item_path)
        elif name_screen in ["button", "field"]:
            _load_kv(dots_path)

    def switch_screen(self, screen_name: str) -> None:
        def switch_screen(*args):
            if screen_name not in self._screen_names:
                self.open_dialog()
                screen = self.create_screen(screen_name)
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
            image = Image(
                source="assets/images/loading.gif",
                size_hint=(0.15, 0.15),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            self.dialog_wait = ModalView(
                background="assets/images/modal-bg.png",
            )
            self.dialog_wait.add_widget(image)
        self.dialog_wait.open()

    def add_screen(self, view) -> None:
        self.add_widget(view)
