from enemies import Ienemies


class Player(Ienemies):

  def __init__(self):
    self.maxhp = 100
    self.hp = 100
    self.atk = 20
    self.maxcapacity = 4
    self.inventory = []

  def AddItem(self, item):
    if self.maxcapacity > 0:
      self.inventory.append(item)
      print(f"{item.Name()} foi adicionado ao inventário!")
      self.maxcapacity -= 1
    else:
      print("Sem espaço disponível!")

  def DeleteItem(self, invindex):
    item = self.inventory[invindex-1].Heal()
    self.inventory.pop(invindex-1)
    self.maxcapacity += 1
    return item

  def ConsumeItem(self):
    itemOrder = 1
    if self.inventory[0] is None:
      print("Sem items de cura!")
      return 0
    for i in self.inventory:
      print(f"{itemOrder} - {i.Name()}")
    print("Para cancelar pressione 0 e enter!")
    print()
    selection = int(input())
    if selection == 0:
      return 0
    return self.DeleteItem(selection)
