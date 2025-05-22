class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f'Product Name: {self.name}; Price: {self.price}')

class Cart:
    def __init__(self):
        self.items =  []
    def add_product(self,product):
        self.items.append(product)
        print(f'Product added to cart: {product.name}')
    
    def remove_product(self, product):
        for p in self.items:
            if p.name == product.name:
                self.items.remove(p)
                print(f'product removes from the cart: {product.name}')
            return
                
        self.items.remove(p)


    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print('Your cart contains:')
        for p in self.items:
            p.display_info()

    def checkout(self):
        total = sum(p.price for p in self.items)
        print(f'Total amount to pay: {total}')



p1 = Product('Laptop', 50000)
p2 = Product('Ps5 Gaming Console', 120000)
p3 = Product('Sony LED', 800000)
p4 = Product('Bike', 8200000)

# creating a cart obj
cart = Cart()
cart.add_product(p1)

cart.add_product(p2)

cart.add_product(p3)

cart.add_product(p4)

#show the cart 
cart.show_cart()

#total amount to pay
cart.checkout()


#removing a product
cart.remove_product(p2)
cart.show_cart()
cart.checkout()

            
        