from constants import (
    MARGIN,
    NUM_COLS,
    NUM_ROWS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from graphics import Window
from maze import Maze


def main():
    cell_size_x = (SCREEN_WIDTH - 2 * MARGIN) // NUM_COLS
    cell_size_y = (SCREEN_HEIGHT - 2 * MARGIN) // NUM_ROWS

    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    Maze(MARGIN, MARGIN, NUM_ROWS, NUM_COLS, cell_size_x, cell_size_y, win, 42)

    win.wait_for_close()


if __name__ == "__main__":
    main()
