import os

from kivymd.uix.screen import MDScreen

from View.SliverScreen.components import SliverCard


class SliverScreenView(MDScreen):
    def on_enter(self):
        if not self.ids.content.children:
            for x in range(10):
                self.ids.content.add_widget(
                    SliverCard(
                        image=f"{os.environ['KITCHEN_SINK_ASSETS']}/images/sliver_screen/avatar.png"
                    )
                )
