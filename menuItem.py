class MenuItem:
    """
    The menu item class would ideally be a single item as part of a list for an "order".
    @params
    - size = this is the size of the menu item, e.g. medium, large
    - cost = this is the cost of the item, it would be driven by the system taking the input probably
    - specialInstructions = any instructions, such as sauce on the side, well done, etc.
    """
    def __init__(self, size, cost, specialInstructions=None):
        self.size = size # e.g. large, xl,
        self.cost = cost
        self.specialInstructions = specialInstructions
        
    def applyCoupon(self, discount):
        print('Applying Discount of {}'.format(discount))
        self.cost -= discount
        
    def addExtras(self, extraCost):
        print('Applying Extra cost of {}'.format(extraCost))
        self.cost += extraCost
        
class Drink(MenuItem):
    """
    The drink class inherits the MenuItem class.
    @params
    - brandName = e.g. Coke, Diet Coke, Pepsi
    - extraFlavor = Vanilla, Chocolate, Cherry
    """
    def __init__(self, brandName, extraFlavor, *args, **kwargs):
        self.brandName = brandName
        self.extraFlavor = extraFlavor
        super(Drink, self).__init__(*args, **kwargs)
        
    def changeBrandName(self, newBrandName):
        print('Changing Brand name from {} to {}'.format(self.brandName, newBrandName))
        self.brandName = newBrandName
    
    def addExtraFlavor(self, newFlavorName):
        print('Adding flavor {} to {}'.format(newFlavorName, self.brandName))
        self.extraFlavor = newFlavorName
       
    def removeExtraFlavor(self):
        print('Removing flavor {} from {}'.format(self.extraFlavor, self.brandName))
        self.extraFlavor = None
        
    def printFullDrinkOrder(self):
        print('Drink Order is: \n *Brand: {} \n *Flavor: {} \n *Size: {} \n *Special Instructions: {} \n *Cost: {}'
              .format(self.brandName, self.extraFlavor, self.size, self.specialInstructions, self.cost))
        
class Pizza(MenuItem):
    """
    The Pizza class inherits the MenuItem class.
    @params
    - cheeseAmount = amount of cheese
    - toppingsLeft = a dict that with K = topping name and V = amount
    - toppingsRight = a dict that with K = topping name and V = amount
    - toppingsAll = a dict that with K = topping name and V = amount
    - crustType = e.g. deep dish, NY style
    """    
    def __init__(self, cheeseAmount, toppingsLeft, toppingsRight, toppingsAll, crustType, *args, **kwargs):
        self.cheeseAmount = cheeseAmount
        self.toppingsLeft = toppingsLeft
        self.toppingsRight = toppingsRight
        self.toppingsAll = toppingsAll
        self.crustType = crustType
        super(Pizza, self).__init__(*args, **kwargs)
        
    def addTopping(self, toppingSide, toppingIngredient, toppingAmount):        
        self.__selectPizzaSideByName(toppingSide)[toppingIngredient] = toppingAmount
            
    def removeTopping(self, toppingSide, toppingIngredient):
        # remove toppings from a the respective side
        try:
            del self.__selectPizzaSideByName(toppingSide)[toppingIngredient]
        except KeyError:
            print("Topping {} on pizza side {} not found!".format(self.toppingIngredient, self.toppingSide))
        
    def __selectPizzaSideByName(self, toppingSide):
        toppingSide = toppingSide.lower()
        
        if toppingSide == 'left':
            return self.toppingsLeft
        elif toppingSide == 'right':
            return self.toppingsRight
        elif toppingSide == 'all':
            return self.toppingsAll
        else:
            print('no valid side provided (left/right/all)! Defaulting to all.')
            return self.toppingsAll
                
    def printPizzaFullOrder(self):
        print('Pizza Order Is: \n *Size: {} \n *Cheese Amount: {} \n *Crust Type: {} \n *Cost: {} \n *Special Instructions: {}'
              .format(self.size, self.cheeseAmount, self.crustType, self.cost, self.specialInstructions))
        
        print(' *Left Toppings:', end = '')
        for key, value in self.toppingsLeft.items():
            print(' {} ({})'.format(key, value), end = '')
        print() 

        print(' *Right Toppings:', end = '')
        for key, value in self.toppingsRight.items():
            print(' {} ({})'.format(key, value), end = '')
        print() 
            
        print(' *Left+Right Toppings:', end = '')            
        for key, value in self.toppingsAll.items():
            print(' {} ({})'.format(key, value), end = '')
               
class Appetizer(MenuItem):
    """
    The appetizer class inherits the MenuItem class.
    @params
    - appetizerType = actual name of the appetizer
    - extraFlavor = Side sauce
    """
    def __init__(self, appetizerType, sauceType, *args, **kwargs):
        self.appetizerType = appetizerType
        self.sauceType = sauceType
        super(Appetizer, self).__init__(*args, **kwargs)
        
    def changeAppetizerType(self, newAppetizerType):
        print('Changing Appetizer Type from {} to {}'.format(self.appetizerType, newAppetizerType))
        self.appetizerType = newAppetizerType
    
    def changeAppetizerSauce(self, newSauceType):
        print('Changing Sauce for {} from {} to {}'.format(self.appetizerType, self.sauceType, newSauceType))
        self.sauceType = newSauceType
        
    def printAppetizerOrder(self):
        print('Appetizer Order is: \n *Type: {} \n *Sauce: {} \n *Size: {} \n *Special Instructions: {} \n *Cost: {}'
              .format(self.appetizerType, self.sauceType, self.size, self.specialInstructions, self.cost))
        
def main():
    print('## Drink Test(s) ##')
    itemDrink = Drink("Pepsi", None, "Medium", 3.99, None)
    itemDrink.addExtraFlavor('chocolate')
    itemDrink.removeExtraFlavor()
    itemDrink.changeBrandName('Diet Pepsi')
    itemDrink.printFullDrinkOrder()
    
    print('## Pizza Test(s) ##')
    toppingsLeft = {'pepperoni': 'extra'}
    toppingsRight = {'jalapeno': 'light'}
    toppingsAll = {'roma tomatoes': 'regular'}
    itemPizza = Pizza('regular', toppingsLeft, toppingsRight, toppingsAll, 'deep dish', 'Large', 9.99, 'Well Done')
    itemPizza.addTopping('left', 'pineapple', 'light')
    itemPizza.removeTopping('all', 'roma tomatoes')
    itemPizza.printPizzaFullOrder()
    
    print('\n## Appetizer Test(s) ##')
    itemAppetizer = Appetizer('mozzarella sticks', None, 'small', 1.99, None)
    itemAppetizer.changeAppetizerSauce('marinara sauce')
    itemAppetizer.printAppetizerOrder()

main()