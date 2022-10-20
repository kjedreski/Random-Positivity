import pyperclip
import random
import datetime
import time
import ExtractQuotes
import sqlite3
from sqlite3 import Error

codeBank = [
    'Good Luck!, Remember this is a game about teamwork and positivity',
    'Wow! Nice one:)',
    'Have a great day all!',
]

positiveQuoteBank = []


def local_test_run():
    while (True):
        rng = random.randrange(1, 3)
        rngCodeBankIndex = random.randrange(0, 3)
        x = datetime.datetime.now()
        randomCode = codeBank[rngCodeBankIndex].format(x.strftime("%X"), rng)
        # randomCode = niceCompBank[rngCodeBankIndex]
        pyperclip.copy(randomCode)
        pyperclip.paste()
        time.sleep(10)


def main():
    database = "C:\SQlite\positiveQuote.db"
    # create a database connection
    conn = ExtractQuotes.create_connection(database)
    rng = 100
    positiveQuoteBank = ExtractQuotes.read_quotes(conn, rng)
    while (True):
        rngCodeBankIndex = random.randrange(0, 100)
        posQuote = positiveQuoteBank[rngCodeBankIndex]
        # print("'{}' - {}".format(posQuote[1],posQuote[0]))
        pyperclip.copy("'{}' - {}".format(posQuote[1], posQuote[0]))
        pyperclip.paste()
        time.sleep(10)


main()
# local_test_run()
