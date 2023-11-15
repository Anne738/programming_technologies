

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
                #print("Помилка: Кількість товару повинна бути більше 0.")
            return False
        #try:
            
        #except TypeError:
            #print("Помилка: Невірний формат замовлення.")

    def pop(self):
        order = self.stack.pop()
        #try:
        #    order = self.stack.pop()
        #    #print(f"Замовлення на {order.item} ({order.quantity} одиниць) виконано.")
        #    return -1
        #except IndexError:
        #    print("Стек замовлень порожній.")

    def view(self):
        #print("Список замовлень:")
        for order in self.stack:
            print(f"- {order.item} ({order.quantity} одиниць)")



