from dataclasses import dataclass

@dataclass
class Person:
   name: str
   lastname: str

if __name__ == '__main__':
   wes = Person("Wesley", "Bertissolo")
   print(wes.name)