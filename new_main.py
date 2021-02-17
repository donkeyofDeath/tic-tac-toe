import visualization as visu

import pygame as pg

import sys

# Initialize everything.
# pygame.init() is include in the __init__-function of Graphics.
my_game = visu.Graphics()

# button_change_flag =

# Game loop.
while 1:
    # Check if the visuals correspond to the right state.
    my_game.check_visuals()
    # Check for events in the event que.
    for event in pg.event.get():
        # Check if the game was quit.
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # Check for mouse clicks.
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Save the position of the mouse at the moment the screen is clicked.
            pos_x, pos_y = pg.mouse.get_pos()
            my_game.on_click(pos_x, pos_y)
    # Update the screen.
    pg.display.flip()
    # If the game ended add a short delay
    # print(my_game.game_state.draw_flag)
    # if my_game.game_state.player2_win_flag or my_game.game_state.player1_win_flag or my_game.game_state.draw_flag:
        # pg.time.delay(500)
    # If the game did not end, add a delay so that the CPU is not occupied all the time.
    pg.time.delay(5)
