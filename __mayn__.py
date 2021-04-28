import wrap

wrap.add_sprite_dir("C:/Users/nnata/wrap_py_catalog")
speed = 1

wrap.world.create_world(1930, 1010)


pipe = wrap.sprite.add("flappy_bird",700,500,"pipe")
wrap.sprite.set_size(pipe, 85, 370)
wrap.sprite.move_bottom_to(pipe,1010)



# игрок
player = wrap.sprite.add("flappy_bird", 500, 500)
wrap.sprite.set_size(player, 85, 70)


# управление
@wrap.on_key_down(wrap.K_SPACE)
def fly():
    global speed
    speed = -22


@wrap.always(30)
def fall():
    global speed
    wrap.sprite.move(player, 0, speed)
    speed += 0.5
