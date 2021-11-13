from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.core.window import Window

resource_add_path('C:/Windows/fonts')
LabelBase.register(DEFAULT_FONT, 'msgothic.ttc')

Window.size = (776, 692)

class TestApp(App):
    pass

if __name__ == '__main__':
    TestApp().run()