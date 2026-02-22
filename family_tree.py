'''
Authors: Chloe Robinson and Camila Fienco
Purpose: 
* Defines people in a family tree
* Builds a family tree
* Recursively counts the number of descendants for a given person in a family tree
'''

#Purpose: Define a person in a family tree
class Person:
    def __init__(self, name):
        self.name = name

#Purpose: Add child to family tree
def add_child(self, child):
    if not hasattr(self, 'children'):
        self.children = []
    self.children.append(child)
