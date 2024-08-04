import random


# Определяем классы игрока и монстров
class Player:
    def __init__(self, player_class):
        self.health = 100
        self.max_health = 100
        self.mana = 100
        self.max_mana = 100
        self.stamina = 100
        self.max_stamina = 100
        self.action_points = 5
        self.player_class = player_class

        # Установим дополнительные очки действия в зависимости от класса
        if player_class == "fighter":
            self.attack_bonus = 1
            self.defense_bonus = 0
        elif player_class == "defender":
            self.attack_bonus = 0
            self.defense_bonus = 1
        elif player_class == "mage":
            self.action_points = 3
            self.attack_bonus = 0
            self.defense_bonus = 0
            self.damage_multiplier = 2
        else:
            raise ValueError("Неизвестный класс персонажа.")

    def display_stats(self):
        print(f"Здоровье: {self.health}/{self.max_health} "
              f"({(self.health / self.max_health) * 100:.1f}%)")
        print(f"Мана: {self.mana}/{self.max_mana} "
              f"({(self.mana / self.max_mana) * 100:.1f}%)")
        print(f"Выносливость: {self.stamina}/{self.max_stamina} "
              f"({(self.stamina / self.max_stamina) * 100:.1f}%)")


class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.action_points = 5

    def display_stats(self):
        print(f"Здоровье {self.name}: {self.health}/{self.max_health} "
              f"({(self.health / self.max_health) * 100:.1f}%)")


# Определяем систему боя
def battle(player, monster):
    print(f"\nВы встретили {monster.name}!")
    choice = input("Начать бой (1) или сбежать (0)? ")
    if choice == "0":
        print("Вы сбежали от боя!")
        return

    while player.health > 0 and monster.health > 0:
        player_action(player, monster)


def player_action(player, monster):
    attack_points = [1, 2, 3, 4, 5, 6, 7]
    defense_points = [1, 2, 3, 4, 5, 6, 7]

    # Фаза защиты
    player_defense = []
    print("Выберите точки защиты (1-7, не более 5): ")
    print("1 - Голова")
    print("2 - Торс")
    print("3 - Пояс")
    print("4 - Правая рука")
    print("5 - Левая рука")
    print("6 - Правая нога")
    print("7 - Левая нога")

    player.display_stats()
    defense_choice = input("Ваш выбор: ").strip()
    if defense_choice:
        selected_defense = [int(x) for x in defense_choice.split(",") if int(x) in defense_points]
        player_defense = selected_defense[:5]  # Ограничиваем до 5 значений
    defense_used = len(player_defense)

    # Рассчитываем выносливость
    player.stamina -= defense_used * 5
    if player.stamina < 0:
        player.stamina = 0

    # Фаза атаки
    attack_points_used = player.action_points - defense_used
    if attack_points_used > 0:
        player_attack = []
        print("Теперь выберите точки атаки (1-7): ")
        attack_choice = input("Ваш выбор: ").strip()
        if attack_choice:
            selected_attack = [int(x) for x in attack_choice.split(",") if int(x) in attack_points]
            player_attack = selected_attack[:attack_points_used]

        # Расчет урона
        calculate_damage(player, player_attack, player_defense, monster)

    # Восстановление выносливости
    if defense_used == 0:
        player.stamina = min(player.max_stamina, player.stamina + 100)
    else:
        player.stamina = min(player.max_stamina, player.stamina + 20 * (player.action_points - defense_used))

    monster.display_stats()
    player.display_stats()


def calculate_damage(player, player_attack, player_defense, monster):
    damage_mapping = {
        1: 10,  # голова
        2: 5,  # торс
        3: 5,  # таз
        4: 1,  # правая рука
        5: 1,  # левая рука
        6: 1,  # правая нога
        7: 1,  # левая нога
    }

    # Урон игрока
    for attack in player_attack:
        if attack not in player_defense:  # Если атака проходит
            damage = damage_mapping[attack] * (1 if player.player_class != "mage" else player.damage_multiplier)
            monster.health -= damage
            print(f"Вы нанесли {damage} урона {monster.name} по точке {attack}!")

    # Урон игрока
    monster_damage = random.randint(5, 20)  # Примерный урон от монстра
    player.health -= monster_damage
    print(f"{monster.name} нанес вам {monster_damage} урона!")


def choose_class():
    print("Выберите класс персонажа:")
    print("1. Боец")
    print("2. Защитник")
    print("3. Маг")

    class_choice = input("Ваш выбор (1-3): ")
    if class_choice == "1":
        return Player("fighter")
    elif class_choice == "2":
        return Player("defender")
    elif class_choice == "3":
        return Player("mage")
    else:
        print("Некорректный ввод. Попробуйте снова.")
        return choose_class()


def main():
    player = choose_class()

    monsters = ["Скелет", "Зомби", "Гоблин", "Орк", "Вампир", "Драконид", "Дракон"]
    while player.health > 0:
        monster_name = random.choice(monsters)
        monster = Monster(monster_name)
        battle(player, monster)

    print("Вы проиграли игру!")


if __name__ == "__main__":
    main()
