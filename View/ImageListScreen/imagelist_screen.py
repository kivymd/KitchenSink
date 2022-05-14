import os

from kivymd.uix.screen import MDScreen

from View.ImageListScreen.components import ImageListScreenTile, ImageListScreenToolbar  # NOQA


class ImageListScreenView(MDScreen):
    def on_enter(self, *args):
        if not self.ids.grid_list.data:
            for i in range(6):
                self.ids.grid_list.data.append(
                    {
                        "viewclass": "ImageListScreenTile",
                        "icon": "book-open-outline",
                        "source":
                            f"{os.environ['KITCHEN_SINK_ASSETS']}/"
                            f"images/imagelist_screen/{i+1}.jpg",
                        "text": {
                            1: "Classic",
                            2: "Leisure",
                            3: "Children's books",
                            4: "E-books",
                            5: "Special literature",
                            6: "Books for study",
                        }[i+1],
                    }
                )
