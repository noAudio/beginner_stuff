#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
nikki = Cat('Nikki', 2)
miu = Cat('Miu', 4)
moo = Cat('Moo', 1)


# 2 Create a function that finds the oldest cat
def oldest_cat_calculater(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat_calculater(nikki.age, miu.age, moo.age)} years old!')