from MainWindow import MainWindow
from GraphicalUI import GraphicalUI

if __name__ == "__main__":
    app = MainWindow()
    ui = GraphicalUI(app)
    app.mainloop()
