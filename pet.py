
# Base Pet Class
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

# Derived Dog Class
class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color
        self.preferences = ("Bones", "Walk")

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.color}, Preferences: {self.preferences}")

# Derived Cat Class
class Cat(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.color = color
        self.preferences = ("Fish", "Naps")

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.color}, Preferences: {self.preferences}")

# Pet Management System
class PetAdoptionSystem:
    def __init__(self):
        self.pets = {}  # Dictionary to store pets with pet_id as key

    def add_pet(self, pet):
        pet_id = random.randint(1000, 9999)
        while pet_id in self.pets:
            pet_id = random.randint(1000, 9999)
        self.pets[pet_id] = pet
        print(f"Pet added successfully with ID: {pet_id}")

    def view_pets(self):
        if not self.pets:
            print("No pets available for adoption.")
        for pet_id, pet in self.pets.items():
            print(f"\nPet ID: {pet_id}")
            pet.display_info()

    def adopt_pet(self, pet_id):
        if pet_id in self.pets:
            adopted_pet = self.pets.pop(pet_id)
            print(f"Congratulations! You have adopted {adopted_pet.name}.")
        else:
            print("Invalid pet ID. Please try again.")

# Menu
def run_system():
    system = PetAdoptionSystem()

    while True:
        print("\n--- Pet Adoption Menu ---")
        print("1. View Available Pets")
        print("2. Add a Pet")
        print("3. Adopt a Pet")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            system.view_pets()

        elif choice == "2":
            species = input("Enter species (Dog/Cat): ").capitalize()
            name = input("Enter pet's name: ")
            age = int(input("Enter pet's age: "))
            breed = input("Enter breed: ")
            color = input("Enter color: ")

            if species == "Dog":
                pet = Dog(name, age, breed, color)
            elif species == "Cat":
                pet = Cat(name, age, breed, color)
            else:
                print("Invalid species. Only 'Dog' or 'Cat' allowed.")
                continue

            system.add_pet(pet)

        elif choice == "3":
            try:
                pet_id = int(input("Enter Pet ID to adopt: "))
                system.adopt_pet(pet_id)
            except ValueError:
                print("Invalid input. Please enter a valid Pet ID.")

        elif choice == "4":
            print("Exiting Pet Adoption System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

# Start the system
run_system()
