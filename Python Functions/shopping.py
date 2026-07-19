shop = [{'item':'flour', 'price':100, 'inventory':250},
        {'item':'sugar', 'price':180, 'inventory':500},
        {'item':'rice', 'price':300, 'inventory':500},
        {'item':'oil', 'price':500, 'inventory':1000},
        {'item':'ghee', 'price':500, 'inventory':500},
        {'item':'tea', 'price':400, 'inventory':100},
        {'item':'soap', 'price':200, 'inventory':50},
        {'item':'salt', 'price':50, 'inventory':100}]

def shopping():
    cart = {}
    while True:
        item_name = input('Enter the item you want to buy or (press "q" to exit)').lower()
        if item_name == 'q':
            print('Thank you for shopping')
            break
        found = False
        for s in shop:
            if s ['item'] == item_name:
                found = True
                if item_name in cart.keys():
                    print('Alreadt added in cart')
                    break
                print(f"{item_name} {s['price']} ka hy")
                quantity = float(input('Kitna Chaye?'))
                if s ['inventory'] >= quantity:
                    cart [item_name] = s['price'] * quantity
                    s ['inventory'] -= quantity
                else:
                    print(f'{item_name} itna nahi hai')
                break
        if not found:
            print(f'{item_name} not available')
    generate_bill(cart)

def generate_bill(cart):
    for item, price in cart.items():
        print(f'''
        {item} : {price}
        ''')
    gross_total = total(cart)
    discount = apply_discount(gross_total)
    tax = tax_apply(gross_total)
    payable_amount = gross_total - discount + tax
    print(f'''
    Total Amount: {gross_total}
    Applied Discount: {discount}
    Tax Applied: {tax}
    Amount Payable: {payable_amount}
    ''')

def total(cart):
    total_amt = sum(cart.values())
    return total_amt

def apply_discount(total_amt):
    if total_amt>= 50000:
        discount = total_amt*.10
    elif total_amt>= 25000:
        discount = total_amt*.05
    elif total_amt>= 10000:
        discount = total_amt*.01
    else:
        discount = total_amt*0
    return discount

def tax_apply(total_amt):
    if total_amt>= 50000:
        tax = total_amt*.05
    elif total_amt>= 25000:
        tax = total_amt*.025
    elif total_amt>= 10000:
        tax = total_amt*.001
    else:
        tax = total_amt*0
    return tax