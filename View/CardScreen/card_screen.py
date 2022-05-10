from kivy.properties import DictProperty

from kivymd.uix.screen import MDScreen

from View.CardScreen.components import CardProfile  # NOQA
from View.CardScreen.components import CardMessage  # NOQA
from View.CardScreen.components import CardCall  # NOQA
from View.CardScreen.components import CardNotification  # NOQA


class CardScreenView(MDScreen):
    data_cards = DictProperty(
        {
            "profile": {
                "name_user": "Rachel",
                "date": "2 weeks ago",
                "status": "Chatted",
                "avatar": "images/card_screen/avatar-profile.jpg",
                "card_color": "#1e4974",
                "radius": 2
            },

            "message": {
                "name_user": "Monica Geller",
                "date": "1 hour ago",
                "message": "I`m making a lasagna for dinner",
                "avatar": "images/card_screen/avatar-message.jpg",
                "card_color": "#3b7fad",
                "radius": 4
            },

            "call": {
                "name_user": "Rachel",
                "radius": 4,
                "card_color": "#1e4974"
            },

            "notification": {
                "text_top": "New photos added • [size=12]5m[/size]",
                "secondary_text_top": "Oregon Coast",
                "icon_top": "email",
                "text_bottom": "Megan Ono • [size=12]5m[/size]",
                "secondary_text_bottom": "How was your trip?",
                "icon_bottom": "image",
                "card_color": "#5f9acc",
                "icon_color": "#1e4974"
            }
        }
    )
