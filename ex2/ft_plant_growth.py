class Plant:
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""

        self.name = name
        self.height = height
        self.age_days = age_days

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

    def __str__(self) -> str:
        """Returns a human-readable string representation
        of the Plant object"""
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


if __name__ == "__main__":
    """This method is the equivalent of the main method.
    It executes when the file is ran as a script,
    but not when it's imported as a module"""
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Day 1 ===")
    print(rose)
    day = 1
    while day < 7:
        rose.update()
        day += 1
    print("=== Day 7 ===")
    print(rose)
    growth = rose.height - initial_height
    if growth < 0:
        print(f"Growth this week: {growth}cm")
    elif growth > 0:
        print(f"Growth this week: +{growth}cm")
