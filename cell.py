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
            )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
    
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')

    def cell_aroud(self, x, y):
        for i in Cell.all:
            if i.x == x and i.y == y and i.x != None:
                return i

    def show_cell(self):
        cell_list = []
        cell_list.append(self.cell_aroud(self.x-1, self.y-1))
        cell_list.append(self.cell_aroud(self.x, self.y-1))
        cell_list.append(self.cell_aroud(self.x+1, self.y-1))
        cell_list.append(self.cell_aroud(self.x-1, self.y))
        cell_list.append(self.cell_aroud(self.x+1, self.y))
        cell_list.append(self.cell_aroud(self.x-1, self.y+1))
        cell_list.append(self.cell_aroud(self.x, self.y+1))
        cell_list.append(self.cell_aroud(self.x+1, self.y+1))
        mine_count = 0
        for i in cell_list:
            if i!=None and i.is_mine:
                mine_count+=1
        return self.cell_btn_object.configure(text=f'{mine_count}')
    
    def right_click_actions(self, event):
        print(f'I am {self.x},{self.y},{self.is_mine} right clicked')

    @staticmethod
    def randomize_cells():
        picked_cells = random.sample(Cell.all, settings.RAMDOM_MINE)
        for i in picked_cells:
            i.is_mine = True

    def __repr__(self):
        return f'Cell({self.x},{self.y},{self.is_mine})'