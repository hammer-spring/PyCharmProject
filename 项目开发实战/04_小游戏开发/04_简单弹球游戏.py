'''
案例介绍
本案例采用 python 实现了一个简单的弹球游戏。该游戏在一个单独的图形窗口中运行。游戏初始化后，在游戏窗口点击鼠标左键开始游戏。玩家通过控制键盘的左、右方向键来控制弹板的移动，弹球和弹板撞击一次，得一分，当弹球触底时，本局游戏结束。玩家一共有四条生命，即可以玩四次游戏，当生命大于等于“ 0 ”时，可以继续游戏，当生命小于“ 0 ”时，游戏结束。

学习目标
本案例主要是对 python 和 GUI 编程（本案例为库 tkinter ）的基础知识的运用，包括 python 的语法、类、函数、条件判断、引入模块、类的继承等基础知识和 tkinter 的创建图形界面、canvas 组件的创建及其属性、方法、事件等的操作的基础知识。通过本案例的学习，将强化对这些知识的理解和运用，为进一步学习打下良好的基础。

需要的引入的模块
本案例以 python3.5.3 版本为基础，需要引入模块 tkinter, 该模块是 Python 的标准 Tk GUI 工具包的接口，是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。

案例结构和主要算法
该案例为一个游戏，其运行的主要逻辑为：
设置游戏：绘制窗口、弹板、初始弹球，设置生命提示文本、得分提示文本、游戏提示文本，将鼠标左键单击事件与开始游戏函数绑定在一起。
单击鼠标左键开始游戏后，解除鼠标左键单击事件绑定、重设得分、删除游戏提示文本。
进入游戏循环。判断弹球是否触底？
弹球触底：弹球速度设为“ 0 ”，生命值减 1，再判断生命值是否小于“ 0 ”。如果小于“ 0 ”，游戏结束，否则重新开始执行第 1 项。
弹球未触底：首先绘制弹球，然后再重新执行第 3 项。
弹球偏移量确定的算法为：
预设弹球速度为 10，预设弹球运动方向为 direction =[1，-1]（向右向上运动）。
当弹球碰到画布上顶边、左边、右边和碰到弹板时，方向取反。
取横坐标 x = direction[0]、纵坐标 y = direction[1]，将方向与速度相乘，得到弹球的偏移量（x,y）。
判定弹球与弹板相撞的算法为：
取得弹球和弹板的坐标。
当弹球的横坐标在弹板之间，且弹球的右下角的纵坐标在弹板的左上角与右下角的纵坐标之间时，判定为弹球与弹板相撞。
该案例包含的功能模块
该案例只有一个程序文件：pinball_game.py，其包含的功能模块为：

类 GameObject 定义了游戏的对象的一些通用方法，各方法如下：
delete( ) 函数：该函数功能为删除指定对象。
get_coords( ) 函数：该函数功能为获得指定对象的坐标。
move( ) 函数：该函数功能为对指定对象进行移动。
类 Racket(GameObject) 继承类 GameObject，定义了游戏中弹板的一些参数和方法，具体内容如下：
__init__( ) 函数：该函数功能为定义变量和调用父类的实例的init方法。
draw( ) 函数：该函数功能为定义了如何绘制弹板。
类 Ball(GameObject) 继承类 GameObject，定义了游戏中弹球的一些参数和方法，具体内容如下：
__init__( ) 函数：该函数功能为定义变量和调用父类的实例的init方法。
draw( ) 函数：该函数功能为定义了如何绘制弹球。
类 Game(tk.Frame) 继承类 tk.Frame, 定义了游戏中的变量和游戏的完整流程，具体内容如下：
__init__( ) 函数：该函数定义了游戏参数的初始值，包括生命、得分、画布大小、画布的创建和放置、初始化弹板位置并绘制，设置游戏，并将键盘焦点转移到画布组件上，同时将键盘左、右键按键事件与弹板左、右移动函数绑定在一起。
setup_game( ) 函数：该函数功能为加载或设置游戏，设置内容依次为
重设弹球；
设置生命提示文本；
设置得分提示文本；
设置游戏提示文本；
将鼠标左键单击事件与开始游戏函数绑定在一起。
reset_ball( ) 函数：该函数功能为重设弹球，将弹球设置在弹板中间位置的上方。
update_lives_text( ) 函数：该函数功能为设置或更新生命提示文本。
update_scores_text( ) 函数：该函数功能为设置或更新得分提示文本。
start_game( ) 函数：该函数功能为定义了开始游戏后的程序运行流程或逻辑，依次为解除绑定、重设得分、删除提示文本、开始游戏循环。
reset_score( ) 函数：该函数功能为重置得分为“ 0 ”。
game_loop( ) 函数：该函数功能为定义了游戏循环的内容。如果弹球触底，就将弹球的速度变为“ 0 ”，生命减 1，否则绘制弹球，再次进行游戏循环。如果生命小于 0，游戏结束，否则调整得分，重新设置游戏，再开始一局。
hit_racket( ) 函数：该函数功能为定义了弹球与弹板的碰撞条件，每碰撞一次就更新一次得分。
'''
# -*- coding: utf-8 -*-

import tkinter as tk

