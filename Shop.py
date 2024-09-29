# Shopping Cart
# -------------

class Shop:
    cart = {}
    bill = 0
    def showcart(this):
        print('\n\nYour cart is')
        print('------------')
        for i in this.cart:
            print(i, this.cart[i])
    
    def clearCart(this):
        this.cart = dict()
        print('Successfully clean your cart')
    
    def calBill(this, items):
        print('\n\nYour Bill')
        print('---------')
        bill = 0
        for i in this.cart:
            if i == 'ball':
                bill += (this.cart[i]*items[i])
                if items[i]<10:
                    bill -= (bill*5//100)
            elif i == 'bat':
                bill += (this.cart[i]*items[i])
                if items[i]<10:
                    bill -= (bill*5//100)
            elif i == 'stump':
                bill += (this.cart[i]*items[i])
                if items[i]<10:
                    bill -= (bill*5//100)
            elif i == 'hat':
                bill += (this.cart[i]*items[i])
                if items[i]<10:
                    bill -= (bill*5//100)
            else:
                bill+=(this.cart[i]*items[i])
                if items[i]<10:
                    bill -= (bill*5//100)
        print('Total bill -', bill)
        n = (bill*8//100)
        bill += n
        print('Tax      - -',n)
        print('Your final Bill including tax', bill,)
    
    def addItem(this, item, quan):
        this.cart[item.lower()] = quan
        
    
    def removeItem(this, item):
        try:
            this.cart.pop(item)
        except:
            return 1
    
    def ModQuantity(this, item, quan):
        if quan > 10:
            print('\nItems should add below 10 quantity\n')
            return 1
        this.cart[item] = quan
    
    def cartNotExistError(this, item):
        try:
            if this.cart[item]:
                return False
            return False
        except:
            return True
        
    

user1 = Shop();
menu = "1.Add item to cart\n2.Remove item from cart\n3.Modify item quantity\n4.Calculate total bill\n5.Clear cart\n6.Exit program\n\nEnter your index number(1-6) of your operation: "
print(menu)
items = {'ball':20, 'bat':25, 'stump':30, 'sat':35, 'shirt':40}

option = int(input())

while not (option>0 and option <7):
    option = int(input('Select number 1-6 range as per index: '))

def showItems(items):
    for i in items: print(i,'-',items[i])

def itemError(items,item):
    try:
        if items[item]:
            return False
        return False
    except:
        return True

def quanError(quan):
    if quan>0 and quan<10:
        return False
    return True

while 1:
    if option == 1:
        showItems(items);
        item = input('Which item do you want: ').lower()
        # print(items)
        while itemError(items,item):
            print('\n\nYour item is doesnot exist.')
            showItems(items);
            item = input('Please add item which are existing: ').lower()
            
        
        
        quan = int(input('How many '+item+'s(1 to 10) do you want to add cart: '))
        while quanError(quan):
            quan = int(input('Enter above 0 and below 10 quantity: '))
        
        user1.addItem(item, quan)
        
        user1.showcart()
    elif option == 2:
        print('Select item to remove')
        user1.showcart()
        item = input('Enter your cart item: ')
        while user1.removeItem(item) == 1:
            item = input('Enter your cart item: ')
            user1.showcart()
        
        user1.showcart()
    elif option == 3:
        print('Select item to Modify')
        user1.showcart()
        item = input('Enter which item: ')
        while user1.removeItem(item) == 1:
            item = input('Enter your cart item: ')
            user1.showcart()
        quan = int(input('New Quantity of the item', item,': '))
        while quanError(quan):
            quan = int(input('Enter above 0 and below 10 quantity: '))
        ret = user1.ModQuantity(item, quan)
        if ret == 1:
            continue
        
        user1.showcart()
    elif option == 4:
        user1.calBill(items)
    elif option == 5:
        user1.clearCart()
    elif option == 6:
        print('Thank you for shop..! Have a nice day :)')
        break
    
    menu = "\n\n\n1.Add item to cart\n2.Remove item from cart\n3.Modify item quantity\n4.Calculate total bill\n5.Clear cart\n6.Exit program\n\nEnter your index number(1-6) of your operation: "
    print(menu)
    option = int(input())
    while not (option>0 and option <7):
        option = int(input('Select number 1-6 range as per index: '))
