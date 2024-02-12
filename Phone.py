from Shop import Item


class Phone(Item):
  def __init__(self, name: str = "Unknown", price: float = 0, quantity: int = 0, status: str = "Unkown") -> None:
    # Call to super function to have access to all atributes and methods
      super().__init__(
          name,price,quantity
      )

      # Run validations to the received arguments
      assert status >= 0, f"Broken Phones {status}"

      # Assign to self-object
      self.status = status
      

