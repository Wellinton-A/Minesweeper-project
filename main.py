from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(100),
    height=utils.height_prct(25)
)
 
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=180)

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(x=360, y=180)

for x in range(settings.GRID_WIDTH_SIZE):
    for y in range(settings.GRID_HEIGHT_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.randomize_cells()
print(Cell.all)
for i in Cell.all:
    if i.is_mine == True:
        print(i.x, i.y)
root.mainloop()
