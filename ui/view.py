import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from threading import Thread
import requests
from src import app as quote_generator



class AsyncStream(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("thread")
        quote_generator.main()





class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Random Positivity')
        self.geometry('400x400')
        self.resizable(0, 0)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()

        self.current_quote_thread = None


    def start_stream(self):
        print("start button clicked")
        quote_thread = AsyncStream()
        quote_thread.start()
        self.current_quote_thread = quote_thread
        print("test2")

        #self.monitor(quote_thread)

    def stop_stream(self):
        print(self.current_quote_thread)
        #self.current_quote_thread.stop()

    def create_header_frame(self):

        self.header = ttk.Frame(self)
        # configure the grid
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=10)
        self.header.columnconfigure(2, weight=1)

        self.strtbutton = ttk.Button(self.header, text='Start')
        self.stopbutton = ttk.Button(self.header, text='Stop' )
        self.strtbutton['command'] = self.start_stream()
        self.stopbutton['command'] = self.stop_stream()


        self.strtbutton.grid(column=0, row=1, sticky=tk.W)
        self.stopbutton.grid(column=1, row=1, sticky=tk.W)
        # attach the header frame
        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)


    def monitor(self, thread):
        if thread.is_alive:
            # check the thread every 100ms
            self.after(1000, lambda: self.monitor(thread))
        else:
            self.html.insert(1.0, thread.html)
            self.download_button['state'] = tk.NORMAL

    def create_body_frame(self):
        self.body = ttk.Frame(self)
        # text and scrollbar
        self.html = tk.Text(self.body, height=20)
        self.html.grid(column=0, row=1)

        scrollbar = ttk.Scrollbar(self.body,
                                  orient='vertical',
                                  command=self.html.yview)

        scrollbar.grid(column=1, row=1, sticky=tk.NS)
        self.html['yscrollcommand'] = scrollbar.set

        # attach the body frame
        self.body.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)

    def create_footer_frame(self):
        self.footer = ttk.Frame(self)
        # configure the grid
        self.footer.columnconfigure(0, weight=1)
        # exit button
        self.exit_button = ttk.Button(self.footer,
                                      text='Exit',
                                      command=self.destroy)

        self.exit_button.grid(column=0, row=0, sticky=tk.E)

        # attach the footer frame
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)

if __name__ == "__main__":
    print("app started")
    app = App()
    app.mainloop()