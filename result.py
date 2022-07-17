import pygame

# pointPlayer1とかはplayerそれぞれのポイント
def result(pointPlayer1, pointPlayer2, pointPlayer3, pointPayer4):
  pygame.init()

  # 画面サイズ
  screen = pygame.display.set_mode((400, 400))

  running = True
  while running:
    for event in pygame.event.get():

      # ウィンドウの☓ボタンが押されたら終わる
      if event.type == pygame.QUIT:
        running = False

      # 画面を真っ黒にする 
      screen.fill((0,0,0))

      # 文字の大きさを指定
      font = pygame.font.Font(None, 45)

      # 文字の色を指定
      text = font.render("hello", True, (255,255,255))

      # 文字の座標
      screen.blit((text, [40, 40]))

      # 画面を再描画
      pygame.display.update()
