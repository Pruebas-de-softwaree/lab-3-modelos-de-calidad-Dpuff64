# Available products (id, name, price)
products = {
    1: {"name": "Laptop", "price": 15000},
    2: {"name": "Mouse", "price": 300},
    3: {"name": "Keyboard", "price": 800},
    4: {"name": "Monitor", "price": 4500}
}

# Shopping cart (list of product IDs)
cart = []

def show_products():
    print("\n=== Available Products ===")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ${info['price']}")

def add_to_cart(pid):
    if pid in products:
        cart.append(pid)
        print(f"{products[pid]['name']} added to cart.")
    else:
        print("Error: Product does not exist.")

def view_cart():
    if not cart:
        print("\nCart is empty")
        return
    
    print("\n=== Shopping Cart ===")
    total = 0
    for i, pid in enumerate(cart, 1):
        product = products[pid]
        print(f"{i}. {product['name']} - ${product['price']}")
        total += product["price"]
    print(f"Total: ${total}")

def checkout():
    if not cart:
        print("\nCannot checkout: the cart is empty.")
        return
    
    view_cart()
    print("Checkout completed. Thank you for your purchase!")
    cart.clear()

def menu():
    while True:
        print("\nOptions: products, add, cart, checkout, exit")
        option = input("Choose an option: ")

        if option == "products":
            show_products()
        elif option == "add":
            try:
                pid = int(input("Enter the product ID: "))
                add_to_cart(pid)
            except ValueError:
                print("Error: ID must be numeric.")
        elif option == "cart":
            view_cart()
        elif option == "checkout":
            checkout()
        elif option == "exit":
            print("Exiting system...")
            break
        else:
            print("Invalid option.")

import time

def performance_test():
    start = time.time()  
    
    add_to_cart(1)  
    
    end = time.time() 
    elapsed = end - start
    
    print(f"Tiempo de respuesta: {elapsed:.4f} segundos")
    if elapsed < 2:
        print("✅ Cumple con RNF1 (menor a 2 segundos)")
    else:
        print("❌ No cumple con RNF1 (mayor a 2 segundos)")

if __name__ == "__main__":
    performance_test()
