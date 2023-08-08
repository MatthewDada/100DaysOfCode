# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("day 21-30\mail merge\Input\Letters\starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("day 21-30\\mail merge\\Input\\Names\\invited_names.txt") as names_list:
    names = names_list.readlines()

# print(names)
# print(letter)

name_of_guests = []
for name in names:
    name_of_guests.append(name.replace("\n", ""))
print(name_of_guests)


for name in name_of_guests:
    with open(f"day 21-30/mail merge/Output/ReadyToSend//{name}.txt", 'w') as letter_done:
        letter_done.write(letter.replace("[name]", name))
