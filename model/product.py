from model.db_manager import DbManager


class Product(DbManager):

    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def get_all_products(cls):
        query = "SELECT * FROM products"
        rows = cls.execute_query(query, values_tuple=None, commit=False)
        return [cls(*row) for row in rows]

    @classmethod
    def add_product(cls, name, description, price):
        product = cls("id", name, description, price)
        query = "INSERT INTO products (Name, Description, Price) VALUES (?, ?, ?)"
        values = (product.name, product.description, product.price)
        cls.execute_query(query, values)

    @classmethod
    def delete_product(cls, id):
        query = "DELETE FROM products WHERE ID = {}".format(id)
        cls.execute_query(query)