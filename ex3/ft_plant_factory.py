class Plant:
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""

        self.name = name
        self.height = height
        self.age_days = age_days
        print(f"Created: {self.__str__()}")

    def grow(self) -> None:
        """The plant gets 1 cm taller"""
        self.height += 1

    def age(self) -> None:
        """The plant gets 1 day older"""
        self.age_days += 1

    def update(self) -> None:
        """Updates both properties: height and age"""
        self.grow()
        self.age()

    def __str__(self) -> None:
        """Returns a human-readable string representation
        of the Plant object"""
        return f"{self.name} ({self.height}cm, {self.age_days} days)"


if __name__ == "__main__":
    """This method is the equivalent of the main method.
    It executes when the file is ran as a script,
    but not when it's imported as a module"""
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print()
    max_plants = 5
    print(f"Total plants created: {max_plants}")
