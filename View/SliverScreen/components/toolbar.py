from kivy.properties import ObjectProperty

from kivymd.uix.toolbar import MDTopAppBar


class SliverToolbar(MDTopAppBar):
    manager_screen = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_back")
        self.type_height = "medium"
        self.headline_text = "Sport Girl"
        self.left_action_items = [["arrow-left", lambda x: self.dispatch("on_back")]]
        self.right_action_items = [
            ["attachment", lambda x: x],
            ["calendar", lambda x: x],
            ["dots-vertical", lambda x: x],
        ]

    def on_back(self, *args):
        self.manager_screen.current = "menu"
