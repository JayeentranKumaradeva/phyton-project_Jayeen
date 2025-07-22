# 3. You should have two lists named: adjectives and animals
# 4. Each list should have 6 items. You can come up with your own adjectives and animals.
adjectives = ["Sly", "Stealthy", "Clever", "Mysterious", "Shadowy", "Quick"]
animals = ["Panther", "Eagle", "Fox", "Wolf", "Viper", "Hawk"]

# 1. Ask user their name
user_name = input("Greetings, agent. What is your name? ")

# 5. Randomly choose a codename by combining a random adjective and animal from your list.
import random
random_adjective = random.choice(adjectives)
random_animal = random.choice(animals)
codename = f"{random_adjective} {random_animal}"

# 6. Randomly choose a number from range 1 to 99 as users lucky number!
lucky_number = random.randint(1, 99)

# 7. Finally let the user know their codename and their lucky number.
print(f"Welcome, Agent {user_name}!")
print(f"Your assigned codename is: {codename}")
print(f"And your lucky number for this mission is: {lucky_number}")