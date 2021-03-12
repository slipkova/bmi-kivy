from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget
import json


class MyItem(TwoLineAvatarListItem):
    def __init__(self, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = kwargs["book"]
        self.secondary_text = kwargs["author"]
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f"images/{kwargs['genre']}.png")
        self.add_widget(self.image)

    def on_press(self):
        print(self.text)

    def on_touch_up(self, touch):
        pass


class Books(BoxLayout):
    # kwargs a args pro slovníky, listy atd zkrátka arguments
    def __init__(self, *args, **kwargs):
        super(Books, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        with open("modules/books.json", encoding="UTF-8") as file:
            for i in json.load(file):
                list.add_widget(MyItem(author=i['author'], book=i['book'], genre=i['genre']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)
