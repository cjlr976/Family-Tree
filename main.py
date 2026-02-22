'''
Authors: Chloe Robinson and Camila Fienco
Purpose: 
* Main file to run examples of counting descendants in a family tree
* Prompts user to select example file and person to count descendants for
'''

'''
Recursive case
Purpose: Recursively count number of descendants for a given person in a family tree
'''
def count_descendants(person):

    #Base case
    if not hasattr(person, 'children'):
        return 0
    
    count = len(person.children)

    for child in person.children:
        count += count_descendants(child)
    return count

'''
Recursive case
Purpose: Recursively get names of descendants for a given person in a family tree
'''
def get_descendants(person, descendants):
    if not hasattr(person, 'children'):
        return descendants
    
    for child in person.children:
        descendants.append(child.name)
        get_descendants(child, descendants)
    return descendants

def main():
    print("Select example file to run: ")
    

    print("Input the person you want to count descendants for: ")
    name = input()


if __name__ == "__main__":
    main()