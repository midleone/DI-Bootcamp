import psycopg2
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            conn = psycopg2.connect(
                dbname='exday3',
                user='postgres',
                password='142321',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()
            cur.execute('INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)', (self.name, self.price))
            conn.commit()
            print(f"Item '{self.name}' added successfully.")
        except Exception as e:
            print(f"Error saving item: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def delete(self):
        try:
            conn = psycopg2.connect(
                dbname='exday3',
                user='postgres',
                password='142321',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()
            cur.execute('DELETE FROM Menu_Items WHERE item_name=%s', (self.name,))
            conn.commit()
            print(f"Item '{self.name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting item: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def update(self, new_name, new_price):
        try:
            conn = psycopg2.connect(
                dbname='exday3',
                user='postgres',
                password='142321',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()
            cur.execute('UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE item_name=%s', (new_name, new_price, self.name))
            conn.commit()
            print(f"Item '{self.name}' updated successfully.")
        except Exception as e:
            print(f"Error updating item: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

import psycopg2
#
# conn = psycopg2.connect(
#     dbname = 'exday3',
#     user= 'postgres',
#     password='142321',
#     host ='localhost',
#     port ='5432'
# )
# cur = conn.cursor()
# conn.commit()
# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def save(self):
#         try:
#             cur.execute('INSERT INTO Menu_Items (name, price) VALUES (%s, %s)', (self.name, self.price))
#             conn.commit()
#
#     # def delete(self):
#     #     try:
#     #         cur.execute('DELETE FROM Menu_Items WHERE name=%s', (self.name,))
#     #         conn.commit()
#
#
#     # def update(self, new_name, new_price):
#     #     try:
#     #         cur.execute('UPDATE Menu_Items SET name=%s, price=%s WHERE name=%s', (new_name, new_price, self.name))
#     #         conn.commit()
#
#
#
# # import psycopg2
# #
# # conn = psycopg2.connect(
# #     dbname = 'exday3',
# #     user= 'postgres',
# #     password='142321',
# #     host ='localhost',
# #     port ='5432'
# # )
# # cur = conn.cursor()
# # conn.commit()
# #
# # cur.execute('SELECT * FROM Menu_Items')
# # rows = cur.fetchall()
# #
# # for row in rows:
# #     print(row)
# # class MenuItem():
# #     def __init__(self,price, item):
# #
# # cur = conn.cursor()
# # cur.execute('INSERT INTO Menu_Items (name, price) VALUES (%s, %s)', (self.name, self.price))
# # conn.commit()
# #
# # cur = conn.cursor()
# # cur.execute('DELETE FROM Menu_Items WHERE name=%s', (self.name,))
# # conn.commit()
# #
# # cur = conn.cursor()
# # cur.execute('UPDATE Menu_Items SET name=%s, price=%s WHERE name=%s', (new_name, new_price, self.name))
# # conn.commit()
# #
# cur.close()
# conn.close()