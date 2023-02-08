import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("INSERT INTO users (full_name, email, password) VALUES (?, ?,?)",
#             ('anu', 'anu@gmail.com', 'anu')
#             )
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)",
#             ('oranges', 'fruit', '75 Rs.','img/goods_img/1.jpg')
#             )
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)",('apples', 'fruit', '60 Rs.','img/goods_img/3.jpg'))
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)", ('brocoli', 'vegetable', '75 Rs.','img/goods_img/2.jpg'))
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)",('banana', 'fruit', '75 Rs.','img/goods_img/5.jpg'))    
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)",('strawberry', 'fruit', '75 Rs.','img/goods_img/4.jpg'))
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)",('pumpkin', 'vegetable', '75 Rs.','img/goods_img/6.jpg'))
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)",('tomato', 'vegetable', '75 Rs.','img/goods_img/7.jpg'))
# cur.execute("INSERT INTO products (product_name, product_type, price,file_name) VALUES (?, ?, ?, ?)", ('peach', 'fruit', '75 Rs.','img/goods_img/8.jpg'))
# cur.execute("INSERT INTO cart (user_id, item_id_price,image,quantity) VALUES (?, ?, ?, ?)",
#             ('oranges', '75 Rs.','img/goods_img/1.jpg',1)
#             )
# cur.execute("INSERT INTO cart (product, product_price,image,quantity) VALUES (?, ?, ?, ?)",
#             ('apples', '75 Rs.','img/goods_img/3.jpg',1)
#             )
# cur.execute("INSERT INTO cart (product, product_price,image,quantity) VALUES (?, ?, ?, ?)",
#             ('banana', '75 Rs.','img/goods_img/5.jpg',1)
#             )    
            

connection.commit()
connection.close()