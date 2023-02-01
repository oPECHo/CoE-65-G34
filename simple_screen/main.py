from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HelloWorldApp(App):
    def on_login(self, instance):
        print(self.username_input.text, self.password_input.text)

    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Login", font_size=50))

        username_layout = BoxLayout()
        username_layout.add_widget(Label(text="Username"))
        self.username_input = TextInput(multiline=False)
        username_layout.add_widget(self.username_input)
        layout.add_widget(username_layout)

        password_layout = BoxLayout()
        password_layout.add_widget(Label(text="Password"))
        self.password_input = TextInput(password=True, multiline=False)
        password_layout.add_widget(self.password_input)
        layout.add_widget(password_layout)

        layout.add_widget(Button(text="Submit", on_press=self.on_login))
        return layout


if __name__ == "__main__":
    HelloWorldApp().run()
