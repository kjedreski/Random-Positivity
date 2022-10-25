import sqlite3
from sqlite3 import Error
import urllib.request
import json


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def add_quote(conn,quote):
    sql = ''' INSERT INTO PositiveQuotes(Author,Quote)
                  VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, quote)
    conn.commit()
    return cur.lastrowid

def read_quotes(conn,quoteNums):
    sql = '''SELECT PQ.Author, PQ.quote FROM PositiveQuotes as PQ LIMIT {}'''.format(quoteNums)
    cur = conn.cursor()
    results = cur.execute(sql)
    rows = results.fetchall()
    return rows


def fetchQuotesAPI():
    contents = urllib.request.urlopen("https://gist.githubusercontent.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json").read()
    obj = json.loads(contents)
    return obj

def main():
    database = "C:\SQlite\positiveQuote.db"
    # create a database connection
    conn = create_connection(database)
    allQuotes = fetchQuotesAPI()
    for quoteObj in allQuotes['quotes']:
        print(quoteObj['quote'])
        print('Quote: {}, Author: {}'.format(quoteObj['quote'], quoteObj['author']))
    with conn:
        # create a new project
        for quoteObj in allQuotes['quotes']:
            quote = (quoteObj['author'],quoteObj['quote'] );
            quoteCreation = add_quote(conn, quote)


