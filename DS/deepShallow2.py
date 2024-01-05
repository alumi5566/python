import copy


class Car:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

honda_colors = ["Red", "Blue"]
honda = Car("Honda", honda_colors)

honda_equal = honda
honda_shallow = copy.copy(honda)
honda_deep = copy.deepcopy(honda)
print("honda.colors: ", honda.colors)
print("honda_equal.colors", honda_equal.colors)
print("honda_shallow.colors", honda_shallow.colors)
print("honda_deep.colors", honda_deep.colors)

honda.colors.append("Black")
print("\nUpdate honda.colors.append('Black')")
print("honda.colors: ", honda.colors)
print("honda_equal.colors", honda_equal.colors)
print("honda_shallow.colors", honda_shallow.colors)
print("honda_deep.colors", honda_deep.colors)