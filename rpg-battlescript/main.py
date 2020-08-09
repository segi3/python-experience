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

enemy = Person("Orc", 1200, 30, 50, 70, [], [])

players = [player1, player2]

running = True
i = 0

while running:
    print("===================================")
    print("\n\n")
    print("NAME                   HP                                  MP")
    for player in players:
        player.get_stats()

    for player in players:
        player.choose_action()
        choice = input("Choose Action: ")

        if choice == "1":
            damage = player.generate_damage()
            enemy.take_damage(damage)
            print("You attacked for", damage, "damage")

        elif choice == "2":
            player.choose_magic()
            magic_choice = int(input("Choose Magic: ")) - 1

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
                enemy.take_damage(magic_damage)
                print(bcolors.FAIL + "\n" + spell.get_name() + " deals", magic_damage, "magic damage", bcolors.ENDC)
        
        elif choice == "3":
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

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
                # player.hp = player.maxHp
                # player.mp = player.maxMp
                player.heal(player.get_max_hp())
                player.restore(player.get_max_mp())
                print(bcolors.OKGREEN + "\n" + item.get_name() + " Fully restores Hp/MP", bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.get_prop())
                print(bcolors.OKGREEN + "\n" + item.get_name() + " deals", str(item.get_prop()), "Damage to enemy", bcolors.ENDC)
    
    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player1.take_damage(enemy_damage)
    print("Enemy attacked " + player1.get_name()  + " for", enemy_damage, "points")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + "You Lose!" + bcolors.ENDC)
        running = False
