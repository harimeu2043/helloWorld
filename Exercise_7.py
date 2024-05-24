class Store:
    def __init__ (self, name):
        self.name=name
        self.items=[]
    
    def add_items(self, name, price):
        self.items.append({'name':name, 'price':price
        })

    def stock_price(self):
        total=0
        for item in self.items:
            total+=item['price']
        return total
    @classmethod
    def franchise(cls, store):
        new_store=cls(store.name+" -franchise")


    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))
    





