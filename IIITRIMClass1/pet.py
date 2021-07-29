class PetClass:

  def __init__(self):
    self.code = 1
    self.name = "Dante"
    self.breed = "Cooker Spaniel"
    self.born_year = 2018
    self.pedigree = False
  
  def show_info_pet(self):
    print(f"{self.name} es un perro de raza {self.breed} que nacio en el año {self.born_year}")


