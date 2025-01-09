from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from math import sqrt


font_size = 35
class Main_Screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.lbl=Label(text='',font_size=font_size,color=(1,1,1,1))

        # пустая клетка для выровнения
        self.btn_C = Button(text='C',font_size=font_size)

        # знаки
        self.btn_divide = Button(text='/',font_size=font_size)
        self.btn_multiply = Button(text='*',font_size=font_size)
        self.btn_minus = Button(text='-',font_size=font_size)
        self.btn_plus = Button(text='+',font_size=font_size)
        self.btn_equals = Button(text='=',font_size=font_size)


        #обновление проги
        self.btn_bracket_up = Button(text='(', font_size=font_size)
        self.btn_bracket_down = Button(text=')', font_size=font_size)
        self.btn_delete = Button(text='->', font_size=font_size)
        self.btn_sqrt = Button(text='√', font_size=font_size)


        # создаем кнопки
        self.btn1 = Button(text='1',font_size=font_size)
        self.btn2 = Button(text='2',font_size=font_size)
        self.btn3 = Button(text='3',font_size=font_size)
        self.btn4 = Button(text='4',font_size=font_size)
        self.btn5 = Button(text='5',font_size=font_size)
        self.btn6 = Button(text='6',font_size=font_size)
        self.btn7 = Button(text='7',font_size=font_size)
        self.btn8 = Button(text='8',font_size=font_size)
        self.btn9 = Button(text='9',font_size=font_size)
        self.btn0 = Button(text='0',font_size=font_size)

        # создаем лайоууты
        layout00 = BoxLayout(orientation='horizontal')
        layout0 = BoxLayout(orientation='horizontal')
        layout1 = BoxLayout(orientation='horizontal')
        layout2 = BoxLayout(orientation='horizontal')
        layout3 = BoxLayout(orientation='horizontal')
        layout4 = BoxLayout(orientation='horizontal')
        other = BoxLayout(orientation='vertical')

        layout00.add_widget(self.lbl)

        #первые триряда
        layout0.add_widget(self.btn_delete)
        layout0.add_widget(self.btn_sqrt)
        layout0.add_widget(self.btn_bracket_up)
        layout0.add_widget(self.btn_bracket_down)

        # вторые триряда
        layout1.add_widget(self.btn7)
        layout1.add_widget(self.btn8)
        layout1.add_widget(self.btn9)

        layout1.add_widget(self.btn_divide)

        # третьи триряда
        layout2.add_widget(self.btn4)
        layout2.add_widget(self.btn5)
        layout2.add_widget(self.btn6)

        layout2.add_widget(self.btn_multiply)

        # четвертые триряда
        layout3.add_widget(self.btn1)
        layout3.add_widget(self.btn2)
        layout3.add_widget(self.btn3)

        layout3.add_widget(self.btn_minus)

        #пятый три ряда
        layout4.add_widget(self.btn_C)
        layout4.add_widget(self.btn0)
        layout4.add_widget(self.btn_equals)
        layout4.add_widget(self.btn_plus)

        # добавляем все лайоуты
        other.add_widget(layout00)
        other.add_widget(layout0)
        other.add_widget(layout1)
        other.add_widget(layout2)
        other.add_widget(layout3)
        other.add_widget(layout4)

        # выводим на экран
        self.add_widget(other)


        # вывод клавишь от 1-9 и 0
        self.btn0.bind(on_press=self.write_0)
        self.btn1.bind(on_press=self.write_1)
        self.btn2.bind(on_press=self.write_2)
        self.btn3.bind(on_press=self.write_3)
        self.btn4.bind(on_press=self.write_4)
        self.btn5.bind(on_press=self.write_5)
        self.btn6.bind(on_press=self.write_6)
        self.btn7.bind(on_press=self.write_7)
        self.btn8.bind(on_press=self.write_8)
        self.btn9.bind(on_press=self.write_9)
        # вывод +-*/
        self.btn_plus.bind(on_press=self.write_plus)
        self.btn_minus.bind(on_press=self.write_minus)
        self.btn_multiply.bind(on_press=self.write_multiply)
        self.btn_divide.bind(on_press=self.write_devide)
        self.btn_C.bind(on_press=self.write_C)
        self.btn_equals.bind(on_press=self.write_equal)

        self.btn_delete.bind(on_press=self.write_delete)
        self.btn_sqrt.bind(on_press=self.write_sqrt)
        self.btn_bracket_up.bind(on_press=self.write_bracket_up)
        self.btn_bracket_down.bind(on_press=self.write_bracket_down)


        #созание функций для вывода чисел
    def write_0(self,btn):
        self.lbl.text = self.lbl.text + '0'

    def write_1(self,btn):
        self.lbl.text = self.lbl.text + '1'

    def write_2(self,btn):
        self.lbl.text = self.lbl.text + '2'

    def write_3(self,btn):
        self.lbl.text = self.lbl.text + '3'

    def write_4(self,btn):
        self.lbl.text = self.lbl.text + '4'

    def write_5(self,btn):
        self.lbl.text = self.lbl.text + '5'

    def write_6(self,btn):
        self.lbl.text = self.lbl.text + '6'

    def write_7(self,btn):
        self.lbl.text = self.lbl.text + '7'

    def write_8(self,btn):
        self.lbl.text = self.lbl.text + '8'

    def write_9(self,btn):
        self.lbl.text = self.lbl.text + '9'

    # созание функций для вывода знаков
    def write_plus(self,btn):
        self.lbl.text = self.lbl.text + '+'

    def write_minus(self,btn):
        self.lbl.text = self.lbl.text + '-'

    def write_devide(self,btn):
        self.lbl.text = self.lbl.text + '/'

    def write_multiply(self,btn):
        self.lbl.text = self.lbl.text + '*'

    def write_C(self,btn):
        self.lbl.text = ''

        self.btn1.set_disabled(False)
        self.btn2.set_disabled(False)
        self.btn3.set_disabled(False)
        self.btn4.set_disabled(False)
        self.btn5.set_disabled(False)
        self.btn6.set_disabled(False)
        self.btn7.set_disabled(False)
        self.btn8.set_disabled(False)
        self.btn9.set_disabled(False)
        self.btn0.set_disabled(False)
        self.btn_plus.set_disabled(False)
        self.btn_minus.set_disabled(False)
        self.btn_multiply.set_disabled(False)
        self.btn_equals.set_disabled(False)
        self.btn_divide.set_disabled(False)
        self.btn_delete.set_disabled(False)
        self.btn_sqrt.set_disabled(False)
        self.btn_bracket_up.set_disabled(False)
        self.btn_bracket_down.set_disabled(False)


    def write_sqrt(self, btn):
        self.lbl.text = str(sqrt(float(self.lbl.text)))

    def write_bracket_up(self, btn):
        self.lbl.text = self.lbl.text + '('

    def write_bracket_down(self, btn):
        self.lbl.text = self.lbl.text + ')'

    def write_delete(self, btn):
        self.lbl.text = self.lbl.text[:-1]


    def write_equal(self, btn):
        try :
            self.lbl.text = str(eval(str(self.lbl.text)))
        except ZeroDivisionError:
            self.lbl.text = 'На ноль делить нельзя'
            self.btn1.set_disabled(True)
            self.btn2.set_disabled(True)
            self.btn3.set_disabled(True)
            self.btn4.set_disabled(True)
            self.btn5.set_disabled(True)
            self.btn6.set_disabled(True)
            self.btn7.set_disabled(True)
            self.btn8.set_disabled(True)
            self.btn9.set_disabled(True)
            self.btn0.set_disabled(True)
            self.btn_plus.set_disabled(True)
            self.btn_minus.set_disabled(True)
            self.btn_multiply.set_disabled(True)
            self.btn_equals.set_disabled(True)
            self.btn_divide.set_disabled(True)
            self.btn_delete.set_disabled(True)
            self.btn_sqrt.set_disabled(True)
            self.btn_bracket_up.set_disabled(True)
            self.btn_bracket_down.set_disabled(True)

        except SyntaxError:
            self.lbl.text = 'так нельзя'
            self.btn1.set_disabled(True)
            self.btn2.set_disabled(True)
            self.btn3.set_disabled(True)
            self.btn4.set_disabled(True)
            self.btn5.set_disabled(True)
            self.btn6.set_disabled(True)
            self.btn7.set_disabled(True)
            self.btn8.set_disabled(True)
            self.btn9.set_disabled(True)
            self.btn0.set_disabled(True)
            self.btn_plus.set_disabled(True)
            self.btn_minus.set_disabled(True)
            self.btn_multiply.set_disabled(True)
            self.btn_equals.set_disabled(True)
            self.btn_divide.set_disabled(True)
            self.btn_delete.set_disabled(True)
            self.btn_sqrt.set_disabled(True)
            self.btn_bracket_up.set_disabled(True)
            self.btn_bracket_down.set_disabled(True)

        except ValueError:
            self.lbl.text = 'так нельзя'
            self.btn1.set_disabled(True)
            self.btn2.set_disabled(True)
            self.btn3.set_disabled(True)
            self.btn4.set_disabled(True)
            self.btn5.set_disabled(True)
            self.btn6.set_disabled(True)
            self.btn7.set_disabled(True)
            self.btn8.set_disabled(True)
            self.btn9.set_disabled(True)
            self.btn0.set_disabled(True)
            self.btn_plus.set_disabled(True)
            self.btn_minus.set_disabled(True)
            self.btn_multiply.set_disabled(True)
            self.btn_equals.set_disabled(True)
            self.btn_divide.set_disabled(True)
            self.btn_delete.set_disabled(True)
            self.btn_sqrt.set_disabled(True)
            self.btn_bracket_up.set_disabled(True)
            self.btn_bracket_down.set_disabled(True)


class App(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main_Screen())

        return sm

App = App()
App.run()