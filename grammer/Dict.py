import pickle


def main():
    nations = get_dictionary(R"C:\Users\Coding-Kai\Desktop\UNdict.txt")
    nation = input_name_of_nation(nations)
    display_data(nations, nation)


def get_dictionary(filename):
    infile = open(filename, "rt", encoding='utf-8')
    nations = pickle.load(infile)
    infile.close()
    return nations


def input_name_of_nation(nations):
    nation = input("Enter the name of a UN member nation:")
    while nation not in nations:
        print("%s is not a member of the UN .Try again." % nation)
        nation = input("Enter the name of a UN member nation:")
    return nation


def display_data(nations, nation):
    print("Continent:", nations[nation]["cont"])
    print("Population:", nations[nation]["population"])
    print("Area:", nations[nation]["area"])


main()
