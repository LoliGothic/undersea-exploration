import pygame

# pointPlayer1とかはplayerそれぞれのポイント
def result(pointPlayer1, pointPlayer2, pointPlayer3, pointPlayer4):
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

      # 出力する文字、文字の色を指定
      text = font.render("player1", True, (255,255,255))
      text2 = font.render("player2", True, (255,255,255))
      text3 = font.render("player3", True, (255,255,255))
      text4 = font.render("player4", True, (255,255,255))
      score = font.render(str(pointPlayer1), True, (255,255,255))
      score2 = font.render(str(pointPlayer2), True, (255,255,255))
      score3 = font.render(str(pointPlayer3), True, (255,255,255))
      score4 = font.render(str(pointPlayer4), True, (255,255,255))

      # 文字の出力、座標
      screen.blit(text, (40, 40))
      screen.blit(text2, (40, 100))
      screen.blit(text3, (40, 160))
      screen.blit(text4, (40, 220))
      screen.blit(score, (200, 40))
      screen.blit(score2, (200, 100))
      screen.blit(score3, (200, 160))
      screen.blit(score4, (200, 220))

      # 画面を再描画
      pygame.display.update()
#resultの実行
# result(100, 120, 60, 40)