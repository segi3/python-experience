import random

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.item import Item

# black magic
fire = Spell("Fireball", 10, 85, "black")
thunderstrike = Spell("Thunderstrike", 15, 110, "black")
blizzard = Spell("Blizzard", 25, 125, "black")
quake = Spell("Quake", 5, 50, "black")

# white magic
cure = Spell("Cure", 12, 120, "white")
bless = Spell("Bless", 18, 200, "white")


# items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
cake = Item("Cake", "potion", "Heals 70 HP", 70)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
healbomb = Item("Heal Bomb", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)
poison = Item("Poison", "attack", "Deals 250 damage", 250)

player_items = [{"item": potion, "quantity": 5}, 
                {"item": cake, "quantity": 5}, 
                {"item": elixer, "quantity": 2}, 
                {"item": healbomb, "quantity": 1}, 
                {"item": grenade, "quantity": 2}, 
                {"item": poison, "quantity": 2}]

player_magic = [fire, thunderstrike, blizzard, cure, bless]


# player instance and enemy instance
player1 = Person("Phoenix", 500, 100, 60, 120, player_magic, player_items)
player2 = Person("Sage", 500, 100, 60, 120, player_magic, player_items)

enemy1 = Person("Remag", 1200, 100, 100, 70, [fire, blizzard], [])
enemy2 = Person("trutlus", 600, 65, 100, 500, [fire], [])

players = [player1, player2]
enemies = [enemy1, enemy2]

running = True
i = 0

while running:
    print("===================================")
    print("\n\n")
    print("NAME                   HP                                    MP")
    for player in players:
        player.get_stats()
    
    print("\nENEMY                   HP")
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    # * players
    for player in players:
        player.choose_action()
        choice = input("    Choose Action: ")

        if choice == "1":
            damage = player.generate_damage()
            target = player.choose_target(enemies)
            enemies[target].take_damage(damage)
            print(player.get_name() + " attacked " + enemies[target].get_name()  + " for", damage, "damage")

            if enemies[target].get_hp() == 0:
                print(enemies[target].get_name() + " has died")
                del enemies[target]

        elif choice == "2":
            player.choose_magic()
            magic_choice = int(input("    Choose Magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]

            current_mp = player.get_mp()

            if spell.get_cost() > current_mp:
                print(bcolors.FAIL + "\nNot enought MP" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.get_cost())
            magic_damage = spell.generate_damage()

            if spell.get_type() == "white":
                player.heal(magic_damage)
                print(bcolors.OKGREEN + "\n" + spell.get_name() + " heals", magic_damage, "HP", bcolors.ENDC)
            elif spell.get_type() == "black":
                target = player.choose_target(enemies)
                enemies[target].take_damage(magic_damage)
                print("\n" + spell.get_name() + " deals", magic_damage, "magic damage to", enemies[target].get_name())

                if enemies[target].get_hp() == 0:
                    print(enemies[target].get_name() + " has died")
                    del enemies[target]

        elif choice == "3":
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if player.items[item_choice]["quantity"] == -1:
                print(bcolors.FAIL + "\n" + "You have none left", bcolors.ENDC)
                player.items[item_choice]["quantity"] = 0
                continue

            if item.get_type() == "potion":
                player.heal(item.get_prop())
                print(bcolors.OKGREEN + "\n" + item.get_name() + " heals", str(item.get_prop()), "HP", bcolors.ENDC)
            elif item.type == "elixer":
                if item.get_name() == "Heal Bomb":
                    for player in players:
                        player.heal(player.get_max_hp())
                        player.restore(player.get_max_mp())
                
                player.heal(player.get_max_hp())
                player.restore(player.get_max_mp())
                print(bcolors.OKGREEN + "\n" + item.get_name() + " Fully restores Party's HP/MP", bcolors.ENDC)
            elif item.type == "attack":
                target = player.choose_target(enemies)
                enemies[target].take_damage(item.get_prop())
                print(bcolors.OKGREEN + "\n" + item.get_name() + " deals", str(item.get_prop()), "Damage to", enemies[target].get_name(), bcolors.ENDC)
                if enemies[target].get_hp() == 0:
                    print(enemies[target].get_name() + " has died")
                    del enemies[target]
    
    # * over condition
    defeated_enemies = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    
    defeated_players = 0
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + "You Lose!" + bcolors.ENDC)
        running = False
    
    # * enemies
    for enemy in enemies:
        # enemy_choice = random.randrange(0, 3)
        enemy_choice = 0

        if enemy_choice == 0:
            target = random.randrange(0, 2)

            enemy_damage = enemy.generate_damage()
            players[target].take_damage(enemy_damage)
            print("\n" + enemy.get_name() +  " attacked " + players[target].get_name()  + " for", enemy_damage, "points")

        elif enemy_choice == 1 and enemy.get_mp() > 50:
            # chose attack spell
            
            if enemy.get_hp()/enemy.get_max_hp() > 0.5:
                valid = False
                while not valid:
                    magic_choice = random.randrange(0, len(enemy.magic))
                    spell = enemy.magic[magic_choice]
                    
                    if enemy.get_mp() > spell.get_cost() and spell.get_type() == "black":
                        valid = True
                magic_damage = spell.generate_damage()
                enemy.reduce_mp(spell.get_cost())

                target = random.randrange(0, 2)
                players[target].take_damage(magic_damage)
                print("\n" + enemy.get_name() +  " attacked " + players[target].get_name()  + " for", magic_damage, "magic damage")


    
