
class Order:
    def __init__(self, price, quantity , buy_sell, nb_id ):
   
        self.quantity = quantity
        self.buy_sell = buy_sell
        self.price = price
        self.nb_id = nb_id
       
    def __setitem__(self,i,val,key=None):
        assert i==1
        if i==1:
            if type(val)==type(self.quantity):
                self.quantity=val
       
    def __str__(self):
        if(self.buy_sell ==0):
            return "    BUY " + str(self.quantity) + "@" + str(self.price) + " id=" + str(self.nb_id)
        else :
            return "    SELL " + str(self.quantity) + "@" + str(self.price) + " id=" + str(self.nb_id)

       
class Book:
    def __init__(self, name):
        self.name = name
        self.numberorder = 0
        self.matriceorder = []
        self.executeorder = []
       
    def insert_buy(self,number,price):
        print("--------------------------------")
        self.numberorder = self.numberorder +1
        noworder = Order(price,number,0, self.numberorder)
        
       
        if(self.matriceorder == []):
            self.matriceorder.append(noworder)
        else:
            for i in range(len(self.matriceorder)):
                if(noworder.price> self.matriceorder[i].price):
                    self.matriceorder.insert(i,noworder)
                    break
                elif i==len(self.matriceorder)-1 :
                    self.matriceorder.append(noworder)
        self.modifications()
        print("---Insert BUY " + str(noworder.quantity) + "@" + str(noworder.price) + "  ID =" + str(noworder.nb_id) +  " on " + self.name)
        for i in range(len(self.executeorder)):
            print(self.executeorder[i])
        self.executeorder = []
        print( "Book on " + self.name)
        print(self)
           
    def insert_sell(self,number,price):
        print("--------------------------------")
        self.numberorder = self.numberorder +1
        noworder = Order(price,number,1, self.numberorder)
       
        if(self.matriceorder == []):
            self.matriceorder.append(noworder)
        else:
            for i in range(len(self.matriceorder)):
                if(noworder.price>= self.matriceorder[i].price):
                    self.matriceorder.insert(i,noworder)
                    break
                #if(self.matriceorder[i].buy_sell==0):
                 #    self.matriceorder.insert(i,noworder)
                  #   break
                elif i==len(self.matriceorder)-1 :
                    self.matriceorder.append(noworder)
        print("---Insert SELL " + str(noworder.quantity) + "@" + str(noworder.price) + "  ID =" + str(noworder.nb_id) +  " on " + self.name)
        self.modifications()
        for i in range(len(self.executeorder)):
            print(self.executeorder[i])
        self.executeorder = []
        print( "Book on " + self.name)
        print(self)
   
    def modifications(self):
        if(len(self.matriceorder)>1):
            for i in range(len(self.matriceorder)-1):
                if(i<len(self.matriceorder)-1):
                    if(self.matriceorder[i].buy_sell == 0 and self.matriceorder[i].buy_sell != self.matriceorder[i+1].buy_sell):
                        if(self.matriceorder[i].quantity >= self.matriceorder[i+1].quantity ):
                            self.matriceorder[i].quantity -= self.matriceorder[i+1].quantity
                            self.executeorder.append("Excecute "+str(self.matriceorder[i+1].quantity) + " at " + str(self.matriceorder[i].price) +" on "+self.name)
                            self.matriceorder.remove(self.matriceorder[i+1])
                        elif(self.matriceorder[i].quantity < self.matriceorder[i+1].quantity ):
                            self.matriceorder[i+1].quantity -= self.matriceorder[i].quantity
                            self.executeorder.append("Excecute "+str(self.matriceorder[i].quantity)+" at " + str(self.matriceorder[i].price) +" on "+self.name)
                            self.matriceorder.remove(self.matriceorder[i])
                            self.modifications()
                    elif(self.matriceorder[i+1].buy_sell == 0 and self.matriceorder[i].buy_sell != self.matriceorder[i+1].buy_sell and self.matriceorder[i].price== self.matriceorder[i+1].price):
                        if(self.matriceorder[i+1].quantity >= self.matriceorder[i].quantity ):
                            self.matriceorder[i+1].quantity -= self.matriceorder[i].quantity
                            self.executeorder.append("Excecute "+str(self.matriceorder[i].quantity)+" at " + str(self.matriceorder[i].price) +" on "+self.name)
                            self.matriceorder.remove(self.matriceorder[i])
                        elif(self.matriceorder[i+1].quantity < self.matriceorder[i].quantity ):
                            self.matriceorder[i].quantity -= self.matriceorder[i+1].quantity
                            self.executeorder.append("Excecute "+str(self.matriceorder[i+1].quantity)+" at " + str(self.matriceorder[i].price) +" on "+self.name)
                            self.matriceorder.remove(self.matriceorder[i+1])
                            self.modifications()
                        
    def __str__(self):
        res =""
        for i in range(len(self.matriceorder)):
            res += str(self.matriceorder[i]) + "\n"
        return res
