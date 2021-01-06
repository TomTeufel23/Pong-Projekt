import sys

import pygame

pygame.init()

font = pygame.font.Font('Minecraft.ttf', 280)
breite = 1920
hoehe = 1080
size = [breite, hoehe]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

settings_pong = pygame.image.load('pong_settings.png')

click = False


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu_pong():
    while True:
        screen.fill((0, 0, 0))

        draw_text('Pong', font, (255, 255, 255), screen, breite / 2 - 280, hoehe / 5)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(breite / 2 - 125, hoehe / 2, 250, 100)
        button_2 = pygame.Rect(breite / 2 - 125, hoehe / 2 + 150, 250, 100)

        if button_1.collidepoint((mx, my)):
            if click:
                pong_game()
        if button_2.collidepoint((mx, my)):
            if click:
                options_pong()

        pygame.draw.rect(screen, (255, 255, 255), button_1)
        pygame.draw.rect(screen, (255, 255, 255), button_2)

        screen.blit(settings_pong, ((1920 - 100), (1080 / 8)))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()
        clock.tick(60)


def options_pong():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()
        clock.tick(60)


def pong_game():
    # ----------------------------------Titel----------------------------------
    pygame.display.set_caption("Pong vong Tom")

    # ----------------------------------Icon----------------------------------
    icon = pygame.image.load('ping-pong.png')

    pygame.display.set_icon(icon)

    # ----------------------------------Net----------------------------------

    pygame.draw.line(screen, (0, 0, 0), (0, 400), (800, 400))

    # ----------------------------------player 1 & 2----------------------------------
    key_up_down = False
    key_down_down = False
    key_w_down = False
    key_s_down = False

    playerX = 570
    playerY = 490

    playerX2 = 1340
    playerY2 = 490

    playerY_change = 0
    playerY2_change = 0

    # ----------------------------------Ball----------------------------------
    ball_x = 580
    ball_y = 160

    diameter = 30

    ball_move_x = 4
    ball_move_y = 4

    # ----------------------------------Scoring Numbers----------------------------------
    score_p1 = 0
    score_p2 = 0

    ta = pygame.font.Font('freesansbold.ttf', 140)

    score_x1 = 740
    score_y1 = 200

    score_x2 = 1140
    score_y2 = 200

    def show_score(x, y, x2, y2):
        score_p1d = ta.render(str(score_p1), True, (0, 0, 0))
        score_p2d = ta.render(str(score_p2), True, (0, 0, 0))
        screen.blit(score_p1d, (x, y))
        screen.blit(score_p2d, (x2, y2))

    # ----------------------------------Gameloop----------------------------------wws
    running = True
    while running:
        screen.fill((255, 255, 255))

        # ----------------------------------event damit es schließt wenn man auf x drückt----------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playerY2_change = -8
                    key_up_down = True

                if event.key == pygame.K_DOWN:
                    playerY2_change = 8
                    key_down_down = True

                if event.key == pygame.K_w:
                    playerY_change = -8
                    key_w_down = True

                if event.key == pygame.K_s:
                    playerY_change = 8
                    key_s_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_up_down = False
                    playerY2_change = 8 if key_down_down else 0

                if event.key == pygame.K_DOWN:
                    key_down_down = False
                    playerY2_change = -8 if key_up_down else 0

                if event.key == pygame.K_w:
                    key_w_down = False
                    playerY_change = 8 if key_s_down else 0

                if event.key == pygame.K_s:
                    key_s_down = False
                    playerY_change = -8 if key_w_down else 0

        # ----------------------------------screen----------------------------------
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 560, 1080))  # linkes Rechteck
        pygame.draw.rect(screen, (0, 0, 0), (1360, 0, 560, 1080))  # rechtes Rechteck
        pygame.draw.rect(screen, (0, 0, 0), (560, 940, 800, 140))  # rechteck unten
        pygame.draw.rect(screen, (0, 0, 0), (560, 0, 800, 140))  # rechteck oben
        # ----------------------------------ball----------------------------------
        pygame.draw.ellipse(screen, (0, 0, 0), [ball_x, ball_y, diameter, diameter])
        ball_y += ball_move_y
        ball_x += ball_move_x

        # ----------------------------------player + Playerbewegung----------------------------------
        pygame.draw.rect(screen, (0, 0, 0), (playerX, playerY, 10, 100))
        pygame.draw.rect(screen, (0, 0, 0), (playerX2, playerY2, 10, 100))
        playerY = playerY + playerY_change
        playerY2 = playerY2 + playerY2_change

        # ----------------------------------ballbewegeung----------------------------------

        ballRect = pygame.Rect(ball_x, ball_y, diameter, diameter)
        player1 = pygame.Rect(playerX, playerY, 10, 100)
        player2 = pygame.Rect(playerX2, playerY2, 10, 100)

       #  if ball_y < 940:
       #     ball_y += ball_move_y
       # else:
       #     ball_y -= ball_move_y

        if ball_y > 940 - diameter or ball_y < 140:
            ball_move_y = ball_move_y * -1

        if ball_x > 1360 - diameter or ball_x < 560:
            ball_move_x = ball_move_x * -1

        if ballRect.colliderect(player1) or ballRect.colliderect(player2):
            ball_move_x *= -1

        # ----------------------------------gameboarders----------------------------------

        if playerY <= 140:
            playerY = 140
        elif playerY >= 840:
            playerY = 840

        if playerY2 <= 140:
            playerY2 = 140
        elif playerY2 >= 840:
            playerY2 = 840

        # ----------------------------------scores----------------------------------

        if ball_x < 560:
            score_p1 += 1
            ball_x = 1920 / 2 - diameter / 2
            ball_y = 1080 / 2 - diameter / 2

        if ball_x > 1360 - diameter:
            score_p2 += 1
            ball_x = 1920 / 2 - diameter / 2
            ball_y = 1080 / 2 - diameter / 2

        if score_p1 > 9:
            score_p1 = 0
            score_p2 = 0

        if score_p2 > 9:
            score_p2 = 0
            score_p1 = 0

        # ----------------------------------Netz----------------------------------
        pygame.draw.line(screen, (0, 0, 0), (960, 140), (960, 940))

        # ----------------------------------Score anzeigen----------------------------------
        show_score(score_x1, score_y1, score_x2, score_y2, )

        # ----------------------------------Display aktualisierung----------------------------------
        pygame.display.flip()
        clock.tick(60)


main_menu_pong()
