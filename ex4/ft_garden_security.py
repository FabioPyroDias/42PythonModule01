class SecurePlant:
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """Returns Plant's current height"""
        return self.__height

    def get_age(self) -> int:
        """Returns Plant's current age"""
        return self.__age

    def set_height(self, height: int) -> None:
        """Set Plant's height, ensuring its not negative"""
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """Set Plant's age, ensuring its not negative"""
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days old [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def print_info(self):
        """Prints SecurePlant information"""
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print()
    print(f"Current plant: {rose.print_info()}")
