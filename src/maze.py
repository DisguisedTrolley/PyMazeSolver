import random
import time

from cell import Cell
from constants import D_COL, D_ROW, NUM_COLS, NUM_ROWS
from graphics import Point, Window


def get_direction(x) -> str | None:
    match x:
        case 0:
            return "right"
        case 1:
            return "left"
        case 2:
            return "bottom"
        case 3:
            return "top"
        case _:
            raise ValueError(f"Invalid value {x}")


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
        time.sleep(0.05)

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
        directions: list[list[int, int]] = []
        directions.append([row, col])

        while len(directions) > 0:
            current = directions.pop()
            row = current[0]
            col = current[1]

            if not self.__isValid(row, col):
                continue

            self.__cells[row][col].visited = True
            self.__cells[row][col].has_right_wall = False
            self.__cells[row][col].draw(self.__win)

            all_dirns = []
            for i in range(4):
                adj_x = row + D_ROW[i]
                adj_y = col + D_COL[i]
                all_dirns.append([adj_x, adj_y])

            random.shuffle(all_dirns)
            directions.extend(all_dirns)
