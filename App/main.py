from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList


class NavigationDrawer(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class TestNavigationDrawer(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('main.kv')

    def on_start(self):
        icons_item = {
            "home": "Home",
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with others",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


TestNavigationDrawer().run()