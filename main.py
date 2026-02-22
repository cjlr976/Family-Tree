'''
Authors: Chloe Robinson and Camila Fienco
Purpose: 
* Defines load and main function
'''

from family_tree import Tree

#Purpose: Loads trees from example.txt file
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
Purpose: User interface to select tree and query relationships
'''
def main():
    tree_choice = input("Select family tree (1-5): ")

    if tree_choice not in ["1", "2", "3", "4"]:
        print("Invalid tree selection.")
        return

    tree = load_tree("example.txt", tree_choice)

    print(
        "Options:\n1. List Descendants\n2. List Ancestors\n3. Number of Descendants\n 4. Number of Ancestors\n"
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
        name = input("Enter person name: ")

        if name in tree.people:
            person = tree.people[name]
            print(tree.count_descendants(person))
        else:
            print("Person not found.")

    elif option == "4":
        name = input("Enter person name: ")

        if name in tree.people:
            person = tree.people[name]
            print(tree.count_ancestors(person))
        else:
            print("Person not found.")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()