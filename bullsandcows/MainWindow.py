import tkinter as tk
from tkinter import messagebox as msg
import config
import OnlineGame
import OfflineGame
from Table import Table

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Bulls & Cows")
        self.geometry("500x400")
        self.configure(bg=config.primary_color)
        self.resizable(True, True)

        self.my_table = Table(self)
#        self.my_table.grid(column=1, row=1, pady=5)

        self.opp_table = Table(self)
#        self.opp_table.grid(column=0, row=1, pady=5)

        self.status_bar = tk.Label(self, justify='left')
#        self.status_bar.grid(column=0, row=0)

#        self.columnconfigure(0, weight=1)
#        self.rowconfigure(0, weight=1)

        self.status_bar.pack(side='top', fill='x')
        self.opp_table.pack(side='left', anchor='nw', fill='y')
        self.my_table.pack(side='right', anchor='ne', fill='y')

        self.set_message('Welcome!')

        self.ask_game_type()

    def set_message(self, message):
        self.status_bar.config(text=message)

    def ask_game_type(self):
        popup = tk.Toplevel(self)
        popup.title('Choose the game type')
        popup.attributes("-topmost", "true")
        self.game_type = tk.StringVar(value="host")
        host_butt = tk.Radiobutton(popup, text="Host game", value="host", variable=self.game_type)
        connect_butt = tk.Radiobutton(popup, text="Connect to game", value="connect", variable=self.game_type)
        bot_butt = tk.Radiobutton(popup, text="Offline game (with a bot)", value="bot", variable=self.game_type)
        host_butt.pack(anchor='w')
        connect_butt.pack(anchor='w')
        bot_butt.pack(anchor='w')
        def accept_game_type(event=None):
            self.game_type = self.game_type.get()
            popup.destroy()
            if self.game_type == "host" or self.game_type == "connect":
                self.ask_host_port()
        accept_butt = tk.Button(popup, text='Accept', command=accept_game_type)
        accept_butt.pack()
        self.wait_window(accept_butt)

    def ask_host_port(self):
        popup = tk.Toplevel(self)
        popup.title('Type host and port')
        popup.attributes("-topmost", "true")
        host_name = tk.Entry(popup)
        port_name = tk.Entry(popup)
        host_name.insert(0, "localhost")
        port_name.insert(0, "9999")
        host_name.pack(anchor='w')
        port_name.pack(anchor='w')
        def accept_host_port(event=None):
            self.host_name = host_name.get()
            self.port_name = int(port_name.get())
            popup.destroy()
        accept_butt = tk.Button(popup, text='Accept', command=accept_host_port)
        accept_butt.pack()
        self.wait_window(accept_butt)



