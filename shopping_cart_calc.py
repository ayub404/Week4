print('\nSHOPPING CART CALCULATOR')
print('=====================================')

def calculate_item_total(quantity, unit_price):

    return quantity * unit_price


def apply_bulk_discount(total, quantity):
    
    if quantity >= 10:
        return total * 0.1
    elif quantity >= 5:
        return total * 0.05
    else:
        return 0
    

def calculate_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)

def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50

def process_order(item_name, quantity, unit_price, tax_rate):
    # print('Shopping cart calculator')
    # print('=====================================')
    print(f'Order receipt for: {item_name}')
    print(f'Quantity: {quantity} @ ${unit_price:.2f} each')

    item_total = calculate_item_total(quantity, unit_price)
    print(f'Item total: ${item_total:.2f}')

    discount = apply_bulk_discount(item_total, quantity)
    print(f'Bulk Discount: -${discount:.2f}')

    subtotal = item_total - discount
    print(f'Subtotal: ${subtotal:.2f}')
    tax = calculate_tax(subtotal, tax_rate)
    print(f'Tax (8%):  ${tax:.2f}')

    final_total = subtotal + tax
    print(f'Final Total: ${final_total:.2f}')

    
    if not is_eligible_for_free_shipping(subtotal):
        shipping = 50 - subtotal
        print(f'Need ${shipping:.2f} more for free shipping!')    
    else:
        return 'Eligible for free shipping'
    print('-'*45)




process_order('Notebooks', 12, 3.50, 8)
process_order('Pens', 6, 1.25, 8)
process_order('Paper', 3, 4.99, 8)



