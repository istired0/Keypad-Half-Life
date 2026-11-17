print('starting')

import board 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

encoderHandler = EncoderHandler()
keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP4, board.GP2, board.GP4)
keyboard.row_pins = (board.GP6, board.GP7, board.GP0, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(encoderHandler)

keyboard.keymap = [
    [KC.MUTE, KC.A, KC.SLSH,   
    KC.B,    KC.C,    KC.D,  
    KC.E,    KC.F,    KC.G,  
    KC.H,    KC.I,    KC.J,  
]]

encoderHandler.pins = (
    (board.GP26, board.GP27,None, False),
    (board.GP28, board.GP29,None, False)
)
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU, KC.NO),
        (KC.LEFT, KC.RIGHT, KC.NO),
    )
]

if __name__ == "__main__":
    keyboard.go()