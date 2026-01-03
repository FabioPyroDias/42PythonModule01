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

    def get_info(self) -> None:
        """Prints Plant information"""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(1, 7):
        rose.update()
    print("=== Day 7 ===")
    rose.get_info()
    growth = rose.height - initial_height
    if growth < 0:
        print(f"Growth this week: {growth}cm")
    elif growth > 0:
        print(f"Growth this week: +{growth}cm")
