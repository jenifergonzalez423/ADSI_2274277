#Importar librería para aplicar color al texto
from colorama import Fore, init
init()
#Importar la clase
from person import PersonClass
from pet import PetClass
from music import MusicClass

#Crear instancia de la clase
inst_person = PersonClass()
inst_pet = PetClass()
inst_music = MusicClass()
#Mediante la instancia se deben de llamar los métodos de la clase diferentes al constructor __init__
print(Fore.GREEN + "Clase person" + Fore.RESET )
inst_person.show_info_person()
print(Fore.GREEN + "Clase pet" + Fore.RESET )
inst_pet.show_info_pet()
print(Fore.GREEN + "Clase music" + Fore.RESET )
inst_music.show_info_group()
