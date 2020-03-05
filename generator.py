from sys import argv

filename = argv[1]
with open(filename, "r") as file:
    with open("requirements.txt", "w+") as outfile:
        text = file.read().split("\n")
        for i in text:
            if i[:6] == "import":
                outfile.write("{}\n".format(i.split()[1]))
            if i[:4] == "from":
                if "." in i:
                    outfile.write("{}\n".format(i.split(".")[0].split()[1]))
                else:
                    outfile.write("{}\n".format(i.split()[1]))
