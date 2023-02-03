from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

user_database = [
    dict(username="admin", password="adminadmin"),
    dict(username="tl", password="123456"),
]


class PlayGameScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.add_widget(Label(text="Go"))


class LoginScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10)
        layout.add_widget(Label(text="Login", font_size=50))

        username_layout = BoxLayout()
        username_layout.add_widget(Label(text="Username"))
        self.username_input = TextInput(multiline=False, size_hint_y=None)
        username_layout.add_widget(self.username_input)
        layout.add_widget(username_layout)

        password_layout = BoxLayout()
        password_layout.add_widget(Label(text="Password"))
        self.password_input = TextInput(password=True, multiline=False)
        password_layout.add_widget(self.password_input)
        layout.add_widget(password_layout)

        layout.add_widget(Button(text="Submit", on_press=self.on_login))
        self.add_widget(layout)

    def on_login(self, instance):
        for user in user_database:
            if (
                user["username"] == self.username_input.text.strip()
                and user["password"] == self.password_input.text
            ):
                print("Hello", self.username_input.text)
                self.manager.current = "play_game"
                break


class HelloWorldApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(PlayGameScreen(name="play_game"))
        return self.sm


if __name__ == "__main__":
    HelloWorldApp().run()
