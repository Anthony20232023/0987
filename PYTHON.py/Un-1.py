class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self.__real_identity = "Unknown"  # private attribute for encapsulation

    def set_identity(self, real_name):
        self.__real_identity = real_name

    def get_identity(self):
        return f"{self.name}'s real identity is {self.__real_identity}"

    def defend_city(self):
        print(f"{self.name} is defending {self.city} using {self.power} 💥")


# Subclass: TechHero inherits from Superhero
class TechHero(Superhero):
    def __init__(self, name, city, gadget):
        super().__init__(name, "Tech Mastery", city)
        self.gadget = gadget

    def defend_city(self):
        print(f"{self.name} uses a {self.gadget} to protect {self.city} 🤖")


# Example usage
hero1 = Superhero("Thunderstrike", "Lightning Control", "Electro City")
hero1.set_identity("Liam Sparks")
hero1.defend_city()
print(hero1.get_identity())

hero2 = TechHero("CyberKnight", "Neo Tokyo", "Nano Suit")
hero1
