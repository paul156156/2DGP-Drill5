from pico2d import *

open_canvas()
back_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global walking, dir_x, dir_y
    global x, y, direction

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            walking = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dir_y += 1
                direction = 3
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                direction = 0
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                direction = 2
            elif event.key == SDLK_RIGHT:
                dir_x += 1
                direction = 1
            elif event.key == SDLK_ESCAPE:
                walking = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1

walking = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0
direction = 0 # 0 하 1 우 2 좌 3 위

while walking:
    clear_canvas()
    back_ground.draw(800 // 2, 600 // 2, 800, 600)
    character.clip_draw(frame * 50, (3 - direction) * 65, 50, 65, x, y)
    update_canvas()
    handle_events()

    # if dir_x != 0 or dir_y != 0:  idle 애니메이션
    frame = (frame + 1) % 4

    x += dir_x * 7
    y += dir_y * 7

    # 경계
    if x < 0:
        x = 0
    elif x > 800:
        x = 800

    if y < 0:
        y = 0
    elif y > 600:
        y = 600

    delay(0.05)

close_canvas()