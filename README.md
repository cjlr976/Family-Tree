Author: Chloe Robinson & Camila Fienco

## Problem Selection
1. Given a family tree, use recursion to find the number of descendants a person has
## Recursive Design
### Base Case

### Recursive Case
### Why Recursion is Appropriate

## Implementation

### Family Tree
1. Each node represents a person
2. Each node contains a list of children
3. Each child is the root of a smaller family tree

example.py
```json

```

## Analysis
### Time complexity (Big-Oh notation)
### Space complexity (recursion stack)
### Worst-case analysis

## Testing
### Sample imputs and outputs
### Edge cases

## Deployment
Windows CMD
```
docker exec -it postgresql-server-container psql -U postgres
```
```
uvicorn main:app --reload
```