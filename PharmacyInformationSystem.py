class Pharmacy:
    def __init__(self):
        self.inventory = {}

    def addProduct(self, productName, price, quantity):
        if productName not in self.inventory:
            self.inventory[productName] = {"Product" : productName, "Price" : price, "Quantity" : quantity}

        else:
            print("'" + productName + "' already added to the inventory")

    def displayProduct(self):
        print("\nCURRENT INVENTORY")

        for product, details in self.inventory.items():
            print(f"\nProduct : {product} \nPrice : P {details["Price"]} \nQuantity : {details["Quantity"]}\n")


pharmacySystem = Pharmacy()

print("Welcome to Bacani`s Pharmacy Information System!")
input("Enter your name to start : ")

while True:
    productName = str(input("\nEnter the name of the product to be added : "))
    price = int(input("Enter the price of the product to be added  P : "))
    quantity = int(input("Enter the quantity of the product to be added : "))

    pharmacySystem.addProduct(productName, price, quantity)

    userAddAgain = str(input("Do you want to add more products to the inventory (y/n?: "))

    if userAddAgain != "y":
        break

pharmacySystem.displayProduct()

        





