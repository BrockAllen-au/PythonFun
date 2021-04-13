# A simple Matlib game. Requests users input and will fill out the pre-made story with their inputs.

print("Please fill in the fields prompted and a story will be printed to you at the end.")

# Gather information and variables to input to the story.
name = input(str("Please enter your name: ")).title()
occupation_night = input(str("Please enter a noun/thing you would do at night: "))
friend_name = input(str("Please enter your best friends name: ")).title()
action_01 = input(str("Enter a verb/action: "))
animal_name = input(str("Enter your pet's name: ")).title()
favourite_colour = input(str("What is your favourite colour? ")).lower()
occupation = input(str("Enter your dream job title: "))
city = input(str("Enter a county/city you would like to visit: ")).title()
favourite_things_01 = input(str("Enter 3 of your favourite hobbies/activities:\n01 - "))
favourite_things_02 = input(str("02 - "))
favourite_things_03 = input(str("03 - "))
noun = input(str("Enter a noun: "))
hated_food = input(str("Enter your most hated food: "))
job_company = input(str("Enter your current job/company: "))

# Create the story and store it as a variable.
story = f"Hi! My name is {name}, and I have a secret to share with you. I'm an average Joe by day and a {occupation_night} by night. " \
        f"Only you and my best friend {friend_name} knows my secret. You may be wondering how this happened? " \
        f"Well, one night I was {action_01} at home, and then BOOM! The lights went out and {animal_name} showed up." \
        f"He/She said in a booming voice, because your favourite colour is {favourite_colour}, you have been chosen to be a {occupation}." \
        f"My mission is to save the people of {city} by doing my favourite things:\n{favourite_things_01}\n{favourite_things_02}\nand {favourite_things_03}.\n" \
        f"This may sound easy, but it is no walk in the park. It requires hard work and {noun}. My weakness is eating {hated_food}. They are gross!" \
        f"I save the world every night, but when I wake up in the morning, I go back to my normal life as a {job_company}."

print(story)
