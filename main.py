
Toppings=['Pepperoni', 'Sausage', 'Bacon', 'Onion', 'Mushroom']
PizzaSize= {'Small': 8, 'Medium': 9.5, 'Large':11, 'XLarge': 13}
CostPerTopping = 1.5 
XtraCheeseCost = 2.5


# OrderListing=[]

#Creating the classes and functions
class Order:
  items=[]
  def __init__(self):
    self.OrderName= input('What is a name for the order?: ')
    self.toppings = self.items[:]
    self.cost=0

  def OrdSize(self, size):
    self.OrdSize = size

  def OrdCost(self):
    TotalCost=0
    TotalCost+=PizzaSize.get(self.OrdSize)
    if len(self.items)>0:
      TotalCost+=len(self.items)*CostPerTopping
    if XtraCheese=='Yes':
      TotalCost+=1 #Only 1 since XtraCheese will be in items list so will already add 1.5
    return TotalCost

  def PrepTime(self):
    TotalTime=0
    TotalTime+=PizzaSize.get(self.OrdSize)
    if len(self.items)>0:
      TotalTime+=len(self.items)
    if XtraCheese=='Yes':
      TotalTime+=1
    return TotalTime

  def Toppings(self, topping):
    self.items.append(topping)

  # def FinalToppings(self):
  #   FinalToppings=''
  #   for x in range(len(self.items)):
  #     FinalToppings+=self.items[x]
  #   return FinalToppings

  #Printing the receipt 
  def OrderReview(self):
    print()
    print()
    print('**********************************')
    print(f'Order name: {self.OrderName}')
    print(f'You ordered a {self.OrdSize} pizza.')
    # for item in self.items:
    #   print(f'{item}' , end=', ')
    print(f'With {self.items}.')
    print(f'\nTotal prep time was: {self.PrepTime()} minutes.')
    print(f'Total Cost is: ${self.OrdCost():.2f}.')
    print('**********************************')


print('Welcome to CHS Pizza Shop ')
PizOrder = Order()

#Asking what size pizza is wanted
while True:
  print('''
  What size Pizza do you want?
  Press 1 for Small
  Press 2 for Medium
  Press 3 for Large
  Press 4 for XLarge''')
  psize = input(': ')
  if psize == '1':
    PizOrder.OrdSize = 'Small'
    break
  elif psize == '2':
    PizOrder.OrdSize = 'Medium'
    break
  elif psize == '3':
    PizOrder.OrdSize = 'Large'
    break
  elif psize == '4':
    PizOrder.OrdSize = 'XLarge'
    break
  else:
    print('Please pick a size')
    continue

#Asking what toppings are wanted
while True:
  print('''
  What toppings would you like?
  Press 1 to add Pepperoni
  Press 2 to add Sausage
  Press 3 to add Bacon
  Press 4 to add Onions
  Press 5 to add Mushrooms
  Press 6 if you are done adding toppings''')
  topping = input(': ')
  if topping == '1':
    PizOrder.Toppings("Pepperoni")
    continue
  elif topping == '2':
    PizOrder.Toppings("Sausage")
    continue
  elif topping == '3':
    PizOrder.Toppings("Bacon")
    continue
  elif topping == '4':
    PizOrder.Toppings("Onions")
    continue
  elif topping == '5':
    PizOrder.Toppings("Mushrooms")
    continue
  elif topping == '6':
    break
  else:
    print('Please pick a topping.')
    continue

#Asking if they want Xtra cheese

XtraCheese = ''
while XtraCheese=='':
  XtraCheese=input('Would you like to add Xtra Cheese?: ')
  if XtraCheese=='Yes':
    PizOrder.Toppings("XtraCheese")
    break
  if XtraCheese=='No':
   break
  else:
    print("Please Enter Yes or No.")
    XtraCheese=''
    continue

PizOrder.OrderReview()

