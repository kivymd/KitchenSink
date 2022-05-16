import os
import sys
from pathlib import Path

from kivy.core.window import Window

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
Window.softinput_mode = "below_target"


class KitchenSink(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Indigo"
        self.manager_screen = ManagerScreen()

    def build(self) -> ManagerScreen:
        self.manager_screen.add_widget(self.manager_screen.create_screen("menu"))
        return self.manager_screen


KitchenSink().run()
