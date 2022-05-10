from kivy.properties import StringProperty

from View.CardScreen.components.cards.basecard import BaseCard


class CardMessage(BaseCard):
    path_to_avatar = StringProperty()
    message = StringProperty()
    date = StringProperty()
    name_user = StringProperty()
