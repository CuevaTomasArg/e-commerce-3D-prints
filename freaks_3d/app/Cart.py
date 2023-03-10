class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart
    
    def add(self,product):
        id = str(product.id)
        if id not in self.cart.keys():
            self.cart[id] ={
                "product_id":product.id,
                "name":product.name,
                "category":product.category,
                "accumulated":product.price,
                "amount":1,
                "image":product.image.url,
            }
        else:
            self.cart[id]["amount"] += 1
            self.cart[id]["accumulated"] += product.price
        self.save_cart()
    
    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def delete(self,product):
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.save_cart()
    
    def subtract(self,product):
        id = str(product.id)
        if id in self.cart.keys():
            self.cart[id]["accumulated"] -= product.price
            self.cart[id]["amount"] -= 1
            if self.cart[id]["amount"] <= 0:
                self.delete(product)
            self.save_cart()
    
    def clean_up(self):
        self.session["cart"] = {}
        self.session.modified = True