class IHealingItems:

  def __init__(self):
    self.name = self.name
    self.heal = self.heal

  def Heal(self):
    return self.heal

  def Name(self):
    return self.name


class Items:
  class Beef(IHealingItems):

  def __init__(self):
    self.name = "Beef"
    self.heal = 20


  class HealingPotion(IHealingItems):

   def __init__(self):
      self.name = "Healing Potion"
      self.heal = 40
