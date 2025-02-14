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
            self.__win.draw_line(line, "red")

        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, "black")
        else:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line, "red")

        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, "black")
        else:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line, "red")

        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, "black")
        else:
            line = Line(top_left, top_right)
            self.__win.draw_line(line, "red")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        mid_x_from = (self.__x1 + self.__x2) // 2
        mid_y_from = (self.__y1 + self.__y2) // 2

        mid_x_to = (to_cell.__x1 + to_cell.__x2) // 2
        mid_y_to = (to_cell.__y1 + to_cell.__y2) // 2

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
