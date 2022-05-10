from kivy.properties import StringProperty

from View.common.rectangular_card import RectangularCard


class MenuCard(RectangularCard):
    title = StringProperty()
    source = StringProperty()
