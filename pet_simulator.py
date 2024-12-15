# Virtual Pet Simulator
# This program allows users to interact with a virtual pet by feeding, playing, or checking its stats. 
# The program ensures the pet's health and happiness are managed effectively.

# Class definition for the Pet
class Pet:
    def __init__(self, name):
        """
        Initialize the pet with default values for hunger, health, and happiness.
        Parameters:
            name (str): Name of the pet provided by the user.
        """
        self.name = name
        self.hunger = 5  # Hunger ranges from 0 (full) to 10 (starving)
        self.health = 10  # Health ranges from 0 (critical) to 10 (optimal)
        self.happiness = 7  # Happiness ranges from 0 (sad) to 10 (joyful)

    def feed(self):
        """
        Simulates feeding the pet. Reduces hunger and slightly boosts health.
        If the hunger is already low, it prevents overfeeding.
        """
        if self.hunger > 0:
            self.hunger -= 3
            self.health += 1
            self.happiness -= 1  # Minor time cost affects happiness
            print(f"{self.name} enjoyed the food!")
        else:
            print(f"{self.name} is already full!")

    def play(self):
        """
        Simulates playing with the pet. Increases happiness but impacts hunger and health.
        """
        self.happiness += 2
        self.hunger += 2
        self.health -= 1  # Playing uses energy
        print(f"{self.name} had a lot of fun!")

    def check_stats(self):
        """
        Displays the current stats of the pet in a readable format.
        """
        print(f"\nPet's Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}\n")

    def is_critical(self):
        """
        Checks if any critical condition is met (hunger, health).
        Returns True if a warning should be displayed.
        """
        if self.hunger >= 10:
            print(f"{self.name} is starving! Feed your pet immediately!")
            return True
        if self.health <= 0:
            print(f"{self.name}'s health has reached zero! Game Over.")
            return True
        return False

# Main program loop
def main():
    """
    Main function to simulate the virtual pet experience.
    Allows the user to interact with the pet through a menu system.
    """
    print("Welcome to the Virtual Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")

    # Create a new Pet object
    my_pet = Pet(pet_name)
    print(f"\n{my_pet.name} is ready to play with you!\n")

    # Main menu loop
    while True:
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Check Stats")
        print("4. Exit")

        # Try-except block to handle invalid inputs
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Menu options
        if choice == 1:
            my_pet.feed()
        elif choice == 2:
            my_pet.play()
        elif choice == 3:
            my_pet.check_stats()
        elif choice == 4:
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        # Check for critical conditions after every action
        if my_pet.is_critical():
            break

# Run the main function if the script is executed
if __name__ == "__main__":
    """
    Entry point of the program. Starts the virtual pet simulation.
    """
    main()
