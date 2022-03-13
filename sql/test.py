# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:53:19 2022

@author: bobga
"""

import sqlite3
class change:
  def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
        self.conn = None
        self.cursor = None
change.conn = sqlite3.connect('my10.db')
change.cursor = change.conn.cursor()
change.cursor.execute("UPDATE Healthdata SET tempreture = 36.6 WHERE ID = 2;")
change.cursor.execute("UPDATE Healthdata SET time = '6.MAR.2022' WHERE ID = 2;")
change.conn.commit()
change.cursor.execute(
        "select * from Healthdata"
        )
print(change.cursor.fetchall())
change.conn.close()
