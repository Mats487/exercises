def main():
    brawler1 = Brawler(4, 4, "Aragorn")
    brawler2 = Brawler(2, 7, "Gimli")
    brawler3 = Brawler(7, 7, "Legolas")
    brawler4 = Brawler(3, 2, "Frodo")

    fight(brawler1, brawler2)
    fight(brawler3, brawler4)

# don't touch below this line


class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()
