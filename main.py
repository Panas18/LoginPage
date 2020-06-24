from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import (Screen, ScreenManager,
                                    NoTransition)
from kivy.lang import Builder
from database import table
import login
import Dialogue


class Screen1(Screen):

    user_name = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_button(self):

        if login.password_User(self):
            if self.password.text == login.password_User(self)[0][0]:
                self.user_name.text = ""
                self.password.text = ""
                MainApp().change_screen("Main")
            else:
                Dialogue.error_dialogue(self, "password is incorrect")
        else:
            self.password.text =""
            Dialogue.error_dialogue(self,"User name doesn't exist")
        

class Screen2(Screen):

    s_user_name = ObjectProperty(None)
    s_password = ObjectProperty(None)
    s_confirm_password = ObjectProperty(None)
    s_full_name = ObjectProperty(None)


    def signup_buton(self):

        if login.chech_validSignup(self):

            if login.check_alreadyUser(self):

                if login.check_passwordSignup(self):

                    table.insert_data(table, self)
                    table.print_data(table)
                    self.s_user_name.text = ""
                    self.s_password.text = ""
                    self.s_confirm_password.text = ""
                    self.s_full_name.text = ""
                    MainApp().change_screen("Main")


                else:
                    Dialogue.error_dialogue(self, "Enter same password")
            else:
                Dialogue.error_dialogue(self,"user name already in use. please try next one")
        else:
            Dialogue.error_dialogue(self, "Please fill the table completely")

kv = Builder.load_file("main.kv")

class Screen3(Screen):
    pass

class MainApp(MDApp):
    sm = ScreenManager(transition=NoTransition())


    def build(self):
        # self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(Screen1(name="login"))
        self.sm.add_widget(Screen2(name="signup"))
        self.sm.add_widget(Screen3(name="Main"))
        return self.sm

    def change_screen(self, screen):
        self.sm.current = screen


if __name__ == "__main__":
    MainApp().run()
