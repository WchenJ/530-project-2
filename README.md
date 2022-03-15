530-project-2
EC530 Project2

Branches contain main branch and device branches, which will be merged when all work of that specific branch is done. Main branch has finished testing.

Database

Data base include five tables: user, permission, device, divrec, Healthdata. And the structure and data fields could be found at

#530 2.jpg.

All data could be attribute to a specific user by cascading foreign key conatraint between several kinds of id in each table.

error conditions and codes:

1 SQL error or missing database

2 Internal error in SQLite

3 Access denied

4 database is locked

5 A table in the database is locked

6 Attempt to write a readonly database

7 Operation terminated by sqlite3_interrupt()

Temperature, blood pressure, pulse, oximeter, weight and Glucometer is included as well as primary information of users and devices. Unit test has been done in

#./Djtest/test0/test1.py.

The example of sending data is shown in

#./sql/test.py

and should be run on local in python, which will update data in the Healthdata table.

Restful system is developed via Django.

The API contains the functions of login, a restful port with the function of GET PUT DELETE POST of the existing database and get json response. All basic and GET function could be easily entered by Microsoft edge and the function of POST, PUT, DELETE are tested on postman. all results could be see in the

#./picture .

test for API is done in

#./Djtest/test0/test0.py.



I‘ll prefer sql database for the chat module for seceral reasons:

First, the content of the chatting information is diverse, there may be words, pictures, syntax that ia not easy to forsee

and considered at the time when structure is designed, which is ecpected to ruled for a long time.

Second, the demand of constrain are not that strict and most information stored are based on timeflow, the rarely simple linear structure.

Chat Module

The user of chat moudle needs to receive the message from the talking parterners, send message to the parterners and store the records.

The Module support sending, receiving and storing based on Sqlite3. A database will be created for a chatroom .  Parterners can send and check the talking content.

the test documents could be seen at

#./picture
