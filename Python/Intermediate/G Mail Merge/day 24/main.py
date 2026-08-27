with open("text.txt", mode="a") as file:
    file.write("something")
    file.write("\nelse")
with open("../../G Snake Game Two/day 24/sub_directory/text2.txt", mode="r") as file:
    c=file.read()
    print(c)