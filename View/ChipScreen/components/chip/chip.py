from kivy.animation import Animation
from kivy.utils import get_color_from_hex

from kivymd.uix.chip import MDChip


class CustomChip(MDChip):
    icon_check_color = (0, 0, 0, 1)
    md_bg_color = (0, 0, 0, 0)
    line_color = get_color_from_hex("#ecaa98")
    text_color = get_color_from_hex("#442c2e")
    radius = [
        8,
    ]
    _no_ripple_effect = True

    def set_chip_text_color(self, instance_chip, active_value: int):
        Animation(color=(0, 0, 0, 1) if active_value else (0, 0, 0, 0.5), d=0.2).start(
            self.ids.label
        )
