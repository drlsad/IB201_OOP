class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self._proteins = proteins
        self._fats = fats
        self._carbohydrates = carbohydrates

    def get_proteins(self):
        return self._proteins

    def get_fats(self):
        return self._fats

    def get_carbohydrates(self):
        return self._carbohydrates

    def get_kcalories(self):
        return 4 * self._proteins + 9 * self._fats + 4 * self._carbohydrates

    def __add__(self, other):
        total_proteins = self._proteins + other._proteins
        total_fats = self._fats + other._fats
        total_carbohydrates = self._carbohydrates + other._carbohydrates
        return FoodInfo(total_proteins, total_fats, total_carbohydrates)


food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(),
      food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(),
      food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.get_kcalories())

