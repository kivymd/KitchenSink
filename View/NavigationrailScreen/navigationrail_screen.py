import os

from kivy.metrics import dp
from kivy.uix.image import Image

from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from View.NavigationrailScreen.components.extendedbutton.extended_button import (
    ExtendedButton,
)  # NOQA


class NavigationrailScreenView(ThemableBehavior, MDScreen):
    def switch_screen(self, instance_navigation_rail, instance_navigation_rail_item):
        try:
            name_screen = instance_navigation_rail_item.icon.split("-")[1].lower()
        except IndexError:
            name_screen = instance_navigation_rail_item.icon.lower()

        if name_screen in self.ids.screen_manager.screen_names:
            self.ids.screen_manager.current = name_screen

    def on_enter(self):
        navigation_rail_items = self.ids.navigation_rail.get_items()[:]
        navigation_rail_items.reverse()

        for widget in navigation_rail_items:
            try:
                name_screen = widget.icon.split("-")[1].lower()
            except IndexError:
                name_screen = widget.icon.lower()

            screen = MDScreen(
                name=name_screen,
                md_bg_color=self.theme_cls.bg_darkest,
                radius=[18, 0, 0, 0],
            )
            label = MDLabel(
                text=name_screen.capitalize(),
                font_style="H6",
                halign="right",
                adaptive_height=True,
                shorten=True,
                padding_y=dp(12),
                padding_x=dp(12),
            )
            image = Image(
                source=(
                    f"{os.environ['KITCHEN_SINK_ASSETS']}/"
                    f"images/navigationrail_screen/{name_screen}.png"
                ),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            screen.add_widget(image)
            screen.add_widget(label)
            self.ids.screen_manager.add_widget(screen)
