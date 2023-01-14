from tkinter import Button, Label, messagebox
from PIL import Image, ImageTk
import random
import settings
import sys
import time


class Cell():
    all = []
    cell_count = settings.TOTAL_CELL_QUANTITY
    cell_count_object = None
    def __init__(self, x, y, is_mine=False, is_opened = False, marked_as_mine = False):
        self.is_mine = is_mine
        self.marked_as_mine = marked_as_mine
        self.is_opened = is_opened
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            bg='#f0f0f3',
            width=settings.CELL_SIZE_WIDTH,
            height=settings.CELL_SIZE_HEIGHT,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_label_cell_count(location):
        label = Label(
            location,
            bg='black',
            fg='white',
            font=('', 30),
            text=f'cell left: {Cell.cell_count}'
        )
        Cell.cell_count_object = label

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            if self.cell_mine_surrounded_length == 0:
                for cell in self.cell_surrounded_list:
                        cell.show_cell()


    def show_mine(self):
        for i in Cell.all:
            if i.is_mine:
                i.cell_btn_object.configure(bg='red')
        self.cell_btn_object.configure(bg='red')
        messagebox.showwarning("GAME OVER", "You clicked on a mine!")
        sys.exit()


    def cell_around(self, x, y):
        for i in Cell.all:
            if i.x == x and i.y == y:
                return i

    @property
    def cell_surrounded_list(self):
        cell_list = []
        cell_list.append(self.cell_around(self.x-1, self.y-1))
        cell_list.append(self.cell_around(self.x, self.y-1))
        cell_list.append(self.cell_around(self.x+1, self.y-1))
        cell_list.append(self.cell_around(self.x-1, self.y))
        cell_list.append(self.cell_around(self.x+1, self.y))
        cell_list.append(self.cell_around(self.x-1, self.y+1))
        cell_list.append(self.cell_around(self.x, self.y+1))
        cell_list.append(self.cell_around(self.x+1, self.y+1))
        cell_list = [cell for cell in cell_list if cell is not None]
        return cell_list

    @property
    def cell_mine_surrounded_length(self):
        counter = 0
        for i in self.cell_surrounded_list:
            if i.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        color_numb = {'blue': 1,'green': 2, 'red': 3, 'Purple': 4}
        if not self.is_opened:
            for key,value in color_numb.items():
                if self.cell_mine_surrounded_length == value:
                    self.cell_btn_object.configure(fg=f'{key}')    
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=f'{self.cell_mine_surrounded_length}',bg='#f0f0f3')
            if Cell.cell_count_object:
                Cell.cell_count_object.configure(text=f'Cell Left: {Cell.cell_count}')
        self.is_opened = True
        is_mine_cell = 0
        for i in Cell.all:
            if i.is_mine:
                is_mine_cell += 1
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
        if Cell.cell_count == is_mine_cell:
            for i in Cell.all:
                if i.is_mine:
                    i.cell_btn_object.configure(bg='red')
            messagebox.showinfo("Congrats!!", "You Won!!!")
            sys.exit()         

    def right_click_actions(self, event):
        if not self.is_opened:
            if not self.marked_as_mine:
                self.cell_btn_object.configure(bg='orange')
                self.marked_as_mine = True
            else:
                self.cell_btn_object.configure(bg='#f0f0f3')
                self.marked_as_mine = False


    @staticmethod
    def randomize_cells():
        picked_cells = random.sample(Cell.all, settings.RAMDOM_MINE)
        for i in picked_cells:
            i.is_mine = True

    def __repr__(self):
        return f'Cell({self.x},{self.y},{self.is_mine})'
