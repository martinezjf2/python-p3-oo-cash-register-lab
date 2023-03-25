#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.last_transaction = 0
    self.items = []
  
  def add_item(self, title, price, quantity=1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    
    # Resource: https://www.w3schools.com/python/python_for_loops.asp
    for x in range(quantity):
      self.items.append(title)
      
  
  def apply_discount(self):
    if self.discount:
      a = (self.total * self.discount) / 100
      self.total = self.total - a
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    pass
  
  def void_last_transaction(self):
    self.total -= self.last_transaction
    pass
    