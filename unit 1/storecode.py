print("🌷Welcome to Aesthetic Flower Shop!🌷 \n Options:")
products=["1. Tulips", "2. Roses", "3. Sunflowers", "4. Daisies", "5. Lillies", "6. Orchids", "(All are $5 each)"]
price=[5, 5, 5, 5, 5, 5]
for product in products:
    print(product)
answer="Yes" or "yes"
total=0
while answer=="Yes" or answer=="yes":
    flower=int(input("Which flower do you want to buy? (Choose the number next to the flower on the list)"))
    amount=float(input("How many do you want to buy?"))
    print("You want", products[flower-1], "for $", price[flower-1])
    subtotal=amount*price[flower-1]
    print("The quantity is", amount)
    print("The unit price is", price[flower-1])
    membership=input("Do you have a membership?")
    if membership=="Yes" or membership=="yes":
        subtotal=subtotal*0.8
        print("You get a 20 percent discount")
    else:
        print("You don't get a discount")
    answer=input("Do you want to buy again?")
    total=subtotal+total
print("Your total is $", total)