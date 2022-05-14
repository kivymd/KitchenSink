import os

from kivymd.uix.screen import MDScreen

from View.MenuScreen.componemts import MenuCard  # NOQA


class MenuScreenView(MDScreen):
    def on_enter(self, *args) -> None:
        if not self.ids.menu_list.data:
            for name_card in [
                "Field",
                "Card",
                "Button",
                "Chip",
                "List",
                "Sliver",
                "Rail",
                "Tile",
            ]:
                self.ids.menu_list.data.append(
                    {
                        "viewclass": "MenuCard",
                        "title": name_card,
                        "elevation": 12,
                        "on_release": lambda x=name_card.lower(): self.manager.switch_screen(
                            x
                        ),
                        "source": (
                            f"{os.environ['KITCHEN_SINK_ASSETS']}/"
                            f"images/menu_screen/{name_card.lower()}.png"
                        ),
                    }
                )
