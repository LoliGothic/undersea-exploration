import sys
import pygame
import keyboard
import time
import random
import result

class Map:
  # マップ
  mapData = [
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "s", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w", "w", "w", "w"],
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
  imgBigPlayer2 = pygame.image.load("./img/player2.png")
  imgPlayer2 = pygame.transform.scale(imgBigPlayer2, (30, 31))
  imgBigPlayer3 = pygame.image.load("./img/player3.png")
  imgPlayer3 = pygame.transform.scale(imgBigPlayer3, (30, 31))
  imgBigPlayer4 = pygame.image.load("./img/player4.png")
  imgPlayer4 = pygame.transform.scale(imgBigPlayer4, (30, 31))
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
  "p2": imgPlayer2,
  "p3": imgPlayer3,
  "p4": imgPlayer4,
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
  def draw(self, gameInfo, playerInfo, positionText1X, positionText1Y, positionText2X, positionText2Y):

    self.drawString(gameInfo, playerInfo, positionText1X, positionText1Y, positionText2X, positionText2Y)

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
  
  def drawString(self, gameInfo, playerInfo, positionText1X, positionText1Y, positionText2X, positionText2Y):
    self.screen.fill((0,0,0))
    font = pygame.font.Font(None, 30)
    text1 = font.render(gameInfo, True, (255,255,255))
    text2 = font.render(playerInfo, True, (255,255,255))
    self.screen.blit(text1, [positionText1X, positionText1Y])
    self.screen.blit(text2, [positionText2X, positionText2Y])
    
class Actor:
  food = 0
  foodPoint = 0
  foodInfo = []
  formerImg = "s"
  goal = False

  def __init__(self, map, x, y, pNumber, playerName):
    self.map = map
    self.x = x
    self.y = y
    self.pNumber = pNumber
    self.playerName = playerName

  def keyMove(self):
    time.sleep(0.3)
    e = keyboard.read_key()
    if e == "backspace":
      sys.exit()

    if e == "up":
      flag = False
      if self.map.mapData[self.y - 1][self.x] == "p1" or self.map.mapData[self.y - 1][self.x] == "p2" or self.map.mapData[self.y - 1][self.x] == "p3" or self.map.mapData[self.y - 1][self.x] == "p4":
        # 上に別プレイヤーがいる時
        for i in range(1, 10):
          if self.map.mapData[self.y - i][self.x] == "w":
            saveX = self.x
            saveY = self.y
            self.y = self.y - i + 1
            self.x = self.x
            break
          elif self.map.mapData[self.y - i][self.x] == "f1" or self.map.mapData[self.y - i][self.x] == "f2" or self.map.mapData[self.y - i][self.x] == "f3" or self.map.mapData[self.y - i][self.x] == "f4" or self.map.mapData[self.y - i][self.x] == "r":
            self.map.mapData[self.y][self.x] = self.formerImg
            self.formerImg = self.map.mapData[self.y - i][self.x]
            self.y -= i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 左に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            break
          if self.map.mapData[self.y][self.x - i] == "w":
            self.y = self.y
            self.x = self.x - i + 1
            break
          elif self.map.mapData[self.y][self.x - i] == "f1" or self.map.mapData[self.y][self.x - i] == "f2" or self.map.mapData[self.y][self.x - i] == "f3" or self.map.mapData[self.y][self.x - i] == "f4" or self.map.mapData[self.y][self.x - i] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y][self.x - i]
            self.x -= i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 右に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            break
          if self.map.mapData[self.y][self.x + i] == "w":
            self.y = self.y
            self.x = self.x + i - 1
            break
          elif self.map.mapData[self.y][self.x + i] == "f1" or self.map.mapData[self.y][self.x + i] == "f2" or self.map.mapData[self.y][self.x + i] == "f3" or self.map.mapData[self.y][self.x + i] == "f4" or self.map.mapData[self.y][self.x + i] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y][self.x + i]
            self.x += i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
      elif self.map.mapData[self.y - 1][self.x] == "w":
        self.map.mapData[self.y][self.x] = self.pNumber
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y - 1][self.x]
        self.y -= 1
        self.map.mapData[self.y][self.x] = self.pNumber

    elif e == "down":
      flag = False
      if self.map.mapData[self.y + 1][self.x] == "p1" or self.map.mapData[self.y + 1][self.x] == "p2" or self.map.mapData[self.y + 1][self.x] == "p3" or self.map.mapData[self.y + 1][self.x] == "p4":
        # 下に別のプレイヤーがいる時
        for i in range(1, 10):
          if self.map.mapData[self.y + i][self.x] == "w":
            saveX = self.x
            saveY = self.y
            self.y = self.y + i - 1
            self.x = self.x
            break
          elif self.map.mapData[self.y + i][self.x] == "f1" or self.map.mapData[self.y + i][self.x] == "f2" or self.map.mapData[self.y + i][self.x] == "f3" or self.map.mapData[self.y + i][self.x] == "f4" or self.map.mapData[self.y + i][self.x] == "r":
            self.map.mapData[self.y][self.x] = self.formerImg
            self.formerImg = self.map.mapData[self.y + i][self.x]
            self.y += i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 左に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            break
          if self.map.mapData[self.y][self.x - i] == "w":
            self.y = self.y
            self.x = self.x - i + 1 
            break
          elif self.map.mapData[self.y][self.x - i] == "f1" or self.map.mapData[self.y][self.x - i] == "f2" or self.map.mapData[self.y][self.x - i] == "f3" or self.map.mapData[self.y][self.x - i] == "f4" or self.map.mapData[self.y][self.x - i] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y][self.x - i]
            self.x -= i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 右に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            break
          elif self.map.mapData[self.y][self.x + i] == "w":
            self.y = self.y
            self.x = self.x + i - 1
            break
          elif self.map.mapData[self.y][self.x + i] == "f1" or self.map.mapData[self.y][self.x + i] == "f2" or self.map.mapData[self.y][self.x + i] == "f3" or self.map.mapData[self.y][self.x + i] == "f4" or self.map.mapData[self.y][self.x + i] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y][self.x + i]
            self.x += i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
      elif self.map.mapData[self.y + 1][self.x] == "w":
        self.map.mapData[self.y][self.x] = self.pNumber
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y + 1][self.x]
        self.y += 1
        self.map.mapData[self.y][self.x] = self.pNumber

    elif e == "left":
      flag = False
      if self.map.mapData[self.y][self.x - 1] == "p1" or self.map.mapData[self.y][self.x - 1] == "p2" or self.map.mapData[self.y][self.x - 1] == "p3" or self.map.mapData[self.y][self.x - 1] == "p4":
        # 左に別プレイヤーがいる時
        for i in range(1, 10):
          if self.map.mapData[self.y][self.x - i] == "w":
            saveX = self.x
            saveY = self.y
            self.y = self.y
            self.x = self.x - i + 1
            break
          elif self.map.mapData[self.y][self.x - i] == "f1" or self.map.mapData[self.y][self.x - i] == "f2" or self.map.mapData[self.y][self.x - i] == "f3" or self.map.mapData[self.y][self.x - i] == "f4" or self.map.mapData[self.y][self.x - i] == "r":
            self.map.mapData[self.y][self.x] = self.formerImg
            self.formerImg = self.map.mapData[self.y][self.x - i]
            self.x -= i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
          elif self.map.mapData[self.y][self.x - i] == "s":
            self.map.mapData[self.y][self.x] = self.formerImg
            self.goal = True
            break

        # 上に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            print("aaa")
            break
          elif self.map.mapData[self.y - i][self.x] == "w":
            self.y = self.y - i + 1
            self.x = self.x
            break
          elif self.map.mapData[self.y - i][self.x] == "f1" or self.map.mapData[self.y - i][self.x] == "f2" or self.map.mapData[self.y - i][self.x] == "f3" or self.map.mapData[self.y - i][self.x] == "f4" or self.map.mapData[self.y - i][self.x] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y - i][self.x]
            self.y -= i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 下に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            break
          elif self.map.mapData[self.y + i][self.x] == "w":
            self.y = self.y + i - 1
            self.x = self.x
            break
          elif self.map.mapData[self.y + i][self.x] == "f1" or self.map.mapData[self.y + i][self.x] == "f2" or self.map.mapData[self.y + i][self.x] == "f3" or self.map.mapData[self.y + i][self.x] == "f4" or self.map.mapData[self.y + i][self.x] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y + i][self.x]
            self.y += i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
      elif self.map.mapData[self.y][self.x - 1] == "w":
        self.map.mapData[self.y][self.x] = self.pNumber
      elif self.map.mapData[self.y][self.x - 1] == "s":
        self.map.mapData[self.y][self.x] = self.formerImg
        self.goal = True
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y][self.x - 1]
        self.x -= 1
        self.map.mapData[self.y][self.x] = self.pNumber

    elif e == "right":
      flag = False
      if self.map.mapData[self.y][self.x + 1] == "p1" or self.map.mapData[self.y][self.x + 1] == "p2" or self.map.mapData[self.y][self.x + 1] == "p3" or self.map.mapData[self.y][self.x + 1] == "p4":
        # 右に別プレイヤーがいる時
        for i in range(1, 10):
          if self.map.mapData[self.y][self.x + i] == "w":
            saveX = self.x
            saveY = self.y
            self.y = self.y
            self.x = self.x + i - 1
            break
          elif self.map.mapData[self.y][self.x + i] == "f1" or self.map.mapData[self.y][self.x + i] == "f2" or self.map.mapData[self.y][self.x + i] == "f3" or self.map.mapData[self.y][self.x + i] == "f4" or self.map.mapData[self.y][self.x + i] == "r":
            self.map.mapData[self.y][self.x] = self.formerImg
            self.formerImg = self.map.mapData[self.y][self.x + i]
            self.x += i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 上に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            print("break")
            break
          elif self.map.mapData[self.y - i][self.x] == "w":
            self.y = self.y - i + 1
            self.x = self.x
            break
          elif self.map.mapData[self.y - i][self.x] == "f1" or self.map.mapData[self.y - i][self.x] == "f2" or self.map.mapData[self.y - i][self.x] == "f3" or self.map.mapData[self.y - i][self.x] == "f4" or self.map.mapData[self.y - i][self.x] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y - i][self.x]
            self.y -= i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
        # 下に別プレイヤーがいる時
        for i in range(1, 10):
          if flag == True:
            break
          elif self.map.mapData[self.y + i][self.x] == "w":
            self.y = self.y + i - 1
            self.x = self.x
            break
          elif self.map.mapData[self.y + i][self.x] == "f1" or self.map.mapData[self.y + i][self.x] == "f2" or self.map.mapData[self.y + i][self.x] == "f3" or self.map.mapData[self.y + i][self.x] == "f4" or self.map.mapData[self.y + i][self.x] == "r":
            self.map.mapData[saveY][saveX] = self.formerImg
            self.formerImg = self.map.mapData[self.y + i][self.x]
            self.y += i
            self.map.mapData[self.y][self.x] = self.pNumber
            flag = True
            break
      elif self.map.mapData[self.y][self.x + 1] == "w":
        self.map.mapData[self.y][self.x] = self.pNumber
      else:
        self.map.mapData[self.y][self.x] = self.formerImg
        self.formerImg = self.map.mapData[self.y][self.x + 1]
        self.x += 1
        self.map.mapData[self.y][self.x] = self.pNumber

  def getFood(self):
    time.sleep(0.3)
    e = keyboard.read_key()
    if e == "backspace":
      sys.exit()

    elif e == "y":
      if self.formerImg == "r":
        if self.food > 0:
          self.foodInfo.sort()
          dumpFood = self.foodInfo[0]
          self.foodInfo.pop(0)

          if dumpFood == 1:
            if self.foodPoint - random.randint(1,4) < 0:
              self.foodPoint = 0
            else:
              self.foodPoint -= random.randint(1,4)
            self.formerImg = "f1"

          elif dumpFood == 2:
            if self.foodPoint - random.randint(7,12) < 0:
              self.foodPoint = 0
            else:
              self.foodPoint -= random.randint(7,12)
            self.formerImg = "f2"

          elif dumpFood == 3:
            if self.foodPoint - random.randint(15,20) < 0:
              self.foodPoint = 0
            else:
              self.foodPoint -= random.randint(15,20)
            self.formerImg = "f3"

          elif dumpFood == 4:
            if self.foodPoint - random.randint(23,28) < 0:
              self.foodPoint = 0
            else:
              self.foodPoint -= random.randint(23,28)
            self.formerImg = "f4"
          self.food -= 1
          
      elif self.formerImg == "f1" or self.formerImg == "f2" or self.formerImg == "f3" or self.formerImg == "f4":
        if self.formerImg == "f1":
          self.foodPoint += random.randint(1,4)
          self.foodInfo.append(1)
        elif self.formerImg == "f2":
          self.foodPoint += random.randint(7,12)
          self.foodInfo.append(2)
        elif self.formerImg == "f3":
          self.foodPoint += random.randint(15,20)
          self.foodInfo.append(3)
        elif self.formerImg == "f4":
          self.foodPoint += random.randint(23,28)
          self.foodInfo.append(4)
        self.food += 1
        self.formerImg = "r"

