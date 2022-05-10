import os
import sys
from pathlib import Path

from kivy import Config

from PIL import ImageGrab

resolution = ImageGrab.grab().size
Config.set("graphics", "height", resolution[1])
Config.set("graphics", "width", "400")

from kivymd.app import MDApp

from View.ManagerScreen.manager_screen import ManagerScreen

if getattr(sys, "frozen", False):
    os.environ["KITCHEN_SINK_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["KITCHEN_SINK_ROOT"] = str(Path(__file__).parent)
os.environ["KITCHEN_SINK_ASSETS"] = os.path.join(
    os.environ["KITCHEN_SINK_ROOT"], f"assets{os.sep}"
)


class KitchenSink(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Indigo"
        self.manager_screen = ManagerScreen()

    def build(self) -> ManagerScreen:
        # self.load_all_kv_files(os.path.join(self.directory, "View", "common"))
        self.manager_screen.add_widget(
            self.manager_screen.create_screen("menu", self)
        )
        return self.manager_screen


KitchenSink().run()
