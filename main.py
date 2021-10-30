from connections.connection_database import *

session.execute("use library")

user_dec=input("""hello please register newbooks through below options
1 - add books
2- delete books
3- update books""")
#add data module

def add_data():
    id = input("Enter id of  your book")
    idnum=int(id)
    info = input("Enter info of your book")
    name= input("Enter name of your book")
    add = "insert into books(book_id,book_info,book_name)values(%s,%s,%s)"
    session.execute(add,(idnum,info,name))

def delete_data():
    print_table= session.execute("select * from books")
    for i in print_table:
        print(i)
    user_input= input(""" Please select option to delete data
    a - id
    b-cloumn name and id
    """)
    if  user_input=="a":
        id = input("Enter id of  your book")
        idnum=int(id)
        delete = f"delete from books where book_id={id}"
        session.execute(delete)
        
    elif user_input== "b":
        id = input("Enter id of  your book")
        idnum=int(id)
        column_name = input("Enter Cloumn name")
        delete= f"delete {column_name} from books where book_id={idnum}"
        session.execute(delete)
    
if user_dec=="1":
    add_data()
elif user_dec=="2":
    delete_data()
elif user_dec=="3":
    update_data()

