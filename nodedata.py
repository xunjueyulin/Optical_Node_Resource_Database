#!/usr/bin/env python

import sqlite3
connection = sqlite3.connect('optical_node_data.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE optical_nodes(
				  id             INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
				  device_type    TEXT   NOT NULL,
				  headend        TEXT   NOT NULL,
				  device_address CHAR(50)   NOT NULL,
				  name           TEXT   NOT NULL,
				  signalling_time DATE   NOT NULL,
				  project_number TEXT   NOT NULL,
				  device_state   TEXT   NOT NULL,
				  manager        TEXT   NOT NULL );""")
				  
connection.commit()
connection.close()