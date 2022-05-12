from kivy.clock import Clock

from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDFillRoundFlatIconButton


class ExtendedButton(RoundedRectangularElevationBehavior, MDFillRoundFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4
