import view 
import candies as can
from logger import game_logger as log
import x_o as xo

def button_click():
    a = view.choose_game()
    if a == 1:
       res = xo.run_game()
    elif a == 2:
        res = can.run_game()
    log(res)

if __name__=='__main__':
    button_click()
