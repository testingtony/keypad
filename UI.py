import tkinter as tk


class Pages:
    def __init__(self, root, width, height):
        self._root = root
        self._width = width
        self._height = height
        self.pages = dict()

    def page(self, name):
        try:
            p = self.pages[name]
        except KeyError:
            p = Page(self._root, name, self._width, self._height, 160, 160)
            self.pages[name] = p
        return p

    def show(self, name):
        for page in self.pages.values():
            page.hide()
        self.pages[name].show()


def positions(frame_width, frame_height, button_width, button_height):
    for y in range(0, frame_height // button_height):
        for x in range(0, frame_width // button_width):
            yield {"x": button_width * x, "y": button_height * y, "width": button_width, "height": button_height}


class Page:
    def __init__(self, root, name, width, height, button_width, button_height):
        self._root = root
        self._name = name
        self._width = width
        self._height = height
        self._buttons = dict()
        self.positions = positions(width, height, button_width, button_height)
        self.frame = tk.Frame(self._root)

    def show(self):
        self.frame.place(x=0, y=0, width=self._width, height=self._height)

    def hide(self):
        self.frame.place_forget()

    def button(self, text, command=None):
        b = tk.Button(self.frame, text=text, command=command)
        b.place(next(self.positions))


if __name__ == '__main__':
    top = tk.Tk()
    top.geometry("480x320")
    pages = Pages(top, 480, 320)

    p1 = pages.page("main")
    p2 = pages.page("second")

    p1.button("1.1", command=lambda: pages.show("second"))
    p1.button("1.2")
    p2.button("2.1")
    p2.button("2.2", command=lambda: pages.show("main"))
    p2.button("2.3")
    p2.button("2.4")

    pages.show("main")

    tk.mainloop()
