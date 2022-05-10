from kivy.properties import StringProperty


from View.CardScreen.components.cards.basecard import BaseCard


class CardProfile(BaseCard):
    path_to_avatar = StringProperty()
    name_user = StringProperty()
    status = StringProperty()
    date = StringProperty()
