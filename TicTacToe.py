from math import inf
import random as rnd
import platform
import time
from os import system

human = -1
ai = 1
coordDict = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}


class TicTacToe:

    def __init__(self,humanChoice,aiChoice):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.humanChoice = humanChoice
        self.aiChoice = aiChoice

    def GetEmptyCells(self):
        emptyCells = []
        for i,row in enumerate(self.board):
            for j,element in enumerate(row):
                if element == 0:
                    emptyCells.append([i,j])
        return emptyCells

    def Clear(self):
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    def Render(self):
        count = 0
        choise = {0:' ', -1: self.humanChoice, 1: self.aiChoice}
        for row in self.board:
            for sy in row:
                print(f'  |{choise[sy]}|',end='')
            if count < 2:
                print('\n ---------------')
                count +=1
        print('\n')

    def Winner(self, palyer):
        win = [[self.board[0][0], self.board[0][1], self.board[0][2]],
                [self.board[1][0], self.board[1][1], self.board[1][2]],
                [self.board[2][0], self.board[2][1], self.board[2][2]],
                [self.board[0][0], self.board[1][0], self.board[2][0]],
                [self.board[0][1], self.board[1][1], self.board[2][1]],
                [self.board[0][2], self.board[1][2], self.board[2][2]],
                [self.board[0][0], self.board[1][1], self.board[2][2]],
                [self.board[2][0], self.board[1][1], self.board[0][2]]]
        if [palyer, palyer, palyer] in win:
            return True

        return False

    def CheckFinalState(self):  
        return self.Winner(human) or self.Winner(ai)

    def Evaluate(self):
        if self.Winner(ai):
            return 1
        elif self.Winner(human):
            return -1
        return 0

    def MiniMax(self, high, player):
        if player == human:
            moveAndResult = [-1, -1, inf]
        else:
            moveAndResult = [-1, -1, -inf]

        if high == 0 or self.CheckFinalState():
            return [-1, -1, self.Evaluate()]

        for emptyCell in self.GetEmptyCells():
            x, y = emptyCell
            self.board[x][y] = player
            result = self.MiniMax(high - 1, -player)
            self.board[x][y] = 0

            if player == human:
                if result[2]<moveAndResult[2]:
                    moveAndResult = [x, y, result[2]]
            else:
                if result[2]>moveAndResult[2]:
                    moveAndResult = [x, y, result[2]]
               

        return moveAndResult

    def ValidMove(self, coord): 
        return coord in self.GetEmptyCells()

    def SetChoise(self, coord, player):
        if self.ValidMove(coord):
            x = coord[0]
            y = coord[1]
            self.board[x][y] = player
            return True
        return False

    def HumanTime(self):
        self.Clear()
        self.Render()
        print('The human plays')
        while True:
            try:
                getCoord = int(input('select a number from 1 to 9 :'))
                getCoord = coordDict[getCoord]
                valid = self.SetChoise(getCoord, human)

                if not valid:
                    print('bad move make another one')
                    print('\n')
                else:
                    break

            except KeyError:
                print('Out of range')
                print('\n')

    def AiTime(self):
        self.Clear()
        self.Render()
        print("The AI plays")

        high = len(self.GetEmptyCells())
        if high == 9:
            x = rnd.randint(0,2)
            y = rnd.randint(0,2)
        else:
            x,y,_ = self.MiniMax(high,ai)

        self.SetChoise([x,y],ai)


