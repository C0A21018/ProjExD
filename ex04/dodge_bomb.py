import pygame as pg
import sys
import random

def main():
    #練習１
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))  #Surface
    screen_rct = screen_sfc.get_rect()  #rect
    bgimg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")  #Surface
    bgimg_rct = bgimg_sfc.get_rect()  #rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    #練習３
    kkimg_sfc = pg.image.load("ex04/fig/6.png")  #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  #Surface
    kkimg_rct = kkimg_sfc.get_rect()  #rect
    kkimg_rct.center = 900, 400
    #練習５
    bmimg_sfc = pg.Surface((20, 20))  #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect()  #rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1
     
    #新しい爆弾の追加
    i=0
    bmimg1_sfc=pg.Surface((20,20)) #Surface
    bmimg1_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg1_sfc,(0,0,255),(10,10),10)
    bmimg1_rct=bmimg1_sfc.get_rect() #rect
    bmimg1_rct.centerx=random.randint(0,screen_rct.width)
    bmimg1_rct.centery=random.randint(0,screen_rct.height)
    wx, wy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        #練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #練習4,7
        key_states = pg.key.get_pressed()  #辞書
        #if key_states[pg.K_c]:
            #kkimg_sfc = pg.image.load("fig/11.png")
            #kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 0.2)
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        if check_bound(kkimg_rct, screen_rct) != (1,1):
            if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        #練習６
        bmimg_rct.move_ip(vx, vy)
        bmimg_rct.move_ip(wx, wy)
        #練習５
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        if key_states[pg.K_2]==True: i=1
        if i==1: screen_sfc.blit(bmimg1_sfc,bmimg1_rct)
        #練習７
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        if yoko == -1:
            vx *= -1.2
        if tate == -1:
            vy *= -1.2
        yoko, tate=check_bound(bmimg1_rct,screen_rct)
        wx*=yoko
        wy*=tate
        #練習８
        if kkimg_rct.colliderect(bmimg_rct): return
        
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1  #領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : 
        yoko = -1  #領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: 
        tate = -1  #領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()   #メイン部分
    pg.quit()
    sys.exit()

