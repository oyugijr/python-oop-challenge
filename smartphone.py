class Smartphone:
    def __init__(self, brand, model, storage, color):
        # Attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    # Method to display phone details
    def display_details(self):
        return f"{self.brand} {self.model} - {self.storage}GB, {self.color}"

    # Method to make a call
    def make_call(self, number):
        return f"Calling {number}..."

    # Method to take a photo
    def take_photo(self):
        return "Photo taken! 📸"


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, color, gpu):
        # Initialize the base class (Smartphone)
        super().__init__(brand, model, storage, color)
        self.gpu = gpu  # Additional attribute for GamingPhone

    # Overriding the method to add gaming features
    def take_photo(self):
        return f"Gaming phone with {self.gpu} GPU took a photo! 📸"

    # New method for gaming
    def play_game(self, game):
        return f"Playing {game} with smooth graphics on {self.gpu} GPU!"


# Example of creating an object of the GamingPhone class
gaming_phone1 = GamingPhone("ASUS", "ROG Phone 5", 512, "Red", "Adreno 650")
print(gaming_phone1.display_details())
print(gaming_phone1.take_photo())
print(gaming_phone1.play_game("PUBG"))
