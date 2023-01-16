import psycopg2
import os

conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user='gaurav',
        password='gaurav')

curr = conn.cursor();

'''
login table to store user credentials.
'''
curr.execute('DROP TABLE IF EXISTS login;');
curr.execute('CREATE TABLE login(login_id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'age int NOT NULL,'
                                 'college varchar (150) NOT NULL,'
                                 'roll_no int NOT NULL,'
                                 'login_date date DEFAULT CURRENT_TIMESTAMP);'
             )

'''
calender table to store calender data.
'''
curr.execute("DROP TABLE IF EXISTS calendar;");
curr.execute('CREATE TABLE calendar(event_id serial PRIMARY KEY,'
                                 'summary varchar(150) NOT NULL,'
                                 'kind varchar (150) NOT NULL,'
                                 'timezone varchar (10) NOT NULL,'
                                 'calender_date date DEFAULT CURRENT_TIMESTAMP);'
             )


conn.commit()
