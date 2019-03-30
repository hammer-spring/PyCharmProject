'''
案例介绍
本案例采用 python 实现了一个简单的井字棋游戏。该游戏在控制台界面中进行，有游戏提示。游戏棋盘为 3 X 3 的九宫格样式，每个棋格与数字键盘上的 1 - 9 数字键一一对应，可通过输入数字来选择落棋位置和落子。游戏的规则是两个玩家轮流下棋，首先实现横线、竖线、斜线连续三个格棋子一样的获胜。

学习目标
本案例主要是对 python 基础知识的运用，包括语法、列表型数据结构、元组、类、函数、循环、条件判断、控制台输入与输出、引入模块等基础知识。通过本案例的学习，将强化对这些知识的理解和运用。

需要的引入的模块
本案例以 python 3.5.3 版本为基础，需要引入三个模块 random 、 sys 、 copy .

模块 random ：主要用于生成随机数；
模块 sys ：该模块包含了与 Python 解释器和它的环境有关的函数。
模块 copy ：主要用于拷贝对象。
案例结构和主要算法
该案例是个游戏，其主要算法为：

初始化棋盘，确定玩家执什么棋子，并随机确定谁执先手；
玩家和计算机轮换下棋。
计算机依据玩家落棋的位置，先依次做五个检测：自己下一步棋是否会赢、玩家下一步棋是否会赢、检测四个角是否为空、检测中心是否为空、检测边是否有空位，然后根据检测结果将棋子下在相应的位置，直到游戏结束。
该案例包含的功能模块
该案例只有一个程序文件： tictactoe.py ，其包含的功能模块为：

starGame( ) 函数：定义了本游戏的主要流程和逻辑——初始化棋盘、输出帮助信息、取得玩家姓名和希望执的棋子、随机选择谁执先手、进入游戏循环。
drawBoard( ) 函数：绘制或更新棋盘。如果没有棋盘，就绘制棋盘；如果棋盘已经存在，就更新棋盘。
help( ) 函数：输出帮助信息。
inputPlayerLetter( ) 函数：确定游戏双方选择的代表棋子的字符。
startGameLoop( ) 函数：定义了游戏的主循环。玩家和计算机轮换下棋，直到某一方获胜或达成平局。
getPlayerMove( ) 函数：玩家下棋，返回输入的位置数字。
makeMove( ) 函数：下棋，将字符配给相应的棋盘网格。
isWin( ) 函数：判断获胜的标准。
isBoardFull( ) 函数：检测棋盘是否下满棋。
isSpaceFree( ) 函数：检测哪个位置为空的，可以下棋。
getComputerMove( ) 函数：依次做五个检测，确定计算机要下棋的位置。
chooseRandomMove( ) 函数：随机下棋。
endGame( ) 函数：游戏结束时给出选择，再来一次，还是退出。
exitGame( ) 函数：退出游戏。
'''
# -*- coding: utf-8 -*-

import random
import sys
import copy

