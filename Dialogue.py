from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import (MDFillRoundFlatButton,
                               MDFlatButton)

def error_dialogue(screen, message):

    dialog = MDDialog(
        text = message,
        buttons = [
            MDFlatButton(
                text = "OK",
                #on_release= MainApp().change_screen(screen)
            )
        ]
    )
    dialog.open()

