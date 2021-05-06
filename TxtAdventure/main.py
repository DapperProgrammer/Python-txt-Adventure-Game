import CromStory
import AmoraStory

print("Hello and welcome to (insert name here)!", "\n"
      "Select your character!" "\n")

characterSelectionMenu = "Crom", "Amora"

print(characterSelectionMenu, "\n")

while True:
    userCharacterSelect = input("Enter character name: ")
    if userCharacterSelect.capitalize() == "Crom":
        CromStory.cromAdventure()
        break
    elif userCharacterSelect.capitalize() == "Amora":
        AmoraStory.amoraAdventure()
        break
    else:
        print("Invalid entry.")