import json

market_stuffs = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Vegetables": ["Carrot", "Broccoli", "Spinach"],
    "Dairy": ["Milk", "Cheese", "Yogurt"],
    "Grains": ["Rice", "Wheat", "Oats"],
    "Snacks": ["Chips", "Cookies", "Nuts"]
}

your_cart = {}

def cartinfo():
    print(f"\n🛒 Your Cart - {your_cart}")
    print("🧺 Here's what's in store today:")
    for category, items in market_stuffs.items():
        print(f"  🗂️  {category}: {', '.join(items)}")

print("🌟 Welcome, shopper extraordinaire, to the Grand Market of Wonders!")
print("\n🔍 What would you like to explore? Here are the categories:")
for category, items in market_stuffs.items():
    print(f"  🍱 {category}: {', '.join(items)}")

print("\n🧾 Your commands for a smooth ride:")
print("  ➕ To add:     add <item/category>")
print("  ➖ To remove:  remove <item>")
print("  ✅ To finish:  done")

def modify_cart():
    while True:
        user_input = input("\n💬 Your command: ").strip()

        if user_input.lower() == "done":
            break

        parts = user_input.split(maxsplit=1)
        if len(parts) != 2:
            print("⚠️ Try 'add <item>' or 'remove <item>'. I'm not that psychic yet.")
            continue

        action, item = parts[0].lower(), parts[1].title()

        if action == "add":
            if item in market_stuffs:
                for product in market_stuffs[item]:
                    product = product.title()
                    your_cart[product] = your_cart.get(product, 0) + 1
                print(f"✅ All {item} items added to your cart. Flavor explosion imminent!")
                cartinfo()
            elif item in your_cart:
                print(f"⚠️ {item} is already chillin' in your cart.")
                while True:
                    response = input("😎 Add more? (yes/no): ").strip().lower()
                    if response == "yes":
                        while True:
                            try:
                                qty = int(input(f"🍽️ How many {item} would you like? "))
                                if qty >= 0:
                                    break
                                else:
                                    print("⚠️ Quantity must be a positive number. Try again.")
                            except ValueError:
                                print("🚫 That’s not a number I can count. Please enter a valid integer.")                       
                        your_cart[item] += qty
                        print(f"🛒 Added {qty} more {item}. This better be your favorite!")
                        cartinfo()
                        break
                    elif response == "no":
                        print(f"ℹ️Hmmm meanie, {item} not added again.")
                        cartinfo()
                        break
                    else:
                        print("⚠️ I need a yes or no to proceed, Don't play around.")
            elif any(item == v.title() for lst in market_stuffs.values() for v in lst):
                while True:
                     try:
                         qty = int(input(f"🍽️ How many {item} would you like? "))
                         if qty >= 0:
                             break
                         else:
                             print("⚠️ Quantity must be a positive number. Try again.")
                     except ValueError:
                         print("🚫 That’s not a number I can count. Please enter a valid integer.")
                your_cart[item] = your_cart.get(item, 0) + qty
                print(f"✅ {qty}x {item} now belongs to your digital basket.")
                cartinfo()
            else:
                print(f"\n❌ '{item}' not found in the market. Ghost produce maybe?")
                cartinfo()

        elif action == "remove":
            if item in your_cart:
                while True:
                    qty = int(input(f"🗑️ How many {item} to remove? "))
                    if qty <= your_cart[item]:
                        your_cart[item] -= qty
                        if your_cart[item] == 0:
                            del your_cart[item]
                        print(f"🧹 Poof! Removed {qty}x {item} from your cart.")
                        cartinfo()
                        break
                    else:
                        print(f"⚠️ You only have {your_cart[item]} {item}. Try again, savvy shopper.")
            else:
                print(f"⚠️ {item} isn't even in your cart. Nice try.")
        else:
            print("⚠️ That action isn't on our menu. Try add/remove/done.")

def summary():
    print("\n📦 Final Cart Summary:")
    for item, qty in your_cart.items():
        print(f"🔸 {item}: {qty}x")
    print(f"\n📊 Unique items: {len(your_cart)}")
    print(f"🧮 Total quantity: {sum(your_cart.values())}")

def checkout():
    if your_cart:
        receipt = {
            "Products": your_cart,
            "Unique Items": len(your_cart),
            "Total Quantity": sum(your_cart.values()),
            "Message": "Thanks for shopping at the Market!"
        }
        print("\n🧾 Final Receipt:")
        for item, qty in your_cart.items():
            print(f"{item} : {qty}")
        print("\n🛒 Your order has been placed successfully!")
        with open("order_receipt.json", "w") as file:
            json.dump(receipt, file, indent=2)
        print("\n📁 A copy of your receipt is waiting in ")
    else:
        print("🛒 You didn't pick up anything. Are you on a window-shopping diet?")

def modify():
    while True:
        response = input("\n🔁 Would you like to modify your cart? (yes/no): ").strip().lower()
        if response == "yes":
            print("✨ Back to the shop floor!")
            modify_cart()
        elif response == "no":
            print("📤 Proceeding to checkout...")
            checkout()
            print("🎉 Thanks for shopping with us — come back hungry!")
            break
        else:
            print("⚠️ That didn't compute. Say 'yes' or 'no' like a proper market legend.")


modify_cart()
summary()
modify()