class Game:
  #pyfameの初期化
  pygame.init()

  # 画面サイズ
  HEIGHT = 450
  WIDTH = 450
  oxygen = 30
  goalPeople = 0
  runnning = True
  screen = pygame.display.set_mode((HEIGHT, WIDTH))

  #画面タイトル設定
  pygame.display.set_caption("sugoroku game")

  map = Map(HEIGHT, WIDTH, 30, screen)
  player1 = Actor(map, 1, 1, "p1", "player1")
  player2 = Actor(map, 1, 1, "p2", "player2")
  player3 = Actor(map, 1, 1, "p3", "player3")
  player4 = Actor(map, 1, 1, "p4", "player4")
  players = [player1, player2, player3, player4]

  def game(self):
    for player in self.players:
      if self.oxygen > 0:
        if self.oxygen - (1 + player.food) < 0:
          self.oxgen = 0
        else:
          self.oxygen -= (1 + player.food)
        dice = random.randint(3, 8) - player.food
        self.map.draw("Dice:" + str(dice) + "   oxygen:" + str(self.oxygen), str(player.playerName) + "   food:" + str(player.food), 20, 20, 20, 60)

      elif self.oxygen  <= 0:
        self.runnning = False
        break
      
      for i in range(dice, 0, -1):
        if self.goalPeople == 4:
          self.runnning = False
          break
        elif player.goal == True:
          self.goalPeople += 1
          break
        player.keyMove()
        dice = i - 1
        self.map.draw("Dice:" + str(dice) + "   oxygen:" + str(self.oxygen), str(player.playerName) + "   food:" + str(player.food), 20, 20, 20, 60)
      if player.goal == False:
        if player.formerImg == "r":
          self.map.draw("dump?[y/n]" + "   oxygen:" + str(self.oxygen), str(player.playerName) + "   food:" + str(player.food), 20, 20, 20, 60)
        else:
          self.map.draw("eat?[y/n]" + "   oxygen:" + str(self.oxygen), str(player.playerName) + "   food:" + str(player.food), 20, 20, 20, 60)
      if player.goal == False:
        player.getFood()

def main():
  playerPoint = []
  # オブジェクトの作成
  game = Game()

  while True:
    game.game()
    if game.runnning == False:
      break

  for player in game.players:
    playerPoint.append(player.foodPoint)

  result.result(playerPoint[0], playerPoint[1], playerPoint[2], playerPoint[3])

if __name__ == "__main__":
  main()
