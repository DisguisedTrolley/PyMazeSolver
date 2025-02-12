from graphics import Line, Point, Window


class Cell:
    def __init__(
        self,
        p1: Point,
        p2: Point,
        win: Window,
        has_left: bool = True,
        has_right: bool = True,
        has_top: bool = True,
        has_bottom: bool = True,
    ) -> None:
        self.has_left_wall = has_left
        self.has_right_wall = has_right
        self.has_top_wall = has_top
        self.has_bottom_wall = has_bottom

        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y

        self.__win = win

    def draw(self) -> None:
        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        mid_x_from = (self.__x1 + self.__x2) // 2
        mid_y_from = (self.__y1 + self.__y2) // 2

        mid_x_to = (to_cell.__x1 + to_cell.__x2) // 2
        mid_y_to = (to_cell.__y1 + to_cell.__y2) // 2

        p1 = Point(mid_x_from, mid_y_from)
        p2 = Point(mid_x_to, mid_y_to)

        line = Line(p1, p2)
        self.__win.draw_line(line, "red" if not undo else "gray")
