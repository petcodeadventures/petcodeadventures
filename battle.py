import random
import time

class Rogue:
    def __init__(self, name, dex, int, vit):
        # attributes (data)
        self.name = name
        self.base_health = 10
        self.dex = dex
        self.int = int
        self.essence = int * 3
        self.health = vit * 3 + self.base_health
        self.max_health = self.health

    def show_stats(self):
        time.sleep(2)
        print(f"Name: {self.name} \nDexterity Points: {self.dex} \nIntelligence Points: {self.int} \nEssence: {self.essence}")
        time.sleep(2)
        if self.health <= self.max_health - 5:
            self.health = self.health + 5
        else:
            self.health = self.max_health

    def take_damage(self, damage):
        self.health -= damage
        print(f"\n{self.name} took {damage}, remaining health: {self.health}.")
        time.sleep(1)

    def melee_attack(self):  # return damage if dice_hits is greater or equal than 5
        dice_hits = random.randint(1, 10)
        if dice_hits == 10:
            dice_dmg = random.randint(1, 6)
            dice_crit = random.randint(1, 6)
            dmg = self.dex + dice_dmg + dice_crit
            print("\nCritical hit, rolling 2d6 plus dexterity for damage:")
            time.sleep(1)
            print(f"{self.name} attacks and deals {dmg}!")
            time.sleep(1)
            return dmg
        elif dice_hits >= 5 and dice_hits < 10:
            dice_dmg = random.randint(1, 6)
            dmg = self.dex + dice_dmg
            print("\nRolling 1d6 for damage plus your dexterity:")
            time.sleep(1)
            print(f"{self.name} attacks and deals {dmg}!")
            time.sleep(1)
            return dmg
        else:
            time.sleep(1)
            print(f"\n{self.name} tries to hit the target, but misses!")
            time.sleep(1)
            return 0

    def essence_attack(self, essence):  # return damage if dice_hits is greater or equal than 4
        self.essence -= essence
        if essence > 0:
            dice_hits = random.randint(1, 10)
            if dice_hits == 10:
                dice_dmg = random.randint(1, 3)
                dice_crit = random.randint(1, 3)
                dmg = self.int + essence + dice_dmg + dice_crit
                print("\nCritical hit, rolling 2d3 plus int and essence for damage:")
                time.sleep(1)
                print(f"{self.name} attacks with a shining essence blade and deals {dmg}!")
                time.sleep(1)
                return dmg
            elif dice_hits >= 4 and dice_hits < 10:
                dice_dmg = random.randint(1, 3)
                dmg = self.int + essence + dice_dmg
                print("\nRolling 1d3 plus essence for damage:")
                time.sleep(1)
                print(f"{self.name} attacks with an essence blade and deals {dmg} damage!")
                time.sleep(1)
                return dmg
            else:
                time.sleep(1)
                print("\nYou miss! But...")
                time.sleep(1)
                print("You cause at least a bit of damage by luck!")
                time.sleep(1)
                return 1
        else:
            print(f"\n{self.name} needs to spend at least some essence to deal magical damage!")
            time.sleep(1)
            print("You cause at least a bit of damage by luck!")
            time.sleep(1)
            return 1

    def is_alive(self):  # return false or true
        return self.health > 0

class Monster:
    def __init__(self, name, dex, str, vit):
        self.name = name
        self.vit = vit
        self.str = str
        self.dex = dex
        self.health = vit * 3

    def take_damage(self, damage):
        self.health -= damage
        print(f"\n{self.name} took {damage}, remaining health: {self.health}.")
        time.sleep(1)

    def attack(self):
        dice_hits = random.randint(1, 10)
        if dice_hits == 10:
            dice_dmg = random.randint(1, 6)
            dice_crit = random.randint(1, 6)
            dmg = self.str + dice_dmg + dice_crit
            print("\nCritical hit, rolling 2d6 plus strength for damage:")
            time.sleep(1)
            print(f"{self.name} attacks and deals {dmg}!")
            time.sleep(1)
            return dmg
        elif dice_hits >= 5 and dice_hits < 10:
            dice_dmg = random.randint(1, 6)
            dmg = self.str + dice_dmg
            print("\nRolling 1d6 for damage plus your strength:")
            time.sleep(1)
            print(f"{self.name} attacks and deals {dmg}!")
            time.sleep(1)
            return dmg
        else:
            time.sleep(1)
            print(f"\n{self.name} tries to hit the target, but misses!")
            time.sleep(1)
            return 0

    def quick_attack(self):
        dice_hits = random.randint(1, 10) + self.dex
        if dice_hits == 15:
            dice_dmg = random.randint(1, 2)
            dice_crit = random.randint(1, 2)
            dmg = dice_dmg + dice_crit
            print("\nCritical hit, rolling 2d2 plus dexterity for damage:")
            time.sleep(1)
            print(f"{self.name} attacks and deals {dmg}!")
            time.sleep(1)
            return dmg
        elif dice_hits >= 7 and dice_hits < 15:
            dice_dmg = random.randint(1, 2)
            dmg = dice_dmg
            print("\nHit! Rolling 1d2 for damage:")
            time.sleep(1)
            print(f"{self.name} makes a quick attack, dealing {dmg}!")
            time.sleep(1)
            return dmg
        else:
            dice_dmg = random.randint(1, 2)
            dmg = dice_dmg
            self.health -= dmg
            time.sleep(1)
            print(f"\nEven with an easy attack, {self.name} ends up hurting itself! It takes {dmg} from its own mistake!")
            time.sleep(1)
            return 0

    def is_alive(self):
        return self.health > 0

# for hero: (name, dex, int, vit)
hero = Rogue("George", 2, 3, 5)
# for monster (name, dex, str, vit)
goblin = Monster("Goblin Chief", 2, 1, 7)

while hero.is_alive() and goblin.is_alive():
    # player's turn
    action = int(input("\nChoose an action: \n1. Attack with your sword (deals 1d6+dex) \n2. Attack with your essence (deals 1d3+essence+int) \n3. Look at yourself (heals 5)\n"))

    if action == 1:
        print("\nYou chose to attack with your weapon!")
        damage = hero.melee_attack()
        goblin.take_damage(damage)
    elif action == 2:
        print("\nYou chose to cast a magical attack!")
        print(f"You have {hero.essence} essence points available.")
        essence_usage = int(input(f"How many essence points do you want to use in the attack?\n"))
        damage = hero.essence_attack(essence_usage)
        goblin.take_damage(damage)
    else:
        print("\nYou observe yourself and strengthen your determination!")
        print("You heal 5 health points!\n")
        hero.show_stats()
        print(f"\nCurrently at {hero.health} health points.")

    if not goblin.is_alive():
        print(f"{goblin.name} has been defeated! You win!")
        break

    enemy_action = random.randint(1, 3)

    time.sleep(1)
    print("\nThe enemy thinks!")
    time.sleep(1)

    if enemy_action == 1:
        print(f"\n{goblin.name} attacks you with tremendous strength!")
        damage = goblin.attack()
        hero.take_damage(damage)
        time.sleep(1)
    elif enemy_action == 2:
        print(f"\n{goblin.name} attacks you slightly but quickly!")
        damage = goblin.quick_attack()
        hero.take_damage(damage)
        time.sleep(1)
    else:
        print(f"\n{goblin.name} is just standing there... threatening.")
        time.sleep(1)

    if not hero.is_alive():
        print(f"\n{hero.name} has been defeated! You lose!")
        break
