#Importar librería para aplicar color al texto
from colorama import Fore, init
init()


class MusicClass:
  def __init__(self):
    self.gender = "Thrash Metal"
    self.group = "Metallica"
    self.song = "Whisky in the jar"

  def show_info_group(self):
    print(f"{self.group} es mi banda de musica favorita.\n"+Fore.CYAN+"    >>> Canción:"+Fore.RESET+ f" {self.song}\n"+ Fore.CYAN+"    >>> Género musical:"+Fore.RESET+ f" {self.gender}")