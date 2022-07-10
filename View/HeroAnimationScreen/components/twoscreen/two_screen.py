from kivy.metrics import dp

from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen


class TwoScreenView(MDScreen):
    def on_enter(self):
        step = -36

        for name_image in [
            "Germany", "USA", "Australia", "Canada", "Dubai", "London"
        ]:
            step += 36
            image = FitImage(
                size_hint=(None, None),
                size=("56dp", "56dp"),
                radius=dp(56) / 2,
                source=f"assets/images/hero_screen/{name_image}.jpg",
                x=step,
            )
            self.ids.previews_box.add_widget(image)

    def on_tap_button_close(self) -> None:
        self.manager.current = "hero one screen"
