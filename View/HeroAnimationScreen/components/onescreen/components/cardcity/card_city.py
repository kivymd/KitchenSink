from kivy.animation import Animation
from kivy.properties import StringProperty

from kivymd.uix.hero import MDHeroFrom


class CityCard(MDHeroFrom):
    source = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.tile.ids.image.ripple_duration_in_fast = 0.05

    def on_transform_in(self, instance_hero_widget, duration):
        Animation(
            radius=[0, 0, 0, 0],
            box_radius=[0, 0, 0, 0],
            duration=duration,
        ).start(instance_hero_widget)

    def on_transform_out(self, instance_hero_widget, duration):
        Animation(
            radius=[24, 24, 24, 24],
            box_radius=[0, 0, 24, 24],
            duration=duration,
        ).start(instance_hero_widget)
