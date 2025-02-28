import random


class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.is_alive = True


    def attack(self, target):
        if self.is_alive and target.is_alive:
            damage = self.attack
            target.health -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")
            if target.health <= 0:
                target.is_alive = False
                print(f"{target.name} has been defeated!")
        elif not self.is_alive:
            print(f"{self.name} is defeated.")
        else:
            print(f"{target.name} is already defeated.")


    def show_stats(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Alive: {self.is_alive}")

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, random.randint(80, 120), random.randint(15, 25))
        self.special_ability = "Heal"


    def use_special_ability(self):
        if self.is_alive:
            heal_amount = random.randint(10, 20)
            self.health += heal_amount
            print(f"{self.name} heals for {heal_amount} health!")
            self.show_stats()
        else:
            print(f"{self.name} is defeated.")
            
class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, random.randint(50, 90), random.randint(10, 20))
        self.enemy_type = random.choice(["Goblin", "Orc"])


hero = Hero("Hero")
enemy = Enemy("Enemy")
while hero.is_alive and enemy.is_alive:
    print("\nChoose your action:")
    print("1. Attack")
    print("2. Use Special Ability")
    print("3. Show Stats")
    while True:
        try:
            choice = 2
            int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3")
        except:
            print()



