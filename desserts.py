"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price, qty = 0):
      
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = qty

      self.cache[name] = self

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def add_stock(self, amount):
      
      self.qty += amount

    def sell(self, amount):
      
      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')
      elif amount >= self.qty:
        self.qty = 0
      else:
        self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):
      
      scaled_recipe = []
      
      for ingredient in ingredients:
        scaled_recipe.append(tuple([ingredient[0], ingredient[1] * amount]))

      return scaled_recipe

    @classmethod
    def get(cls, name):
      
      if name in cls.cache:
        return cls.cache[name]
      
      else:
        print("Sorry, that cupcake doesn't exist")

class Brownie(Cupcake):

  def __init__(self, name, price):
    super().__init__(name, 'chocolate', price, qty = 0)
  
  def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Brownie name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

# c = Cupcake('Strawberry Fields', 'strawberry', 5.0)
# print(c.name)
# print(c.flavor)
# print(c.qty)

# print(Cupcake.cache)
# c.add_stock(10)
# print(Cupcake.cache)