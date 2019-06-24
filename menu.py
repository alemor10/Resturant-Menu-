from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()


    def init_window(self):
        
        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)


    def create_widgets(self):
        self.orders_to_go = Button(self)
        self.orders_to_go["text"] = "Orders to Go"
        self.orders_to_go["command"] = self.say_ToGo
        self.orders_to_go.pack(side="bottom")


        self.orders_at_bar = Button(self)
        self.orders_at_bar["text"] = "Orders at Bar"
        self.orders_at_bar["command"] = self.say_Bar
        self.orders_at_bar.pack(side="bottom")


        self.table11 = Button(self)
        self.table11["text"] = "Table 11"
        self.table11.pack(side="left")

        self.table12 = Button(self)
        self.table12["text"] = "Table 12"
        self.table12.pack(side="left")

    def say_ToGo(self):
        print("to go Order")

    def say_Bar(self):
        print("order at the bar")

    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x300")
app = Application(master=root)
app.mainloop()