'''
Authors: Chloe Robinson and Camila Fienco
Purpose: 
* Defines people in a family tree
* Builds a family tree using an adjacency list
* Recursively find a given person relationshisp in teh tree shuch as descendants, ancestors, and common ancestors   
'''

#Purpose: Define a person in a family tree
class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

class Tree:
    def __init__(self):
        self.people = {}

    #Adds person to tree
    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    #Adds relationship between a parent and child
    def add_relationship(self, parent_name, child_name):
        parent = self.people[parent_name]
        child = self.people[child_name]
        parent.add_child(child)

    #Function: Count Descendants
    def count_descendants(self, person):
        # Base case
        if not person.children:
            return 0

        count = 0

        # Recursive case
        for child in person.children:
            count += 1 + self.count_descendants(child)

        return count

    # Function: Get Descendants
    def get_descendants(self, person):
        descendants = []

        # Base case
        if not person.children:
            return []

        # Recursive case
        for child in person.children:
            descendants.append(child.name)
            descendants.extend(self.get_descendants(child))

        return descendants
    
    #Function: Count Ancestors
    def count_ancestors(self, person):
        # Base case
        if not person.parents:
            return 0

        count = 0

        # Recursive case
        for parent in person.parents:
            count += 1 + self.count_ancestors(parent)

        return count

    # Function: Get Ancestors
    def get_ancestors(self, person):
        ancestors = []

        # Base case
        if not person.parents:
            return []

        # Recursive case
        for parent in person.parents:
            ancestors.append(parent.name)
            ancestors.extend(self.get_ancestors(parent))

        return ancestors