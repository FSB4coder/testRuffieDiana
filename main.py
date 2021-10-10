from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import *
from sekonds import Seconds

age = 7
name = ""
p1, p2, p3 = 0, 0, 0

def check_int(age):
    try:
        age = int(age)
    except:
        return False
    return age

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        name = Label(text="Введите ваше имя")
        self.in_name = TextInput(multiline=False)
        age = Label(text="Введите ваш возраст", halign="right")
        self.in_age = TextInput(text="", multiline=False)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        box1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box1.add_widget(name)
        box1.add_widget(self.in_name)
        box2.add_widget(age)
        box2.add_widget(self.in_age)
        self.btn.on_press = self.next

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(box1)
        outer.add_widget(box2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global name, age
        age = check_int(self.in_age.text)
        name = self.in_name.text
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'


class PulseScr1(Screen):
    def __init__(self, name="PulseScr1", **kwargs):
        super().__init__(name=name, **kwargs)
        self.next_screen = False
        instr = Label(text=txt_test1)
        self.lbl_seconds = Seconds(15)
        self.lbl_seconds.bind(done=self.finished)
        result1 = Label(text="Введите результат:")
        self.in_result = TextInput(multiline=False)
        self.in_result.set_disabled(True)

        self.btn = Button(text='Start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        box1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box1.add_widget(result1)
        box1.add_widget(self.in_result)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(box1)
        outer.add_widget(self.lbl_seconds)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Продолжить"

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_seconds.start()
        else:
            global p1
            p1 = check_int(self.in_result)
            if p1 == False:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'


class PulseScr2(Screen):
    def __init__(self, name="PulseScr2", **kwargs):
        super().__init__(name=name, **kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text="Продолжить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        self.manager.current = 'pulse2'

class PulseScr3(Screen):
    def __init__(self, name="PulseScr3", **kwargs):
        super().__init__(name=name, **kwargs)
        self.next_screen = False
        instr = Label(text=txt_test3)
        self.lbl_seconds = Seconds(15)
        self.lbl_seconds.bind(done=self.finished)
        result1 = Label(text="Считайте пульс:")
        box1 = BoxLayout(size_hint=(0.8, None), height="30sp")

        result2 = Label(text="Результат:", halign="right")
        self.in_result2 = TextInput(text="", multiline=False)
        box1.add_widget(result2)
        box1.add_widget(self.in_result2)

        self.btn = Button(text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.on_press = self.next
        box2 = BoxLayout(size_hint=(0.8, None), height="30sp")

        result3 = Label(text="Результат после отдыха:", halign="right")
        self.in_result3 = TextInput(text="", multiline=False)
        box2.add_widget(result3)
        box2.add_widget(self.in_result3)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(box1)
        outer.add_widget(box2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)


# class Result(Screen):
#     def __init__(self, name="Result", **kwargs):
#         super().__init__(name=name, **kwargs)
#         self.instruction = Label(text="")
#         self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
#         self.outer.add_widget(self.instruction)
#         self.add_widget(self.outer)
#         self.on_enter = self.before
#
#     def before(self):
#         self.instruction.text = name + "\n" + test(p1, p2, p3, age)


class test_of_rufie(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='init'))
        sm.add_widget(PulseScr1(name='pulse1'))
        sm.add_widget(PulseScr2(name='sits'))
        sm.add_widget(PulseScr3(name='pulse2'))
        # sm.add_widget(Result(name='result'))
        return sm


app = test_of_rufie()
app.run()
