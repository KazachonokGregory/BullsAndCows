import tkinter as tk
import tkinter.ttk as ttk
import Utilities as util

class Table(ttk.Treeview):
    columns = ("number", "bulls", "cows")

    def __init__(self, *args, **kwargs):
        super().__init__(show='headings', columns=Table.columns, *args, **kwargs)

        self.heading("number", text="Number")
        self.heading("bulls", text="Bulls")
        self.heading("cows", text="Cows")
        self.column(0, width=100)
        self.column(1, width=50, stretch=False)
        self.column(2, width=50, stretch=False)
        self.config(selectmode="none")
        self.guess = None
        self.active_widgets = []

    def pop_edit(self, idx, column, accept_edit, validate):
        x, y, width, height = self.bbox(item=idx, column=column)
        vcmd = (self.register(validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        entry = tk.Entry(self, borderwidth=0, highlightthickness=0,
                validate='key', validatecommand=vcmd)

        entry.place(x=x, y=y, width=width, height=height)
        entry.focus_set()
        entry.grab_set()
        entry.bind("<Return>", accept_edit)
        self.active_widgets.append(entry)
        self.wait_window(entry)


    def make_guess(self):
        self.lst = self.insert("", tk.END, values=("", "", ""))
        self.master.update()
        self.pop_edit(self.lst, '0', self.accept_guess, self.validate_guess)
        return self.guess

    def accept_guess(self, event):
        guess = event.widget.get()
        self.guess = guess
        if not util.is_valid(guess):
            return
        event.widget.destroy()
        self.item(self.lst, values=(guess, '?', '?'))
        self.master.update()

    def receive_result(self, result):
        bulls, cows = result[0], result[1]
        self.item(self.lst, values=(self.guess, bulls, cows))
        self.master.update()

    def get_result(self, guess):
        self.guess = guess
        self.lst = self.insert("", tk.END, values=(guess, "?", "?"))
        self.pop_edit(self.lst, 1, self.accept_bulls, self.validate_bulls_cows)
        self.pop_edit(self.lst, 2, self.accept_cows, self.validate_bulls_cows)
        return (self.bulls, self.cows)

    def accept_bulls(self, event):
        bulls = event.widget.get()
        if not bulls.isdigit() or int(bulls) > util.DIGIT_COUNT:
            return
        event.widget.destroy()
        self.bulls = bulls
        self.item(self.lst, values=(self.guess, self.bulls, '?'))
        self.master.update()

    def accept_cows(self, event):
        cows = event.widget.get()
        if not cows.isdigit() or int(cows) > util.DIGIT_COUNT:
            return
        event.widget.destroy()
        self.cows = cows
        self.item(self.lst, values=(self.guess, self.bulls, self.cows))
        self.master.update()

    def validate_guess(self, action, index, value_if_allowed,
            prior_value, text, validation_type, trigger_type, widget_name):
        return util.is_almost_valid(value_if_allowed)

    def validate_bulls_cows(self, action, index, value_if_allowed,
            prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed == "":
            return True
        return value_if_allowed.isdigit() and len(value_if_allowed) == 1 and int(value_if_allowed) <= util.DIGIT_COUNT

    def destroy(self):
        for widget in self.active_widgets:
            widget.destroy()
        super().destroy()
