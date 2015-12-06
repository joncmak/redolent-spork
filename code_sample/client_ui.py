from tkinter import *

class ClientUI:
    def __init__(self):
        root = Tk()
        root.iconbitmap('favicon.ico')
        root.title('Client UI - rodelent-spork')
        root.geometry("275x100")
        self.makeWidgets(root)
        root.mainloop()

    def makeWidgets(self, root):
        # Top and bottom frame
        top_frame = Frame(root)
        bot_frame = Frame(root)
        top_frame.pack()
        bot_frame.pack(side=BOTTOM)

        # Name label and entry
        name_label = Label(top_frame, text='Name:', padx=20)
        self.name_entry = Entry(top_frame)
        name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        # Ip address label and entry
        ip_label = Label(top_frame, text='Ip address:')
        self.ip_entry = Entry(top_frame)
        ip_label.grid(row=1, column=0)
        self.ip_entry.grid(row=1, column=1)

        # Port label and entry
        port_label = Label(top_frame, text='Port:')
        self.port_entry = Entry(top_frame)
        port_label.grid(row=2, column=0)
        self.port_entry.grid(row=2, column=1)

        # Connect, Empty label buffer and Quit button
        self.connect = Button(bot_frame,
                              text="Connect",
                              fg="green",
                              width=10,
                              command=self.connect_to_server)
        empty_label = Label(bot_frame, text='', padx=5, pady=10)
        self.quit = Button(bot_frame,
                           text="Quit",
                           fg="red",
                           width=10,
                           command=root.quit)
        self.connect.grid(row=0, column=0)
        empty_label.grid(row=0, column=1)
        self.quit.grid(row=0, column=2)

    # Connection code goes in here
    def connect_to_server(self):
        print('%s is connecting to %s on port %s'
              % (self.name_entry.get(), self.ip_entry.get(), self.port_entry.get()))

if __name__ == "__main__":
    ui = ClientUI()
