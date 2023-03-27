PLACEHOLDER = "[name]"
# read names from invited names as list
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

# for each name create separate letter with their name
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
