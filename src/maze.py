import random
import time

from cell import Cell
from constants import D_COL, D_ROW, NUM_COLS, NUM_ROWS
from graphics import Point, Window


def get_direction(x: list[int, int], y: list[int, int]) -> str:
    x1 = x[0]
    x2 = y[0]
    y1 = x[1]
    y2 = y[1]

    if x2 - x1 == 1:
        return "bottom"
    elif x2 - x1 == -1:
        return "top"

    if y2 - y1 == 1:
        return "right"
    elif y2 - y1 == -1:
        return "left"


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
        seed: int | None = None,
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells: list[list[Cell]] = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

        if seed is not None:
            random.seed(seed)

    def __create_cells(self) -> None:
        for j in range(self.__num_cols):
            row = []
            for i in range(self.__num_rows):
                # Top left coords.
                x1 = self.__x1 + i * self.__cell_size_x
                y1 = self.__y1 + j * self.__cell_size_y

                # bottom right coords.
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y

                p1 = Point(x1, y1)
                p2 = Point(x2, y2)

                cell = Cell(p1, p2)

                row.append(cell)

            self.__cells.append(row)
        self.__draw_cells()
        return

    def __draw_cells(self) -> None:
        if not self.__win:
            return

        for row in self.__cells:
            for cell in row:
                cell.draw(self.__win)
                self.__animate()

    def __animate(self) -> None:
        if not self.__win:
            return

        self.__win.redraw()
        time.sleep(0)

    def __break_entrance_and_exit(self) -> None:
        top_left_cell = self.__cells[0][0]
        top_left_cell.has_top_wall = False

        bottom_right_cell = self.__cells[-1][-1]
        bottom_right_cell.has_bottom_wall = False

        self.__draw_cells()

    def __isValid(self, row: int, col: int) -> bool:
        if row < 0 or col < 0 or row >= NUM_ROWS or col >= NUM_COLS:
            return False

        if self.__cells[row][col].visited:
            return False

        return True

    def __break_walls_r(self, row: int, col: int) -> None:
        self.__cells[row][col].visited = True

        while True:
            dirns: list[list[int, int]] = []

            for i in range(4):
                dir_x = row + D_ROW[i]
                dir_y = col + D_COL[i]

                if self.__isValid(dir_x, dir_y):
                    dirns.append([dir_x, dir_y])

            if len(dirns) == 0:
                self.__cells[row][col].draw(self.__win)
                return

            rand_index = random.randint(0, len(dirns) - 1)
            new_dirn = dirns[rand_index]

            r = new_dirn[0]
            c = new_dirn[1]
            get_mov_dir = get_direction([row, col], [r, c])
            curr_cell = self.__cells[row][col]
            next_cell = self.__cells[r][c]

            curr_cell.break_wall(next_cell, get_mov_dir)

            self.__break_walls_r(r, c)

    # NOTE : The implementation below is something i attempted to do without recursion.
    # Needless to say, it sucks. I mean not totally sucks, it kinda works but kinds doesn't.
    # I'll figure it out some day. For now, the above code works good enough.

    # def __break_walls_r(self, row: int, col: int) -> None:
    #     directions: list[list[int, int]] = []
    #     directions.append([row, col])
    #     prev: list[int, int] = []
    #
    #     while len(directions) > 0:
    #         current = directions.pop()
    #
    #         row = current[0]
    #         col = current[1]
    #
    #         if not self.__isValid(row, col):
    #             continue
    #
    #         self.__cells[row][col].visited = True
    #
    #         if prev:
    #             # print(f"PREV: {prev}, CURR: {[row, col]}")
    #             dirn = get_direction(prev, [row, col])
    #             # print(f"DIRN: {dirn}")
    #             # print("\n")
    #             prev_cell = self.__cells[prev[0]][prev[1]]
    #             curr_cell = self.__cells[row][col]
    #
    #             prev_cell.break_wall(curr_cell, dirn)
    #
    #         self.__cells[row][col].draw(self.__win)
    #
    #         all_dirns = []
    #         for i in range(4):
    #             adj_x = row + D_ROW[i]
    #             adj_y = col + D_COL[i]
    #             all_dirns.append([adj_x, adj_y])
    #
    #         random.shuffle(all_dirns)
    #         directions.extend(all_dirns)
    #         prev = [row, col]
