class PersonClass:

  #Método inicializador, constructor de la clase
  def __init__(self):
    self.name = "Fulgencio"
    self.edad = 20
    self.labora = False

  def show_info_person(self):
    print(f"{self.name} {self.edad} {self.labora}")