class TicTacToe:
    # 初始化信息
    def __init__(self):
        self.board = [' '] * 10
        self.playerName = ''
        self.playerLetter = ''
        self.computerName = 'Leo'
        self.computerLetter = ''
        self.corners = [1,3,7,9]
        self.sides = [2,4,6,8]
        self.middle = 5

        self.form = '''
            \t        |   |
            \t      %s | %s | %s
            \t        |   |
            \t    -------------
            \t        |   |
            \t      %s | %s | %s
            \t        |   |
            \t    -------------
            \t        |   |
            \t      %s | %s | %s
            \t        |   |
           '''

    # 开始游戏
    def startGame(self):
        # 欢迎信息
        print('''\n\t------------------------------------
                \n\t             TIC-TAC-TOE
                \n\t------------------------------------
             ''')

        # 画棋盘，调用 drawBoard()
        self.drawBoard(board = None)

        # 显示帮助信息，调用 help()
        self.help()

        # 获取玩家姓名
        self.playerName = input("您好，我是 %s" % self.computerName + ". 请问您的名字是? ")

        # 获取代表棋子的字符，调用 inputPlayerLetter()
        self.playerLetter, self.computerLetter = self.inputPlayerLetter()
        print("您的选择是 " + self.playerLetter)

        # 随机选择谁执先手，并开始游戏。调用 startGameLoop()
        if random.randint(0,1) == 0:
            print(self.computerName + "为执先手方!")
            self.startGameLoop(self.computerName)
        else:
            print(self.playerName + "为执先手方!")
            self.startGameLoop(self.playerName)

    # 画棋盘，如果游戏新开始，没有棋盘，就初始化棋盘，棋盘格都为空。如果在游戏中，就在网格中显示字符。
    def drawBoard(self,board = None):
        if board is None:
            print(self.form % tuple(self.board[7:10] + self.board[4:7] + self.board[1:4]))
        else:
            print(self.form % tuple(board[7:10] + board[4:7] + board[1:4]))

    # 帮助信息
    def help(self):
        print('''
        \n\t 游戏说明：
        \n\t 1、游戏棋盘是以 3 X 3 的九宫格形式。每格坐标与键盘上的小键盘 1 - 9 数字键一一对应。
        \n\t 2、游戏中，两个玩家轮流下棋，输入数字，将棋下在九宫格的相应格里。
        \n\t 3、首先实现横线、竖线、斜线连续三个格棋子一样的获胜。
        ''')

    # 玩家输入选择的代表棋子的字符
    def inputPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('您希望选择 X 还是 O ?')
            letter = input().upper()
        # 设置第一个字符为玩家，第二个为计算机
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    # 游戏主循环
    def startGameLoop(self,turn):
        gameIsRunning = True
        player = turn
        while gameIsRunning:
            # 如果是玩家下棋
            if player == self.playerName:
                playerInput = self.getPlayerMove()
                self.makeMove(self.board, self.playerLetter, playerInput)
                if(self.isWin(self.board, self.playerLetter)):
                    self.drawBoard()
                    print("\n\t恭喜您获胜，%s!!! \t\n" % self.playerName)
                    gameIsRunning = False
                else:
                    if self.isBoardFull():
                        self.drawBoard()
                        print("\n\t 您和%s战成平局!!! \n\t" % self.computerName)
                        gameIsRunning = False
                    else:
                        self.drawBoard()
                        player = self.computerName
            # 转为计算机下棋
            else:
                computerMove =  self.getComputerMove()
                self.makeMove(self.board, self.computerLetter, computerMove)
                if (self.isWin(self.board, self.computerLetter)):
                    self.drawBoard()
                    print("\n\t很遗憾，计算机%s获得了胜利 \t\n" % self.computerName)
                    gameIsRunning = False
                    break
                else:
                    if self.isBoardFull():
                        self.drawBoard()
                        print("\n\t 您和%s战成平局!!! \n\t" % self.computerName)
                        gameIsRunning = False
                    else:
                        self.drawBoard()
                        player = self.playerName

        # 当跳出游戏循环，及获胜、平局、失败后结束游戏。
        self.endGame()

    # 玩家下棋，返回输入的位置数字
    def getPlayerMove(self):
        move = int(input("请选择棋子位置: (1-9) "))
        while move not in range(1,10) or not self.isSpaceFree(self.board, move):
            move = int(input("无效操作，请重新选择: (1-9) "))
        return move

    # 下棋，将字符配给相应的棋盘网格
    def makeMove(self,board, letter, move):
        board[move] = letter

    # 判断获胜的标准
    def isWin(self, board, letter):
        if ((board[1] == letter and board[2] == letter and board[3] == letter) or      # 下横线
                (board[4] == letter and board[5] == letter and board[6] == letter) or  # 中横线
                (board[7] == letter and board[8] == letter and board[9] == letter) or  # 上横线
                (board[1] == letter and board[4] == letter and board[7] == letter) or  # 左竖线
                (board[2] == letter and board[5] == letter and board[8] == letter) or  # 中竖线
                (board[3] == letter and board[6] == letter and board[9] == letter) or  # 右竖线
                (board[1] == letter and board[5] == letter and board[9] == letter) or  # 一条对角线
                (board[3] == letter and board[5] == letter and board[7] == letter)):   # 又一条对角线
            return True
        else:
            return False

    # 检测棋盘是否下满
    def isBoardFull(self):
        for i in range(1,10):
            if self.isSpaceFree(self.board, i):
                return False
        return True

    # 检测哪个位置为空的，可以下棋
    def isSpaceFree(self, board, move):
        return board[move] == ' '

    # 计算机下棋，得到要下的位置
    # 依次做五个检测： 1、自己下一步棋是否会赢； 2、玩家下一步棋是否会赢； 3、检测四个角是否为空； 4、检测中心是否为空； 5、检测边是否有空位。
    def getComputerMove(self):
        for i in range(1, 10):
            boardCopy = copy.deepcopy(self.board)
            if self.isSpaceFree(boardCopy, i):
                self.makeMove(boardCopy, self.computerLetter, i)
                if self.isWin(boardCopy, self.computerLetter):
                    return i

        for i in range(1, 10):
            boardCopy = copy.deepcopy(self.board)
            if self.isSpaceFree(boardCopy, i):
                self.makeMove(boardCopy, self.playerLetter, i)
                if self.isWin(boardCopy, self.playerLetter):
                    return i

        move = self.chooseRandomMove(self.corners)
        if move != None:
            return move

        if self.isSpaceFree(self.board, self.middle):
            return self.middle

        return self.chooseRandomMove(self.sides)

    # 随机下棋
    def chooseRandomMove(self, moveList):
        possibleWinningMoves = []
        for move in moveList:
            if self.isSpaceFree(self.board, move):
                possibleWinningMoves.append(move)
                if len(possibleWinningMoves) != 0:
                    return random.choice(possibleWinningMoves)
                else:
                    return None

    # 游戏结束
    def endGame(self):
        playAgain = input("您希望再战一局吗? (y/n): ").lower()
        if playAgain == 'y':
            self.__init__()
            self.startGame()
        else:
            print("\n\t-- 游戏结束!!!--\n\t")
            self.exitGame()

    # 退出游戏
    def exitGame(self):
        print("\n\t 感谢您的参与 ? \n\t 欢迎下次再玩!\n")
        sys.exit()

if __name__ == "__main__":
     TTT = TicTacToe()
     TTT.startGame()