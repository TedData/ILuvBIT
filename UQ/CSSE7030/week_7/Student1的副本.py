SQ_CLOSE = 1600
def close_to(p1,p2):
    x1,y1=p1
    x2,y2=p2 
    return (x1 - x2)**2 +(y1 -y2)**2<SQ_CLOSE

class Character(object):
    def __init__(self,x,y,name):
        self._x,self._y = x,y 
        self._name =name 
        self._inventory =[]
        self._holding = None 
    def get_name(self):
        return self._name 
    def get_position(self):
        return (self._x,self._y)
    def get_inventory(self):
        return self._inventory
    def get_holding(self):
        return self._holding
    def take(self,item):
        self._inventory.append(item)
        item.set_taken(True)
    def hold(self,index):
        if 0<= index<len(self._inventory):
            self._holding=self._inventory[index]
    def drop(self,index):
        if 0<=index<len(self._inventory):
            item=self._inventory.pop(index)
            x,y=self.get_position()
            item.set_position(x,y)
            item.set_taken(False)
            if item == self._holding:
                self._holding = None
    def move(self, dx,dy):
        self._x += dx
        self._y += dy 
    def __repr__(self):
        return 'Char name:{0} \nPos:{1}\nInventory:{2}'.format(self.get_name(),self.get_position(),self.get_inventory())

class Item(object):
    def __init__(self,x,y,name):
        self._x,self._y = x,y 
        self._name =name 
        self._taken=False
    def get_name(self):
        return self._name 
    def set_position(self,x,y):
        self._x,self._y = x,y
    def get_position(self):
        return (self._x,self._y)
    def set_taken(self,t ):
        self._taken=t 
    def is_taken(self):
        return self._taken
    def __str__(self):
        return self.get_name()
    def __repr__(self):
       return 'Item name:{0} \nPos:{1}\ntaken:{2}'.format(self.get_name(),self.get_position(),self.is_taken())
 










