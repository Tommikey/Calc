name = input("Enter your name: ")
print("Hello " + name.title() + ','+ " Welcome to my game!")

should_we_play = input("Do you wanna play? ").lower()

if should_we_play == "yes":
    print("Perfect, Let's get started!")
elif should_we_play == "no":
    print("No worries! Have a great day...")
else:
    print("I didn't understand that. Please answer 'yes' or 'no'.")