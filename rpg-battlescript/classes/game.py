import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, attack, defense, magic, items):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defense = defense
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items
    
    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        return self.hp
    
    def heal(self, damage):
        self.hp += damage
        if self.hp > self.maxHp:
            self.hp = self.maxHp
    
    def restore(self, damage):
        self.mp += damage
        if self.mp > self.maxMp:
            self.mp = self.maxMp

    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxHp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxMp
    
    def reduce_mp(self, cost):
        self.mp -= cost
    
    def choose_target(self, enemies):
        i = 1
        print("\n" + "    Target enemies:")
        for enemy in enemies:
            print("    " + str(i) + ":" + enemy.get_name())
            i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def choose_action(self):
        i = 1
        print("\n" + "    " + self.name + " turn")
        print("\n    ACTIONS")
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1
        
    def choose_magic(self):
        i = 1
        print("\n    MAGIC")
        for spell in self.magic:
            print("    " + str(i) + ":", spell.get_name(), "| cost:", spell.get_cost())
            i += 1
    
    def choose_item(self):
        i = 1
        print("\n    ITEMS")
        for item in self.items:
            print("    " + str(i) + ":", item["item"].get_name(), "|", item["item"].get_description(), "|", "x" + str(item["quantity"]))
            i += 1

    def get_stats(self):
        hp_bar = ""
        hp_bar_total = (self.hp / self.maxHp) * 100 / 4

        while hp_bar_total > 0:
            hp_bar += "█"
            hp_bar_total -= 1
        
        while len(hp_bar) < 25:
            hp_bar += " "
        
        mp_bar = ""
        mp_bar_total = (self.mp / self.maxMp) * 100 / 10
        
        while mp_bar_total > 0:
            mp_bar += "█"
            mp_bar_total -= 1
        
        while len(mp_bar) < 10:
            mp_bar += " "
        
        print("                        _________________________             __________")
        print(f'{self.name: <8}' + ":   " + f'{str(self.hp) + "/" + str(self.maxHp): <11}' + "|" + hp_bar + "|  " +  f'{str(self.mp) + "/" + str(self.maxMp): <8}' + " |" + mp_bar + "|")
        # print(f'{self.name: <8}' + ': ' + f'{str(self.hp) + "/" + str(self.maxHp): <9}')
    
    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar_total = (self.hp / self.maxHp) * 100 / 2

        while hp_bar_total > 0:
            hp_bar += "█"
            hp_bar_total -= 1
        
        while len(hp_bar) < 50:
            hp_bar += " "
        
        print("                        __________________________________________________")
        print(f'{self.name: <8}' + ': ' + f'{str(self.hp) + "/" + str(self.maxHp): <12}' + " |" + hp_bar + "|")


    