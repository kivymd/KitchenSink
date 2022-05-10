from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from View.FieldScreen import OneScreen, TwoScreen, Dots  # NOQA
from View.FieldScreen.components.thirdscreen.third_screen import ThirdScreen  # NOQA
from View.slide_animatior import SlideAnimatior


class FieldScreenView(
    ThemableBehavior,
    MDScreen,
    SlideAnimatior,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
