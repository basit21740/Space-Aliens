#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021

import ugame
import stage

import constants

def game_scene():


    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    

    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    game = stage.Stage(ugame.dsiplay, 60)

    game.layers = [ship] + [background]

    game.render_block()

    while True:

        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            print("A")
        if keys & game.K_O != 0:
            print("B")
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0: 
            print("Select")

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENTS_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE),ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship. x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED) , ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        game.render_sprites({ship})
        game.tick()

if __name__ == "__main__":
    game_scene()
