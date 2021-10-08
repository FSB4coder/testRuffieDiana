from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from instruction import txt_instruction
from instruction import txt_test1
from instruction import txt_test3
from instruction import txt_sits
from rufie import *
age = 7
name = ""
p1, p2, p3 = 0,0,0
class SuperButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.txt = Label()
        self.screen = screen
        self.goal = goal
        self.direction = direction

    def change_text(self, text):
        self.txt.text = text

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        name = Label(text="Введите ваше имя")
        self.in_name = TextInput(multiline=False)
        age = Label(text="Введите ваш возраст", halign="right")
        self.in_age = TextInput(text="", multiline=False)
        btn = SuperButton(self, text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}, goal="PulseScr1", direction="left", background_color="green")
        box1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box1.add_widget(name)
        box1.add_widget(self.in_name)
        box2.add_widget(age)
        box2.add_widget(self.in_age)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(box1)
        outer.add_widget(box2)
        outer.add_widget(btn)
        self.add_widget(outer)

    def next(self):
        global name, age
        age = (self.in_age.text)
        name = self.in_name.text


class PulseScr1(Screen):
    def __init__(self,name="PulseScr1", **kwargs):
        super().__init__(name=name, **kwargs)
        instr = Label(text=txt_test1)
        result1 = Label(text="Введите результат:")
        self.in_result = TextInput(multiline=False)

        btn = SuperButton(self, text="Продолжить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}, goal="PulseScr2",
                          direction="left", background_color="green")
        box1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box1.add_widget(result1)
        box1.add_widget(self.in_result)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(box1)
        outer.add_widget(btn)
        self.add_widget(outer)
    def next(self):
        global p1
        p1 = int(self.in_result)

class PulseScr2(Screen):
    def __init__(self,name="PulseScr2" ,**kwargs):
        super().__init__(name=name, **kwargs)
        instr = Label(text=txt_sits)

        btn = SuperButton(self, text="Продолжить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}, goal="PulseScr3",
                          direction="left", background_color="green")
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(btn)
        self.add_widget(outer)
class PulseScr3(Screen):
    def __init__(self, name="PulseScr3",**kwargs):
        super().__init__(name=name, **kwargs)
        instr = Label(text=txt_test3)
        result1 = Label(text="Результат:")
        self.in_result1 = TextInput(multiline=False)
        result2 = Label(text="Результат после отдыха:", halign="right")
        self.in_result2 = TextInput(text="", multiline=False)
        btn = SuperButton(self, text="Завершить", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}, goal="Result",
                          direction="left", background_color="green")
        box1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        box1.add_widget(result1)
        box1.add_widget(self.in_result1)
        box2.add_widget(result2)
        box2.add_widget(self.in_result2)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(box1)
        outer.add_widget(box2)
        outer.add_widget(btn)
        self.add_widget(outer)

    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
class Result(Screen):
    def __init__(self,name="Result", **kwargs):
        super().__init__(name=name, **kwargs)
        self.instruction = Label(text="")
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instruction)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        self.instruction.text = name + "\n" + test(p1, p2, p3, age)
class test_of_rufie(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr())
        sm.add_widget(PulseScr1())
        sm.add_widget(PulseScr2())
        sm.add_widget(PulseScr3())
        sm.add_widget(Result())
        return sm


app = test_of_rufie()
app.run()
