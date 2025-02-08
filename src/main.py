from graphics import Line, Point, Window


def main():
    win = Window(800, 600)

    p1 = Point(1, 100)
    p2 = Point(200, 100)

    line = Line(p1, p2)
    win.draw_line(line, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()
