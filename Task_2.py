class Lemonade:
    
    def __init__(self, type_of_additive: str):
            self.type_of_additive = type_of_additive

    @property
    def drink_info(self):
        print(f"Lemonade with {self.type_of_additive}")


lemonade = Lemonade("Bluberry")
lemonade.drink_info


