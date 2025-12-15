from database.db import get_connection
from models.product import Product

class CatalogService:

    def add_product(self, product: Product):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO products (name, category, price)
            VALUES (?, ?, ?)
        """, (product.name, product.category, product.price))
        conn.commit()
        conn.close()

    def show_products(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        conn.close()
