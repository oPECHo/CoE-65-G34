from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HelloWorldApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Head"))

        username_layout = BoxLayout()
        username_layout.add_widget(Label(text="Password"))
        username_layout.add_widget(TextInput(multiline=False))
        layout.add_widget(username_layout)

        password_layout = BoxLayout()
        password_layout.add_widget(Label(text="Password"))
        password_layout.add_widget(TextInput(password=True, multiline=False))
        layout.add_widget(password_layout)

        layout.add_widget(Button(text="Submit"))
        return layout


if __name__ == "__main__":
    HelloWorldApp().run()
