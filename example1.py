from family_tree import count_descendants

# Generation 1
grandparent = Person("Grandparent")

# Generation 2
parent1 = Person("Parent1")
parent2 = Person("Parent2")

# Generation 3
child1 = Person("Child1")
child2 = Person("Child2")
child3 = Person("Child3")

family_tree = { 
    "Grandparent": [parent1, parent2],
    "Parent1": [child1, child2],
    "Parent2": [child3],
    "Child1": [],
    "Child2": [],
    "Child3": []
}