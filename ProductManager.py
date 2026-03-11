class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    def list_products(self):
        return self.products

    # This method calculates discount price for a product given the original price and discount percentage
    def calculateDiscount(self, price, discount_percent):
        return price - (price * discount_percent / 100)