from kivy.app import App
from kivy.uix.label import Label


class Okno(App):
    title = "Моя первая программа"

    def build(self):  # не менять названия функции
        return Label(text="Привет Мир!")


if __name__ == "__main__":
    Okno().run()