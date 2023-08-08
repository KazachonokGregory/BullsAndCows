from MainWindow import MainWindow
from UI import GraphicalUI

if __name__ == "__main__":
    app = MainWindow()
    ui = GraphicalUI(app)
    app.mainloop()
