with open("Input/Names/invited_names.txt") as name_file:
    name_list=name_file.readlines()
with open("Input/Letters/starting_letter.txt") as template_file:
    letter_template=template_file.read()
for name in name_list:
        recipient_name = name.strip()
        letter=letter_template.replace("[name]",recipient_name)
        with open(f"Output/ReadyToSend/{recipient_name}.txt",mode="a") as letter_file:
            letter_file.write(letter)
