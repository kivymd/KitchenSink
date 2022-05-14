from kivy.properties import StringProperty
from kivymd.uix.imagelist import MDSmartTile


class ImageListScreenTile(MDSmartTile):
    icon = StringProperty()
    text = StringProperty()

