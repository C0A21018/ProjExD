import pygame as pg
import sys
import random

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(image)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()     # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        
        if check_bound(self.rct, scr.rct) != (1, 1):  #領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)

class Bomb():
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

img_weapon = pg.image.load("bullet.png")
pg_y = 0
px = 320
py = 240
bx = 0
by = 0
space = 0
BULLET_MAX = 100
bull_n = 0
bull_x =[0] * BULLET_MAX
bull_y =[0] * BULLET_MAX
bull_f =[False] * BULLET_MAX


class Shooting():
    def set_bullet():
        global bull_n
        bull_f[bull_n] = True
        bull_x[bull_n] = px-16
        bull_y[bull_n] = py-32
        bull_n = (bull_n+1)%BULLET_MAX
    
    def move_bullet(screen):
        for i in range(BULLET_MAX):
            if bull_f[i] == True:
                bull_y[i] = bull_y[i] - 32
                screen.bullet(img_weapon, [bull_x[i], bull_y[i]])
                if bull_y[i] < 0:
                    bull_f[i] = False


def main():
    clock = pg.time.Clock()

    scr = Screen("逃げろ！こうかとん", (1600, 900), "ex04/fig/pg_bg.jpg")

    kkt = Bird("ex04/fig/6.png", 2.0, (900, 400))

    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)         #爆弾
    bkd_2 = Bomb((160, 32, 255), 30, (+1, +1), scr)    #爆弾の追加(紫)
    bkd_3 = Bomb((255, 96, 208), 20, (+1, +1), scr)    #爆弾の追加(ピンク)

    sho = Shooting()

    while True:
        scr.blit()
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        kkt.update(scr)

        bkd.update(scr)
        bkd_2.update(scr)
        bkd_3.update(scr)

        if kkt.rct.colliderect(bkd.rct):
            return
        if kkt.rct.colliderect(bkd_2.rct):
            return
        if kkt.rct.colliderect(bkd_3.rct):
            return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1       # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1       # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()