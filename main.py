from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from math import sqrt
from functools import partial

font_size = 35


class CalculatorButton(Button):
    """Кастомная кнопка с предустановленными стилями"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = font_size
        self.background_normal = ''
        self.background_color = (0.2, 0.2, 0.2, 1)


class Main_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_buttons = []
        self.create_ui()

    def create_ui(self):
        # Основные контейнеры
        main_layout = BoxLayout(orientation='vertical')
        self.lbl = Label(
            text='',
            font_size=font_size,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2),
            halign='right',
            valign='middle'
        )
        main_layout.add_widget(self.lbl)

        # Создаем кнопки с помощью GridLayout
        grid = GridLayout(cols=4, rows=5, spacing=5, padding=5)

        # Конфигурация кнопок: (текст, обработчик, параметры)
        buttons = [
            ('C', self.clear), ('√', self.sqrt), ('(', partial(self.add_text, '(')), (')', partial(self.add_text, ')')),
            ('7', partial(self.add_text, '7')), ('8', partial(self.add_text, '8')), ('9', partial(self.add_text, '9')),
            ('/', partial(self.add_text, '/')),
            ('4', partial(self.add_text, '4')), ('5', partial(self.add_text, '5')), ('6', partial(self.add_text, '6')),
            ('*', partial(self.add_text, '*')),
            ('1', partial(self.add_text, '1')), ('2', partial(self.add_text, '2')), ('3', partial(self.add_text, '3')),
            ('-', partial(self.add_text, '-')),
            ('<-', self.delete), ('0', partial(self.add_text, '0')), ('=', self.calculate),
            ('+', partial(self.add_text, '+')),
        ]

        # Создаем кнопки и добавляем их в grid
        for text, handler in buttons:
            btn = CalculatorButton(text=text)
            btn.bind(on_press=handler)
            grid.add_widget(btn)
            self.all_buttons.append(btn)

        main_layout.add_widget(grid)
        self.add_widget(main_layout)

    # Общие методы обработки
    def add_text(self, char, *args):
        self.lbl.text += char

    def clear(self, *args):
        self.lbl.text = ''
        for btn in self.all_buttons:
            btn.disabled = False

    def delete(self, *args):
        self.lbl.text = self.lbl.text[:-1]

    def sqrt(self, *args):
        try:
            self.lbl.text = str(sqrt(float(self.lbl.text)))
        except:
            self.show_error()

    def calculate(self, *args):
        try:
            self.lbl.text = str(eval(self.lbl.text))
        except ZeroDivisionError:
            self.lbl.text = "На ноль делить нельзя"
            self.disable_buttons()
        except:
            self.show_error()

    def show_error(self):
        self.lbl.text = "Ошибка"
        self.disable_buttons()

    def disable_buttons(self):
        for btn in self.all_buttons:
            if btn.text not in {'C', '='}:
                btn.disabled = True


class CalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main_Screen(name='main'))
        return sm


if __name__ == '__main__':
    CalculatorApp().run()