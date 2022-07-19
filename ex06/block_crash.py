from ctypes import c_size_t
import pygame
from pygame.locals import *
import math
import sys
import pygame.mixer
SCREEN = Rect(0, 0, 600, 600)

# パドルのクラス
class Paddle(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20          # パドルのy座標
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]  # マウスのx座標をパドルのx座標に
        self.rect.clamp_ip(SCREEN)                     # ゲーム画面内のみで移動

# ボールのクラス
class Ball(pygame.sprite.Sprite):
    speed = 5
    angle_left = 135
    angle_right = 45

    def __init__(self, filename, paddle, blocks):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.dx = self.dy = 0  # ボールの速度
        self.paddle = paddle  # パドルへの参照
        self.blocks = blocks  # ブロックグループへの参照
        self.update = self.start
        self.hit = 0  # 連続でブロックを壊した回数

    def start(self):
        # ボールの初期位置(パドルの上)
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top
        # 左クリックでボール射出
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy = -self.speed
            self.update = self.move

    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        # 壁との反射
        if self.rect.left < SCREEN.left:    # 左側
            self.rect.left = SCREEN.left
            self.dx = -self.dx              # 速度を反転
        if self.rect.right > SCREEN.right:  # 右側
            self.rect.right = SCREEN.right
            self.dx = -self.dx
        if self.rect.top < SCREEN.top:      # 上側
            self.rect.top = SCREEN.top
            self.dy = -self.dy
        # パドルとの反射(左端:135度方向, 右端:45度方向, それ以外:線形補間)
        if self.rect.colliderect(self.paddle.rect) and self.dy > 0:
            self.hit = 0                                # 連続ヒットを0に戻す
            (x1, y1) = (self.paddle.rect.left - self.rect.width, self.angle_left)
            (x2, y2) = (self.paddle.rect.right, self.angle_right)
            x = self.rect.left                          # ボールが当たった位置
            y = (float(y2-y1)/(x2-x1)) * (x - x1) + y1  # 線形補間
            angle = math.radians(y)                     # 反射角度
            self.dx = self.speed * math.cos(angle)
            self.dy = -self.speed * math.sin(angle)
        # ボールを落とした場合
        #if self.rect.top > SCREEN.bottom:
            #self.update = self.start                    # ボールを初期状態に
            #self.hit = 0
        if self.rect.top > SCREEN.bottom:
 
            ### GAME OVERを表示
            font = pygame.font.Font(None, c_size_t)
            text = font.render("GAME OVER", True, (255,31,31))
            pygame.Surface.blit(text, [73,299])

        # ボールと衝突したブロックリストを取得
        blocks_collided = pygame.sprite.spritecollide(self, self.blocks, True)
        if blocks_collided:  # 衝突ブロックがある場合
            oldrect = self.rect
            for block in blocks_collided:
                # ボールが左から衝突
                if oldrect.left < block.rect.left < oldrect.right < block.rect.right:
                    self.rect.right = block.rect.left
                    self.dx = -self.dx
                # ボールが右から衝突
                if block.rect.left < oldrect.left < block.rect.right < oldrect.right:
                    self.rect.left = block.rect.right
                    self.dx = -self.dx
                # ボールが上から衝突
                if oldrect.top < block.rect.top < oldrect.bottom < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.dy = -self.dy
                # ボールが下から衝突
                if block.rect.top < oldrect.top < block.rect.bottom < oldrect.bottom:
                    self.rect.top = block.rect.bottom
                    self.dy = -self.dy
                self.hit += 1               # 衝突回数

# ブロックのクラス
class Block(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    group = pygame.sprite.RenderUpdates()  # 描画用のスプライトグループ
    blocks = pygame.sprite.Group()       # 衝突判定用のスプライトグループ
    Paddle.containers = group
    Ball.containers = group
    Block.containers = group, blocks
    paddle = Paddle("ex06/paddle.png")           # パドルの作成
    # ブロックの作成(14*10)
    for x in range(1, 22):
        for y in range(1, 15):
            Block("ex06/block.png", x, y)

    Ball("ex06/ball.png", paddle, blocks) # ボールを作成
    clock = pygame.time.Clock()

    while (1):
        clock.tick(60)      # フレームレート(60fps)
        screen.fill((0,20,0))
        group.update()        # 全てのスプライトグループを更新
        group.draw(screen)    # 全てのスプライトグループを描画
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()