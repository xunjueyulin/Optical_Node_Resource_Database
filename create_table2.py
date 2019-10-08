# -*-coding:utf-8-*-


# 导入sqlite3模块,os模块
import sqlite3
import os

# 连接到数据库
# 数据库文件是“DataBase”
# 如果文件不存在，会自动在当前目录创建，后期需修改到目标路径
conn = sqlite3.connect('DataBase1.db')
print("Opened database successfully")
# 创建一个游标cursor

cursor = conn.cursor()

# 执行SQL语句创建光机表，如果表格不存在就创建，使用create table if not exists语句，
# 外键目前未开启，project_number项、attached_to_cmts项应该开启外键约束，
# using_state项应该开启0-1之间整数的约束
# 这里id暂时设为自增主键，使用autoincrement语句，后期考虑把node_number设为主键

cursor.execute('''CREATE TABLE IF NOT EXISTS Optical_workstation
            (id                   INTEGER PRIMARY KEY    AUTOINCREMENT,
            workstation_name          VARCHAR(20)    NOT NULL,
            address                   VARCHAR(60)    NOT NULL,
            using_state               INTEGER ,
            attached_to_cmts          NOT NULL,
            downlink_MAC_domain       VARCHAR(10)    NOT NULL,
            upstream_channel          VARCHAR(10)    NOT NULL,
            node_number               VARCHAR(20)    NOT NULL,
            downstream_wiring_number  VARCHAR(10)    NOT NULL,
            upstream_wiring_number    VARCHAR(10)    NOT NULL,
            ODF_fiber_core_address    VARCHAR(20)    NOT NULL,
            project_number            VARCHAR(30)    NOT NULL,
            workstation_remarks       VARCHAR(30));''')
print("table Optical_workstation created successfully")
# 执行SQL语句创建工程信息表

# 执行SQL语句创建结算表

# 执行SQL语句创建审计表


# 关闭cursor
cursor.close()

# 提交事务
conn.commit()

# 关闭连接
conn.close()