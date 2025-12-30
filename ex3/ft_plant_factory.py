class Plant:
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self):
        """The plant gets 1 cm taller"""
        self.height += 1

    def age(self):
        """The plant gets 1 day older"""
        self.age_days += 1

    def update(self):
        """Updates both properties: height and age"""
        self.grow()
        self.age()

    def get_info(self):
        """Prints Plant information"""
        return f"{self.name} ({self.height}cm, {self.age_days} days)"


if __name__ == "__main__":
    names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    height = [25, 200, 5, 80, 15]
    age = [30, 365, 90, 45, 120]
    max_plants = 5
    plants = [None] * max_plants
    print("=== Plant Factory Output ===")
    for index in range(max_plants):
        plants[index] = Plant(names[index], height[index], age[index])
        print("Created: " + plants[index].get_info())
    print()
    print("Total plants created: " + str(max_plants))
