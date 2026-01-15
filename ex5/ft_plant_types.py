class Plant:
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""

        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set Plant's height, ensuring its not negative"""
        if height >= 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")

    def set_age(self, age: int) -> None:
        """Set Plant's age, ensuring its not negative"""
        if age >= 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")

    def get_height(self) -> int:
        """Returns Plant's current height"""
        return self.__height

    def get_age(self) -> int:
        """Returns Plant's current age"""
        return self.__age

    def __str__(self, plant_type: str = "Plant") -> str:
        """Returns Plant's current information as well as it's type"""
        return f"{self.name} ({plant_type}): {self.__height}cm, {self.__age} days"


class Flower(Plant):
    """Inherits Plant. Represents a specific Plant (Flower)"""

    def __init__(self, name: str, height: int, age: int, color: str):
        """This method calls the parent class method __init__, with
        the base properties. The new properties are handled in this
        function"""

        super().__init__(name, height, age)
        self.set_color(color)

    def set_color(self, color: str) -> None:
        """Set Flower's color"""
        if color is not None:
            self.__color = color
        else:
            print(f"Invalid operation attempted: color {color} [REJECTED]")

    def get_color(self) -> str:
        """Returns Flower's current color"""
        return self.__color

    def bloom(self) -> None:
        """Specific Flower method."""
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        """Prints Flower information"""
        return f"{super().__str__('Flower')}, {self.__color} color"


class Tree(Plant):
    """Inherits Plant. Represents a specific Plant (Tree)"""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: str):
        """This method calls the parent class method __init__, with
        the base properties. The new properties are handled in this
        function"""

        super().__init__(name, height, age)
        self.__trunk_diameter = 0
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter: int) -> None:
        """Set Tree's trunk diameter"""
        if trunk_diameter > 0:
            self.__trunk_diameter = trunk_diameter
        else:
            print("Error")

    def get_trunk_diameter(self) -> int:
        """Returns Tree's current trunk diameter"""
        return self.__trunk_diameter

    def produce_shade(self) -> None:
        """Specific Tree method"""
        print(f"{self.name} provides "
              f"{(3.14 * ((self.__trunk_diameter) ** 2))/100:.0f} "
              f"square meters of shade")

    def __str__(self) -> str:
        """Prints Tree information"""
        return f"{super().__str__('Tree')}, " \
        f"{self.__trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Inherits Plant. Represents a specific Plant (Vegetable)"""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """This method calls the parent class method __init__, with
        the base properties. The new properties are handled in this
        function"""

        super().__init__(name, height, age)
        self.set_harvest_season(harvest_season)
        self.set_nutritional_value(nutritional_value)

    def set_harvest_season(self, harvest_season: str) -> None:
        """Set Vegetables's harvest season"""
        if harvest_season is not None:
            self.__harvest_season = harvest_season
        else:
            print(f"Invalid operation attempted: harvest season "
            f"{harvest_season} [REJECTED]")

    def set_nutritional_value(self, nutritional_value: str) -> None:
        """Set Vegetables's nutritional value"""
        if nutritional_value is not None:
            self.__nutritional_value = nutritional_value
        else:
            print(f"Invalid operation attempted: nutritional value "
            f" {nutritional_value} [REJECTED]")

    def get_harvest_seson(self) -> str:
        """Returns Vegetables's current harvest season"""
        return self.__harvest_season

    def get_nutritional_value(self) -> str:
        """Returns Vegetables's current nutritional value"""
        return self.__nutritional_value

    def print_nutritional_value(self) -> None:
        """Specific Vegetable method"""
        print(f"{self.name} is rich in vitamin {self.__nutritional_value}")

    def __str__(self) -> str:
        """Prints Vegetable information"""
        return f"{super().__str__('Vegetable')}, " \
        f"{self.__harvest_season} harvest"


if __name__ == "__main__":
    """This method is the equivalent of the main method.
    It executes when the file is ran as a script,
    but not when it's imported as a module"""
    print("=== Garden Plant Types ===")
    print()
    p1 = Flower("Rose", 25, 30, "red")
    print(p1)
    p1.bloom()
    print()
    p2 = Flower("Tulip", 40, 20, "yellow")
    print(p2)
    p2.bloom()
    print()
    t1 = Tree("Oak", 500, 1825, 50)
    print(t1)
    t1.produce_shade()
    print()
    t2 = Tree("Maple", 800, 3650, 60)
    print(t2)
    t2.produce_shade()
    print()
    v1 = Vegetable("Tomato", 80, 90, "summer", "C")
    print(v1)
    v1.print_nutritional_value()
    print()
    v2 = Vegetable("Carrot", 30, 70, "fall", "beta-carotene")
    print(v2)
    v2.print_nutritional_value()
