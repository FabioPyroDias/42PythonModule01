class Plant:
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""

        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """Returns a human-readable string representation
        of the Plant object"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    """This method is the equivalent of the main method.
    It executes when the file is ran as a script,
    but not when it's imported as a module"""
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(rose)
    print(sunflower)
    print(cactus)
    print()
    print("=== End of Program ===")
