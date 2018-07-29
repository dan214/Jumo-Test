

class LoanParameter(object):
  registry = {}
  def __init__(self, name):
    self.name = name
    self.totals_loan = 0
    self.count = 1

  @classmethod
  def create_item(cls, x):
      try:
          return cls.registry[x]
      except KeyError:
          new_item = cls(x)
          cls.registry[x] = new_item
          return new_item

  def loan_amount(self, amt):
      self.totals_loan = self.totals_loan + amt

  def set_loan_type(self,type):
      self.type = type

  def set_number_of_loans(self):
      self.count = self.count + 1

  def get_number_of_loans(self):
      return self.count

  def getLoanAmount(self):
      return self.totals_loan

  def to_tuple(self):
      return (self.name, self.totals_loan,self.count)

  def __str__(self):
      return self.name