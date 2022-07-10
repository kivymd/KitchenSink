from kivymd.uix.screen import MDScreen

from View.HeroAnimationScreen.components import OneScreenView, TwoScreenView


class HeroAnimationScreenView(MDScreen):
    def on_enter(self):
        if not self.ids.screen_manager.screens:
            self.ids.screen_manager.add_widget(
                OneScreenView(name="hero one screen")
            )
            self.ids.screen_manager.add_widget(
                TwoScreenView(name="hero two screen")
            )
