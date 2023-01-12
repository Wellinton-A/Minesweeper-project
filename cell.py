from tkinter import Button
import random
import settings

class Cell():
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=settings.CELL_SIZE_WIDTH,
            height=settings.CELL_SIZE_HEIGHT,
            text=f'{self.x},{self.y}')
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(f'I am {self.x},{self.y},{self.is_mine} left clicked')

    def right_click_actions(self, event):
        print(f'I am {self.x},{self.y},{self.is_mine} right clicked')

    @staticmethod
    def randomize_cells():
        picked_cells = random.sample(Cell.all, settings.RAMDOM_MINE)
        for i in picked_cells:
            i.is_mine = True

    def __repr__(self):
        return f'Cell({self.x},{self.y},{self.is_mine})'