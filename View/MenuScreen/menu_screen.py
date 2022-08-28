import os

from kivymd.uix.screen import MDScreen

from View.MenuScreen.componemts import MenuCard  # NOQA


class MenuScreenView(MDScreen):
    def on_enter(self, *args) -> None:
        if not self.ids.menu_list.data:
            manu_list = [
                "Field",
                "Card",
                "Button",
                "Chip",
                "List",
                "Sliver",
                "Rail",
                "Tile",
                "Hero",
            ]
            manu_list.sort()
            for name_card in manu_list:
                self.ids.menu_list.data.append(
                    {
                        "viewclass": "MenuCard",
                        "title": name_card,
                        "elevation": 3,
                        "on_release": lambda x=name_card.lower(): self.manager.switch_screen(
                            x
                        ),
                        "source": (
                            f"{os.environ['KITCHEN_SINK_ASSETS']}/"
                            f"images/menu_screen/{name_card.lower()}.png"
                        ),
                    }
                )
