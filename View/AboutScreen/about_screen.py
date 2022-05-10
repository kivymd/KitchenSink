import os

from kivymd.uix.screen import MDScreen


class AboutScreenView(MDScreen):
    def on_enter(self) -> None:
        if not self.ids.about_label.text:
            with open(
                f"{os.environ['KITCHEN_SINK_ROOT']}/assets/data/about_screen/about.txt",
                encoding="utf-8",
            ) as about:
                self.ids.about_label.text = about.read()
