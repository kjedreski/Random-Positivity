import pyperclip
import random
import datetime
import time
import ExtractQuotes
import sqlite3
from sqlite3 import Error

code_bank = [
    'Good Luck!, Remember this is a game about teamwork and positivity',
    'Wow! Nice one:)',
    'Have a great day all!',
]

positive_quote_bank = []


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


main()
# local_test_run()
