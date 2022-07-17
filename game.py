from email.policy import default
import sys
import pygame
import keyboard
import time
import random

class Map:
  # マップ
  mapData = [
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "s", "p1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "f2", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "f2", "w", "w", "w", "w"],
    ["w", "w", "w", "f3", "f3", "f2", "f2", "f2", "f2", "f2", "f2", "w", "w", "w", "w"],
    ["w", "w", "w", "f3", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "f3", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "f3", "f3", "f3", "f3", "f4", "f4", "f4", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "f4", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "f4", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "f4", "f4", "f4", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]
  ]

  # 画像を読み込んでサイズを縮小
  imgBigWater = pygame.image.load("./img/water.png")
  imgWater = pygame.transform.scale(imgBigWater, (30, 31))
  imgGigRoad = pygame.image.load("./img/road.png")
  imgRoad = pygame.transform.scale(imgGigRoad, (30, 30))
  imgBigPlayer1 = pygame.image.load("./img/player1.png")
  imgPlayer1 = pygame.transform.scale(imgBigPlayer1, (30, 31))
  imgBigFood1 = pygame.image.load("./img/f1.png")
  imgFood1 = pygame.transform.scale(imgBigFood1, (30, 31))
  imgBigFood2 = pygame.image.load("./img/f2.png")
  imgFood2 = pygame.transform.scale(imgBigFood2, (30, 31))
  imgBigFood3 = pygame.image.load("./img/f3.png")
  imgFood3 = pygame.transform.scale(imgBigFood3, (30, 31))
  imgBigFood4 = pygame.image.load("./img/f4.png")
  imgFood4 = pygame.transform.scale(imgBigFood4, (30, 31))
  imgBigSubMarine = pygame.image.load("./img/submarine.png")
  imgSubMarine = pygame.transform.scale(imgBigSubMarine, (30, 31))

  # タイル画像とマップ文字を対応
  mapImg = {
  "w": imgWater,
  "r": imgRoad,
  "p1": imgPlayer1,
  "f1": imgFood1,
  "f2": imgFood2,
  "f3": imgFood3,
  "f4": imgFood4,
  "s": imgSubMarine
  }

  def __init__(self, HEIGHT, WIDTH, tileSize, screen):
    self.height = HEIGHT
    self.width = WIDTH
    self.tileSize = tileSize
    self.screen = screen

  # マップを描画
  def draw(self, string, positionX, positionY):

    self.drawString(string, positionX, positionY)

    maxWidth = self.height // self.tileSize
    maxHeight = self.width // self.tileSize

    for i in range(maxWidth):
     for j in range(maxHeight):

      # タイル画像に対応するマップ文字を取得
      number = self.mapData[j][i]  

      # タイル画像のファイル名を取得
      img = self.mapImg[number] 

      # タイル画像を画面に描画
      self.screen.blit(img, (i * self.tileSize, j * self.tileSize + 90))
    pygame.display.update()
  
  def drawString(self, string, positionX, positionY):
    self.screen.fill((0,0,0))
    font = pygame.font.Font(None, 45)
    text = font.render(string, True, (255,255,255))
    self.screen.blit(text, [positionX, positionY])
    
class Actor:
  food = 0
  foodPoint = 0
  formerImg = "f1"

  def __init__(self, map, x, y):
    self.map = map
    self.x = x
    self.y = y

  def keyMove(self):
    time.sleep(0.5)
    e = keyboard.read_key()
    if e == "backspace":
      sys.exit()

    if e == "up":
      if self.map.mapData[self.y - 1][self.x] == "w":
        self.map.mapData[self.y][self.x] = "p1"
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y - 1][self.x]
        self.y -= 1
        self.map.mapData[self.y][self.x] = "p1"

    elif e == "down":
      if self.map.mapData[self.y + 1][self.x] == "w":
        self.map.mapData[self.y][self.x] = "p1"
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y + 1][self.x]
        self.y += 1
        self.map.mapData[self.y][self.x] = "p1"

    elif e == "left":
      if self.map.mapData[self.y][self.x - 1] == "w":
        self.map.mapData[self.y][self.x] = "p1"
      elif self.map.mapData[self.y][self.x - 1] == "s":
        sys.exit()
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y][self.x - 1]
        self.x -= 1
        self.map.mapData[self.y][self.x] = "p1"

    elif e == "right":
      if self.map.mapData[self.y][self.x + 1] == "w":
        self.map.mapData[self.y][self.x] = "p1"
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y][self.x + 1]
        self.x += 1
        self.map.mapData[self.y][self.x] = "p1"

  def getFood(self):
    time.sleep(0.5)
    e = keyboard.read_key()
    if e == "backspace":
      sys.exit()
      
    if e == "y":
      if self.formerImg == "f1" or self.formerImg == "f2" or self.formerImg == "f3" or self.formerImg == "f4":
        self.food += 1
        self.formerImg = "r"



class Game:
  #pyfameの初期化
  pygame.init()

  # 画面サイズ
  HEIGHT = 450
  WIDTH = 450
  oxygen = 30
  screen = pygame.display.set_mode((HEIGHT, WIDTH))

  #画面タイトル設定
  pygame.display.set_caption("sugoroku game")

  map = Map(HEIGHT, WIDTH, 30, screen)
  player1 = Actor(map, 2, 1)
  
  def game(self):
    if(self.oxygen - self.player1.food <= 0):
      sys.exit()
    else:
      self.oxygen -= (1 + self.player1.food)
      
    dice = random.randint(3, 8) - self.player1.food
    self.map.draw("Dice:" + str(dice) + "   food:" + str(self.player1.food) + "   oxygen:" + str(self.oxygen), 20, 20)

    for i in range(dice, 0, -1):
      self.player1.keyMove()
      dice = i - 1
      self.map.draw("Dice:" + str(dice) + "   food:" + str(self.player1.food) + "   oxygen:" + str(self.oxygen), 20, 20)

    self.map.draw("eat?[y/n]" + "   food:" + str(self.player1.food) + "   oxygen:" + str(self.oxygen), 20, 20)

    self.player1.getFood()

def main():
  # オブジェクトの作成
  game = Game()

  while True:
    game.game()

if __name__ == "__main__":
  main()
