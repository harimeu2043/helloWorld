class Store:
    def __init__(self,name):
        self.name=name
        self.items=[]
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        item={'name':name,'price':price}
        self.items.append(item)
        
        
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        
        return sum([item['price'] for item in self.items])
    
s1=Store("Hari")
s1.add_item('Patato',100)
print(s1.items)
s1.add_item('sita', 150)
s1.add_item('hanuman', 200)

print(s1.items)

print(s1.stock_price())
