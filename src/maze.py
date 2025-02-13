import time

from cell import Cell
from graphics import Point, Window


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
