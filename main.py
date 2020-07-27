from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.screenmanager import Screen, ScreenManager
from helpers import navigation_helper, screen_helper
# Window.size = (300, 500)  # Remove this when pushing app to production

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        # screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    DemoApp().run()
