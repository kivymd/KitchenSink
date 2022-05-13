from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from View.ButtonScreen.components import ButtonScreenOneScreen, ButtonScreenTwoScreen  # NOQA
from View.common.dots import Dots  # NOQA
from View.common.round_card import RoundCard  # NOQA
from View.slide_animatior import SlideAnimatior


class ButtonScreenView(ThemableBehavior, MDScreen, SlideAnimatior):
    pass
