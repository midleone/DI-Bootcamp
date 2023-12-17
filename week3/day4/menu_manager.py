class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            conn = psycopg2.connect(
                dbname='exday3',
                user='postgres',
                password='142321',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()
            cur.execute('SELECT * FROM Menu_Items WHERE item_name=%s', (item_name,))
            item = cur.fetchone()
            return item if item else None
        except Exception as e:
            print(f"Error getting item by name: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    @classmethod
    def all_items(cls):
        try:
            conn = psycopg2.connect(
                dbname='exday3',
                user='postgres',
                password='142321',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()
            cur.execute('SELECT * FROM Menu_Items')
            items = cur.fetchall()
            return items
        except Exception as e:
            print(f"Error getting all items: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()