# 游戏对象的一些通用方法
class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    # 删除对象
    def delete(self):
        self.canvas.delete(self.item)

    # 得到对象的坐标
    def get_coords(self):
        return self.canvas.coords(self.item)

    # 对象移动
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

class Racket(GameObject):
    def __init__(self, canvas, x, y):
        item = canvas.create_rectangle(x, y, x + 90, y + 10, fill='green')
        super().__init__(canvas, item)

    # 绘制弹板
    def draw(self, offset):
        pos = self.get_coords()
        width = self.canvas.winfo_width()
        # 当弹板在画布内时，按给定偏移量移动
        if pos[0] + offset >= 0 and pos[2] + offset <= width:
            super().move(offset, 0)

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(x, y, x + 20, y + 20, fill='blue')
        super().__init__(canvas, item)

    # 绘制弹球
    def draw(self):
        pos = self.get_coords()
        self.canvas_width = self.canvas.winfo_width()
        # 方向判断
        if pos[1] <= 0:
            self.direction[1] *= -1
        if game.hit_racket():
            self.direction[1] *= -1
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.direction[0] *= -1
        # 偏移量
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

# 游戏类，定义了游戏的完整流程
class Game(tk.Frame):
    def __init__(self, master):
        #调用父类 ( tk.Frame ) 并返回该类实例的__init__方法。
        super().__init__(master)

        self.lives = 3
        self.scores = 0
        self.width = 800
        self.height = 600

        # 设置画板并放置
        self.canvas = tk.Canvas(self, bg='#f8c26c', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()

        self.ball = None
        self.lives_text = None
        self.scores_text = None

        # 初始化弹板
        self.racket = Racket(self.canvas, self.width/2-45, 480)

        self.setup_game()
        # 将键盘焦点转移到画布组件上
        self.canvas.focus_set()

        # 将键盘左右键与弹板左右移动绑定在一起
        self.canvas.bind('<KeyPress-Left>', lambda turn_left: self.racket.draw(-20))
        self.canvas.bind('<KeyPress-Right>', lambda turn_right: self.racket.draw(20))

    # 加载游戏，或预置游戏
    def setup_game(self):
        # 将球设置在弹板中间位置的上方
        self.reset_ball()
        # 预置生命、得分和游戏提示的文本
        self.update_lives_text()
        self.update_scores_text()
        self.text = self.canvas.create_text(400, 200, text='单击鼠标左键开始游戏', font=('Helvetica', 36))
        # 将鼠标左键单击与开始游戏绑定在一起
        self.canvas.bind('<Button-1>', lambda start_game: self.start_game())

    # 在游戏预置时添加弹球，弹球在弹板中间位置的上方
    def reset_ball(self):
        if self.ball != None:
            self.ball.delete()
        racket_pos = self.racket.get_coords()
        x = (racket_pos[0] + racket_pos[2]) * 0.5-10
        self.ball = Ball(self.canvas, x, 350)

    # 更新生命的数字
    def update_lives_text(self):
        text = '生命: %s' % self.lives
        if self.lives_text is None:
            self.lives_text = self.canvas.create_text(60, 30, text=text, font=('Helvetica', 16), fill='green')
        else:
            self.canvas.itemconfig(self.lives_text, text=text)

    # 更新得分的数字
    def update_scores_text(self):
        text = '得分: %s' % self.scores
        if self.scores_text is None:
            self.scores_text = self.canvas.create_text(60, 60, text=text, font=('Helvetica', 16), fill='green')
        else:
            self.scores = self.scores + 1
            text = '得分: %s' % self.scores
            self.canvas.itemconfig(self.scores_text, text=text)

    # 开始游戏
    def start_game(self):
        # 依次解除绑定、重设得分、删除提示文本、开始游戏循环
        self.canvas.unbind('<Button-1>')
        self.reset_score()
        self.canvas.delete(self.text)
        self.game_loop()

    # 重置得分的数字为“ 0 ”
    def reset_score(self):
        self.scores = 0
        text = '得分: %s' % self.scores
        self.canvas.itemconfig(self.scores_text, text=text)

    # 游戏循环
    def game_loop(self):
        # 如果弹球超过底部，则将弹球的速度变为 0，lives 减 1，否则绘制弹球，再次进行游戏循环
        if self.ball.get_coords()[3] >= self.height:
            self.ball.speed = 0
            self.lives -= 1
            # 如果 lives 小于 0，游戏结束，否则调整 scores，重新预置游戏
            if self.lives < 0:
                self.canvas.create_text(400, 200, text='游戏结束', font=('Helvetica', 36), fill='red')
            else:
                self.scores = self.scores - 1
                self.after(1000, self.setup_game)
        else:
            self.ball.draw()
            self.after(50, self.game_loop)

    # 弹球与弹板的碰撞条件，当碰撞一次就更新一次得分
    def hit_racket(self):
        ball_pos = self.ball.get_coords()
        racket_pos = self.racket.get_coords()
        if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
            if ball_pos[3] >= racket_pos[1] and ball_pos[3] <= racket_pos[3]:
                self.update_scores_text()
                return True
        return False

if __name__ == '__main__':
    root = tk.Tk()
    root.title('弹球游戏')
    # 设定窗口大小不可改变
    root.resizable(0, 0)
    # 设定窗口总是显示在最前面
    root.wm_attributes("-topmost", 1)
    game = Game(root)
    game.mainloop()
