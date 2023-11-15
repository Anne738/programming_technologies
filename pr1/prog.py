

class Order:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

class OrderStack:
    def __init__(self):
        self.stack = []

    def push(self, i, q):
        order = Order(i, q)
        if order.quantity > 0:
            self.stack.append(order)
        else:
            return False

    def pop(self):
        order = self.stack.pop()

    def view(self):
        print("Список замовлень:")
        for order in self.stack:
            print(f"- {order.item} ({order.quantity} одиниць)")

ord = None
def switch_case(option):
    global ord
    if option == 1:
        ord = OrderStack()
        print("new")
    elif option == 2:
        ord.push("frog", 4)
        ord.view()
    elif option == 3:
        ord.view()
    elif option == 4:
        ord.pop()
        ord.view()


while True:
    print("list comand:\n 1-create\n 2-add\n 3-view\n 4-delete\n")
    c = int(input("your choice "))
    switch_case(c)
