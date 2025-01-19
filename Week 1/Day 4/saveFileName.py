def saveName():
    name = input("Enter your name: ")
    with open("./name.txt", "w") as f:
        f.write(name)

    with open("./name.txt", "r") as f:
        print(f.read())

saveName()