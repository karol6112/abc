from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
WindowManager:
    MainWindow:
    SecondWindow:

<MainWindow>:
    name: "main"

    GridLayout:
        cols:1

        GridLayout:
            cols: 2

            Label:
                text: "Password: "

            TextInput:
                id: passw
                multiline: False

        Button:
            text: "Submit"
            on_release:
                app.root.current = "second" if passw.text == "tim" else "main"
                root.manager.transition.direction = "left"


<SecondWindow>:
    name: "second"

    Button:
        text: "Go Back"
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"