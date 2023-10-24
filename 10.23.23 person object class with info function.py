class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f"{self.name}s age is {self.age}"

# P string
# R string describing what was added as the new class
# E Jimbo, 33 -> Jimbos age is 33
# P self goes in the __init__(), can use f"{}" to make the text as needed, could use @property instead of just adding the property to the __init__()
# would create new function for the property info like def info(self): return f"{self.name}s age is {self.age}"