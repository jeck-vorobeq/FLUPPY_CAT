import wrap_py, wrap_py.ru

speed = 1





wrap_py.world.create_world(1930, 1010)

player = wrap_py.sprite.add_sprite("flappy_bird", 500, 500)


# управление
@wrap_py.on_key_down(wrap_py.K_SPACE)
def fly():
    global speed
    speed=-22

@wrap_py.always(50)
def fall():
    global speed
    wrap_py.sprite.move_sprite_by(player,0,speed)
    speed+=1