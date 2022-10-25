import pyperclip
import random
import datetime
import time
from src import ExtractQuotes
from threading import Thread
import requests


code_bank = [
    'Good Luck!, Remember this is a game about teamwork and positivity',
    'Wow! Nice one:)',
    'Have a great day all!',
]

positive_quote_bank = []

class AsyncQuotesOnGoing(Thread):
    def __init__(self, url):
        super().__init__()
        self.html = None
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.html = response.text

def handle_download(self):
    url = self.url_var.get()
    if url:
        self.download_button['state'] = tk.DISABLED
        self.html.delete(1.0, "end")

        download_thread = AsyncDownload(url)
        download_thread.start()

        self.monitor(download_thread)
    else:
        showerror(title='Error',
                message='Please enter the URL of the webpage.')


def monitor(self, thread):
    if thread.is_alive():
        # check the thread every 100ms
        self.after(100, lambda: self.monitor(thread))
    else:
        self.html.insert(1.0, thread.html)
        self.download_button['state'] = tk.NORMAL






#Local testing only.
def local_test_run():
    while (True):
        rng = random.randrange(1, 3)
        rng_code_bank_index = random.randrange(0, 3)
        x = datetime.datetime.now()
        random_code = code_bank[rng_code_bank_index].format(x.strftime("%X"), rng)
        # random_code = niceCompBank[rng_code_bank_index]
        pyperclip.copy(random_code)
        pyperclip.paste()
        time.sleep(10)


def main():
    database = "C:\SQlite\positiveQuote.db"
    # create a database connection
    conn = ExtractQuotes.create_connection(database)
    rng = 100
    quotes = ExtractQuotes.read_quotes(conn, rng)
    while (True):
        rngCodeBankIndex = random.randrange(0, 100)
        posQuote = quotes[rngCodeBankIndex]
        # print("'{}' - {}".format(posQuote[1],posQuote[0]))
        pyperclip.copy("'{}' - {}".format(posQuote[1], posQuote[0]))
        pyperclip.paste()
        time.sleep(10)


def end():
    return


#main()
# local_test_run()
