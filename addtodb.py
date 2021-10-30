from connections.connection_database import *
from test import *
session.execute("use library")

class astradb:
    def __init__(self,id,book_info,book_name):
        self.id = id
        self.book_info = book_info
        self.book_name= book_name

    def adddata(self):
        add = "insert into books(book_id,book_info,book_name)values(%s,%s,%s)"
        session.execute(add,(self.id,self.book_info,self.book_name))

   