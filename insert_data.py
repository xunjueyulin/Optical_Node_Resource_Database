# -*-coding:utf-8 -*-


# 导入sqlite3模块
import sqlite3

# 连接到数据库
# 数据库文件是“DataBase”
# 如果文件不存在，会自动在当前目录创建，后期需修改到目标路径
conn = sqlite3.connect('DataBase1.db')
print("Opened database successfully")
# 创建一个游标cursor

cursor = conn.cursor()

# 插入数据,第一次尝试，后期应注释掉，思考如何从csv格式批量导入
cursor.execute("INSERT INTO Optical_workstation (id,workstation_name,address,using_state,attached_to_cmts,\
          downlink_MAC_domain,upstream_channel,node_number,downstream_wiring_number,upstream_wiring_number,\
          ODF_fiber_core_address,project_number)\
          VALUES (NULL,'越秀方圆时光12楼' , '广东省广州市越秀区珠光街道东沙角路越秀方圆时光12楼弱电井内' ,\
          1,'DZZ-4.M.C10G','2\\4','11\\3','010112090210079','93','78','暂缺',\
          'SZ-BB-XJ-JRW-201606-046')");

# 关闭cursor
cursor.close()

# 提交事务
conn.commit()
print("Records created successfully")

# 关闭连接
conn.close()