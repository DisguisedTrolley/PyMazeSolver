from graphics import Line, Point, Window


class Cell:
    def __init__(
        self,
        p1: Point,
        p2: Point,
    ) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self.__win: Window = None
        self.__p1: Point = p1
        self.__p2: Point = p2

    def draw(self, win: Window) -> None:
        if not win:
            return

        self.__win = win
        top_left = Point(self.__p1.x, self.__p1.y)
        bottom_left = Point(self.__p1.x, self.__p2.y)
        top_right = Point(self.__p2.x, self.__p1.y)
        bottom_right = Point(self.__p2.x, self.__p2.y)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self.__win.draw_line(line, "black")
        else:
            line = Line(top_left, bottom_left)
            self.__win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, "black")
        else:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, "black")
        else:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, "black")
        else:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        mid_x_from = (self.__p1.x + self.__p2.x) // 2
        mid_y_from = (self.__p1.y + self.__p2.y) // 2

        mid_x_to = (to_cell.__p1.x + to_cell.__p2.x) // 2
        mid_y_to = (to_cell.__p1.y + to_cell.__p2.y) // 2

        p1 = Point(mid_x_from, mid_y_from)
        p2 = Point(mid_x_to, mid_y_to)

        line = Line(p1, p2)
        self.__win.draw_line(line, "red" if not undo else "gray")

    def break_wall(self, other: "Cell", dirn: str) -> None:
        match dirn:
            case "left":
                self.has_left_wall = False
                other.has_right_wall = False
                return

            case "right":
                self.has_right_wall = False
                other.has_left_wall = False
                return

            case "top":
                self.has_top_wall = False
                other.has_bottom_wall = False
                return

            case "bottom":
                self.has_bottom_wall = False
                other.has_top_wall = False
                return

            case _:
                return None

    def has_wall(self, other: "Cell", dirn: str) -> None:
        match dirn:
            case "left":
                return not self.has_left_wall and not other.has_right_wall

            case "right":
                return not self.has_right_wall and not other.has_left_wall

            case "top":
                return not self.has_top_wall and not other.has_bottom_wall

            case "bottom":
                return not self.has_bottom_wall and not other.has_top_wall

            case _:
                return None
