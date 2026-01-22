class Plant():
    """Represents a Plant and its properties"""

    def __init__(self, name: str, height: int) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created"""
        self.name = name
        self.__height = 0
        self.set_height(height)

    def set_height(self, height: int) -> None:
        """Set Plant's height, ensuring its not negative"""
        if height >= 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")

    def get_height(self) -> int:
        """Returns Plant's current height"""
        return self.__height

    def __str__(self) -> str:
        """Returns Plant's current information"""
        return f"{self.name}: {self.__height}cm"


class FloweringPlant(Plant):
    """Inherits Plant. Represents a specific Plant (FloweringPlant)"""

    def __init__(self, name: str, height: int, color: str) -> None:
        """This method calls the parent class method __init__, with
        the base properties. The new properties are handled in this
        function"""
        super().__init__(name, height)
        self.__color = "red"
        self.set_color(color)

    def set_color(self, color: str) -> None:
        """Set FloweringPlant's color, ensuring it isn't None"""
        if color is not None:
            self.__color = color
        else:
            print(f"Invalid operation attempted: color "
                  f"{color} [REJECTED]")

    def get_color(self) -> str:
        """Returns FloweringPlant's color"""
        return self.__color

    def __str__(self) -> str:
        """Returns FloweringPlant's current information"""
        return f"{super().__str__()}, {self.__color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Inherits Plant. Represents a specific Plant (PrizeFlower)"""

    def __init__(self, name: str, height: int,
                 color: str, prize_points: int) -> None:
        """This method calls the parent class method __init__, with
        the base properties. The new properties are handled in this
        function"""
        super().__init__(name, height, color)
        self.__prize_points = 0
        self.set_prize_points(prize_points)

    def set_prize_points(self, prize_points: int) -> None:
        """Set PrizeFlower's prize_points, ensuring it's not negative"""
        if prize_points >= 0:
            self.__prize_points = prize_points
        else:
            print(f"Invalid operation attempted: prize_points "
                  f"{prize_points} [REJECTED]")

    def get_prize_points(self) -> int:
        """Returns PrizeFlower's current prize_points"""
        return self.__prize_points

    def __str__(self) -> str:
        """Returns PrizeFlower's current information"""
        return f"{super().__str__()}, Prize points: {self.__prize_points}"


class GardenManager():
    """Represents the Garden. It will hold several flowers
    and manage them"""
    __gardens = []

    def __init__(self, name: str) -> None:
        """This method is used to assign values to object properties, or to
        perform operations when the object is being created.
        In this particular case, the plants array will hold all the
        plants added to the garden. It starts empty."""
        self.name = name
        self.__plants = []
        self.__initial_heights = []
        GardenManager.__gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        """Adds Plant to Garden, ensuring it isn't None.
        Additionaly, record Plant's starting height"""
        if plant is not None:
            self.__plants.append(plant)
            self.__initial_heights.append(plant.get_height())
            print(f"Added {plant.name} to {self.name}'s garden")
        else:
            print(f"Invalid operation attempted: Adding "
                  f"{plant} to Garden [REJECTED]")

    def grow_plants(self) -> None:
        """Makes all Plant's grow 1cm"""
        print(f"{self.name} is helping all plants grow...")
        current_height = 0
        for i in range(len(self.__plants)):
            current_height = self.__plants[i].get_height()
            self.__plants[i].set_height(current_height + 1)
            print(f"{self.__plants[i].name} grew 1 cm")

    def get_plants(self):
        """Returns all Plant's in Garden"""
        return self.__plants

    def print_garden_report(self) -> None:
        """Lists all the plants in the Garden, as well as their information.
        Displays the ammount of Plant's as well as their total growth.
        Finally, enumerates the types of plants in the Garden"""
        print(f"=== {self.name}'s Garden Report ===")
        n_plants = len(self.__plants)
        t_g = 0
        plant_type_normal = 0
        plant_type_flowering = 0
        plant_type_prize = 0
        print("Plants in garden:")
        index = 0
        while index < n_plants:
            print(f"- {self.__plants[index]}")
            t_g += (self.__plants[index].get_height() -
                    self.__initial_heights[index])
            if type(self.__plants[index]) is Plant:
                plant_type_normal += 1
            elif type(self.__plants[index]) is FloweringPlant:
                plant_type_flowering += 1
            elif type(self.__plants[index]) is PrizeFlower:
                plant_type_prize += 1
            index += 1
        print()
        print(f"Plants added: {n_plants}, Total growth: {t_g}cm")
        print(f"Plant types: {plant_type_normal} regular, "
              f"{plant_type_flowering} flowering, "
              f"{plant_type_prize} prize flowers")

    @classmethod
    def create_garden_network(cls):
        """Returns all Gardens in the Garden Network"""
        return cls.__gardens


class GardenStats():

    @staticmethod
    def validate_heights(garden: GardenManager) -> bool:
        """Checks wheter all Plant's height are greater than 0"""
        plant_index = 0
        while plant_index < len(garden.get_plants()):
            if garden.get_plants()[plant_index].get_height() < 0:
                return False
            plant_index += 1
        return True

    @staticmethod
    def get_garden_scores() -> str:
        """Returns string with respective Garden Owners and their Points"""
        gardens = GardenManager.create_garden_network()
        info = ""
        index = 0
        while index < len(gardens):
            info += gardens[index].name + ": "
            scores = 0
            plants = gardens[index].get_plants()
            plant_index = 0
            while plant_index < len(plants):
                if type(plants[plant_index]) is PrizeFlower:
                    scores += plants[plant_index].get_prize_points()
                plant_index += 1
            info += f"{scores}"
            if (index != len(gardens) - 1):
                info += " "
            index += 1
        return info

    @staticmethod
    def get_total_gardens() -> int:
        """Returns number of Gardens managed"""
        return (len(GardenManager.create_garden_network()))


if __name__ == "__main__":
    """This method is the equivalent of the main method.
    It executes when the file is ran as a script,
    but not when it's imported as a module"""
    print("=== Garden Management System Demo ===")
    print()
    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()
    bob = GardenManager("Bob")
    bob.add_plant(PrizeFlower("Dahlia", 45, "pink", 30))
    bob.add_plant(PrizeFlower("Tulip", 40, "red", 25))
    bob.add_plant(PrizeFlower("Petunia", 35, "pink", 42))
    print()
    alice.grow_plants()
    print()
    bob.grow_plants()
    print()
    bob.add_plant(PrizeFlower("Lavender", 15, "purple", 10))
    bob.add_plant(PrizeFlower("Wisteria", 25, "purple", 50))
    print()
    bob.grow_plants()
    print()
    alice.print_garden_report()
    print()
    bob.print_garden_report()
    print()
    print(f"Height validation test: {GardenStats.validate_heights(alice)}")
    print(f"Garden scores - {GardenStats.get_garden_scores()}")
    print(f"Total gardens managed: {GardenStats.get_total_gardens()}")
