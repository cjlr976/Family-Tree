'''
Authors: Chloe Robinson and Camila Fienco
Purpose: 
* Defines load and main function
'''

from family_tree import Tree

def load_tree(filename, tree_number):
    tree = Tree()
    current_tree = None

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Detect tree section
            if line.startswith("TREE"):
                current_tree = line.split()[1]
                continue

            # Skip if not selected tree
            if current_tree != str(tree_number):
                continue

            # Process person lines
            if line.startswith("PERSON:"):
                name = line.split(":")[1].strip()
                tree.add_person(name)

            # Process relationship lines
            elif line.startswith("CHILD:"):
                parts = line.split(":")[1].strip()
                parent_name, child_name = parts.split("->")
                tree.add_relationship(parent_name.strip(), child_name.strip())

    return tree


'''
Purpose:
* Load family tree from file

'''
def main():
    tree_choice = input("Select family tree (1-5): ")

    if tree_choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid tree selection.")
        return

    tree = load_tree("example.txt", tree_choice)

    print(
        "\n1. Get descendants\n"
        "2. Get ancestors\n"
        "3. Get relationship"
    )

    option = input("Enter option: ")

    if option == "1":
        name = input("Enter person name: ")

        if name in tree.people:
            person = tree.people[name]
            print(tree.get_descendants(person))
        else:
            print("Person not found.")

    elif option == "2":
        name = input("Enter person name: ")

        if name in tree.people:
            person = tree.people[name]
            print(tree.get_ancestors(person))
        else:
            print("Person not found.")

    elif option == "3":
        name1 = input("Enter first person: ")
        name2 = input("Enter second person: ")

        if name1 in tree.people and name2 in tree.people:
            p1 = tree.people[name1]
            p2 = tree.people[name2]
            print(tree.get_relationship(p1, p2))
        else:
            print("One or both persons not found.")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()