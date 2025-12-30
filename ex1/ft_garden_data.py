class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        """Prints Plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()
    print()
    print("=== End of Program ===")
