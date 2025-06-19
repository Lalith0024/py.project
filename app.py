import random
from headlinedata import subjects, actions, places

def get_random_headline(category):
    subject = random.choice(subjects.get(category, subjects["random"]))
    action = random.choice(actions)
    place = random.choice(places)
    return f"BREAKING: {subject} {action} {place}!"

def get_personalized_headline(name):
    action = random.choice(actions)
    place = random.choice(places)
    return f"EXCLUSIVE: {name} {action} {place}!"

def main():
    print("🗞️ Welcome to the FAKE HEADLINER GENERATOR! 🗞️\n")

    while True:
        print("\nChoose an option:")
        print("1. Generate Random Headline")
        print("2. Generate Personalized Headline")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("\nCategories: politics, sports, bollywood, food, random")
            category = input("Enter category: ").strip().lower()
            print("\n" + get_random_headline(category))

        elif choice == "2":
            name = input("Enter your name: ").strip().capitalize()
            print("\n" + get_personalized_headline(name))

        elif choice == "3":
            print("👋 Goodbye! Hope you enjoyed the fake news headlines!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
