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
    pass


class LoginScreen(Screen):
    def on_login(self):
        print("in on login")
        for user in user_database:
            if (
                user["username"] == self.ids.username.text.strip()
                and user["password"] == self.ids.password.text
            ):
                print("Hello", self.ids.username.text)
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
