import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def _init_(self,**kwargs):
        super(childApp, self)._init_()
        self.cols = 2
        self.add_widget(Label(text = 'name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        
        self.add_widget(Label(text = 'marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_work)

        self.add_widget(Label(text = 'gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        class parentApp(App):
            def build(self):
                return childApp()

                if _name_ == "_main_":
                    parentApp().run()