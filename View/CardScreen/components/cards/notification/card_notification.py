from kivy.properties import StringProperty, ColorProperty

from View.CardScreen.components.cards.basecard import BaseCard


class CardNotification(BaseCard):
    text_top = StringProperty()
    secondary_text_top = StringProperty()
    icon_top = StringProperty()
    text_bottom = StringProperty()
    secondary_text_bottom = StringProperty()
    icon_bottom = StringProperty()
    icon_color = ColorProperty([1, 1, 1, 1])
