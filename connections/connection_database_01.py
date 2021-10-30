from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'I:/ashrith/python/Library Mangement application/connections/secure-connect-library-management.zip'
}
auth_provider = PlainTextAuthProvider('sDBPmTAyaABQmABZhoIZeTfs', 'XwFQBZwDgLMe2pgA0Onr1ipCxNo9kqfl_BqmQhd2LKvb3dlBciIeTDq2_ZwI3HOf5gesbsMQlrqrf4pJHWAjK2.WS.2D7CY77dDjY9jc-2K-2xkNdZHM8lZtINMZ-pTP')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

#row = session.execute("Use library")
#row1 = session.execute("SELECT * FROM books")

#bookid= input("please enter bookid")
#bookidnum=int(bookid)
#bookinfo= input("please enter booinfo")
#bookname= input("please enter bookname")
#insert_table="insert into books(book_id,book_info,book_name)values(%s,%s,%s)"
#session.execute(insert_table,(bookidnum,bookinfo,bookname))
