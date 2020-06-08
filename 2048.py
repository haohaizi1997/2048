import pygame
import random


# 颜色常量
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = 0, 0, 255
GRAY = 102, 102, 102


class Game2048():
    def __init__(self):
        pygame.init()
        self.gameWindowSize = (500, 500)
        self.score = 0
        self.highscore = 0
        self.weight = 4
        self.height = 4
        self.win_score = 2048
        self.reset()


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.gameList = [[0 for i in range(self.weight)] for j in range(self.height)]
        self.drawRandNum(self.gameList)
        self.drawRandNum(self.gameList)

        self.MYWINDOWS = pygame.display.set_mode(self.gameWindowSize)
        pygame.display.set_caption("2048")
        pygame.draw.rect(self.MYWINDOWS, (187, 173, 160), (0, 0, 500, 500))
        self.drawBlock()
        self.draw_num(self.gameList)


    def drawRandNum(self, gameList):
        (i, j) = random.choice([(i, j) for i in  range(self.weight) for j in range(self.height) if gameList[i][j] == 0])
        gameList[i][j] = 4 if random.randrange(100) > 89 else 2

    def draw_text(self, text, numList):
        font = pygame.font.SysFont('comicsans', 60, bold=False)
        label = font.render(text, 1, WHITE)
        self.MYWINDOWS.blit(label, (70 + numList[0] * 120 - label.get_width()/2, 70 + numList[1] * 120 - label.get_height()/2))

    def draw_tip(self, text):
        font = pygame.font.SysFont('SimHei', 36, bold=False)
        label = font.render(text, 1, WHITE)
        self.MYWINDOWS.blit(label, (self.gameWindowSize[0] / 2 - label.get_width() / 2, self.gameWindowSize[1] / 2 - label.get_height() / 2))

    def drawBlock(self):
        for j in range(0, self.height):
            for i in range(0, self.weight):
                pygame.draw.rect(self.MYWINDOWS, (205, 193, 180),
                                 (20 + i*120, 20 + j * 120,
                                  100, 100))

    def draw_num(self, gameList):
        for i in range(4):
            for j in range(4):
                if gameList[i][j] != 0:
                    self.draw_text(str(gameList[i][j]), [j, i])


    def merge_left_num(self, gameList):
        newGameList = [[], [], [], []]
        for i in range(4):
            line = gameList[i]
            newGameList[i] = [j for j in line if j != 0]
            newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

        isChanged = False
        for i in range(4):
            if self.gameList[i] != newGameList[i]:
                self.gameList = newGameList
                isChanged = True

        isPair = False
        for i in range(4):
            line = self.gameList[i]
            for j in range(3):
                if line[j] == line[j + 1] and line[j] != 0:
                    self.score += 2 * line[j]
                    line[j] = 2 * line[j]
                    line[j + 1] = 0
                    isPair = True

        if isPair:
            for i in range(4):
                line = self.gameList[i]
                newGameList[i] = [j for j in line if j != 0]
                newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

        if isChanged or isPair:
            self.drawBlock()
            self.draw_num(self.gameList)
            self.drawRandNum(self.gameList)
            self.draw_num(self.gameList)


    def merge_num(self, gameList, whereStr):
        if whereStr == 'left':
            newGameList = [[],[],[],[]]
            for i in range(4):
                line = gameList[i]
                newGameList[i] = [j for j in line if j != 0]
                newGameList[i] += [0 for k in range(len(line)-len(newGameList[i]))]

            isChanged = False
            for i in range(4):
                if self.gameList[i] != newGameList[i]:
                    self.gameList = newGameList
                    isChanged = True

            isPair = False
            for i in range(4):
                line = self.gameList[i]
                for j in range(3):
                    if line[j] == line[j+1] and line[j] != 0:
                        self.score += 2 * line[j]
                        line[j] = 2 * line[j]
                        line[j+1] = 0
                        isPair = True

            if isPair:
                for i in range(4):
                    line = self.gameList[i]
                    newGameList[i] = [j for j in line if j != 0]
                    newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            self.gameList = newGameList

            if isChanged or isPair:
                self.drawBlock()
                self.draw_num(self.gameList)
                self.drawRandNum(self.gameList)
                self.draw_num(self.gameList)

        if whereStr == 'right':
            for i in range(4):
                gameList[i].reverse()

            newGameList = [[], [], [], []]
            for i in range(4):
                line = gameList[i]
                newGameList[i] = [j for j in line if j != 0]
                newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            isChanged = False
            for i in range(4):
                if gameList[i] != newGameList[i]:
                    gameList = newGameList
                    isChanged = True

            isPair = False
            for i in range(4):
                line = gameList[i]
                for j in range(3):
                    if line[j] == line[j + 1] and line[j] != 0:
                        self.score += 2 * line[j]
                        line[j] = 2 * line[j]
                        line[j + 1] = 0
                        isPair = True

            if isPair:
                for i in range(4):
                    line = gameList[i]
                    newGameList[i] = [j for j in line if j != 0]
                    newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            gameList = newGameList

            for i in range(4):
                gameList[i].reverse()

            self.gameList = gameList
            if isChanged or isPair:
                self.drawBlock()
                self.draw_num(self.gameList)
                self.drawRandNum(self.gameList)
                self.draw_num(self.gameList)

        if whereStr == 'up':
            leftGameList = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    leftGameList[j][i] = gameList[i][j]
            gameList = leftGameList

            newGameList = [[], [], [], []]
            for i in range(4):
                line = gameList[i]
                newGameList[i] = [j for j in line if j != 0]
                newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            isChanged = False
            for i in range(4):
                if gameList[i] != newGameList[i]:
                    gameList = newGameList
                    isChanged = True

            isPair = False
            for i in range(4):
                line = gameList[i]
                for j in range(3):
                    if line[j] == line[j + 1] and line[j] != 0:
                        self.score += 2 * line[j]
                        line[j] = 2 * line[j]
                        line[j + 1] = 0
                        isPair = True

            if isPair:
                for i in range(4):
                    line = gameList[i]
                    newGameList[i] = [j for j in line if j != 0]
                    newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            gameList = newGameList

            upGameList = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    upGameList[i][j] = gameList[j][i]

            self.gameList = upGameList

            if isChanged or isPair:
                self.drawBlock()
                self.draw_num(self.gameList)
                self.drawRandNum(self.gameList)
                self.draw_num(self.gameList)

        if whereStr == 'down':
            leftGameList = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    leftGameList[j][i] = gameList[i][j]
            gameList = leftGameList

            for i in range(4):
                gameList[i].reverse()

            newGameList = [[], [], [], []]
            for i in range(4):
                line = gameList[i]
                newGameList[i] = [j for j in line if j != 0]
                newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            isChanged = False
            for i in range(4):
                if gameList[i] != newGameList[i]:
                    gameList = newGameList
                    isChanged = True

            isPair = False
            for i in range(4):
                line = gameList[i]
                for j in range(3):
                    if line[j] == line[j + 1] and line[j] != 0:
                        self.score += 2 * line[j]
                        line[j] = 2 * line[j]
                        line[j + 1] = 0
                        isPair = True

            if isPair:
                for i in range(4):
                    line = gameList[i]
                    newGameList[i] = [j for j in line if j != 0]
                    newGameList[i] += [0 for k in range(len(line) - len(newGameList[i]))]

            gameList = newGameList

            for i in range(4):
                gameList[i].reverse()

            upGameList = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    upGameList[i][j] = gameList[j][i]

            self.gameList = upGameList

            if isChanged or isPair:
                self.drawBlock()
                self.draw_num(self.gameList)
                self.drawRandNum(self.gameList)
                self.draw_num(self.gameList)

    def isWin(self):
        return any(any(i >= self.win_score for i in line) for line in self.gameList)

    def isGameover(self):
        isfull = True
        for i in range(4):
            for j in range(4):
                if self.gameList[i][j] == 0:
                    isfull = False

        if isfull:
            is_gameover = True
            for i in range(4):
                for j in range(3):
                    if self.gameList[i][j] == self.gameList[i][j+1] and self.gameList[i][j] != 0:
                        is_gameover = False

            leftGameList = [[0 for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    leftGameList[j][i] = self.gameList[i][j]
            for i in range(4):
                for j in range(3):
                    if leftGameList[i][j] == leftGameList[i][j+1] and leftGameList[i][j] != 0:
                        is_gameover = False

            return is_gameover


if __name__ == '__main__':
    game2048 = Game2048()
    while True:
        pygame.time.Clock().tick(30)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game2048.merge_num(game2048.gameList, 'left')
                if event.key == pygame.K_RIGHT:
                    game2048.merge_num(game2048.gameList, 'right')
                if event.key == pygame.K_UP:
                    game2048.merge_num(game2048.gameList, 'up')
                if event.key == pygame.K_DOWN:
                    game2048.merge_num(game2048.gameList, 'down')
                if event.key == pygame.K_r:
                    game2048.reset()
                if game2048.isWin():
                    game2048.draw_tip('你赢了！！！')
                if game2048.isGameover():
                    game2048.draw_tip('你输了！！！')
        title = '2048---当前分数:' + str(game2048.score)
        pygame.display.set_caption(title)






