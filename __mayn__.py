import wrap,os

wrap.add_sprite_dir("C:/Users/nnata/wrap_py_catalog")
speed = 1

# окно
wrap.world.create_world(1930, 1010)
shon = wrap.sprite.add("backgrounds", 965, 505)
wrap.sprite.set_size(shon, 1929, 1009)

# трубы
pipe = wrap.sprite.add("flappy_bird", 700, 500, "pipe")
wrap.sprite.set_size(pipe, 85, 370)
wrap.sprite.move_bottom_to(pipe, 802)
pipe2 = wrap.sprite.add("flappy_bird", 700, 500, "pipe")
wrap.sprite.set_reverse_y(pipe2,True)
wrap.sprite.set_size(pipe2, 85, 370)
wrap.sprite.move_top_to(pipe2,0)













# игрок
player = wrap.sprite.add("flappy_bird", 500, 500, "кот")
wrap.sprite.set_height_proportionally(player, 100)


# управление
@wrap.on_key_down(wrap.K_SPACE)
def fly():
    global speed
    speed = -25


# падение
@wrap.always(30)
def fall():
    global speed
    wrap.sprite.move(player, 0, speed)
    speed+=1
    if wrap.sprite.get_bottom(player) >= 800:
        os._exit(6)



@wrap.always(30)
def dvishenie():
    if wrap.sprite.is_collide_sprite(pipe,player):
        os._exit(0)
    if wrap.sprite.is_collide_sprite(pipe2,player):
        os._exit(0)
    wrap.sprite.move(pipe,-3,0)
    wrap.sprite.move(pipe2, -3, 0)




























