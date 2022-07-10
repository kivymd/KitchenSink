from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.screen import MDScreen

from View.HeroAnimationScreen.components import CityCard


class OneScreenView(MDScreen):
    def on_enter(self):
        if not self.ids.box.children:
            for name_image in [
                "Germany", "USA", "Australia", "Canada", "Dubai", "London"
            ]:
                card = CityCard(
                    source=f"assets/images/hero_screen/{name_image}.jpg",
                    tag=name_image,
                    size_hint_y=None,
                    height="200dp",
                )
                card.ids.tile.bind(on_release=self.on_tap_city_card)
                self.ids.box.add_widget(card)

    def on_tap_city_card(self, tile: MDSmartTile) -> None:
        def switch_screen(*args):
            self.manager.current_hero = tile.parent.tag
            self.manager.current = "hero two screen"

        Clock.schedule_once(switch_screen, 0.1)

    def back_to_menu(self):
        MDApp.get_running_app().manager_screen.current = "menu"
