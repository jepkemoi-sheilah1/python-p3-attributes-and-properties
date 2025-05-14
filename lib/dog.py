#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name=None,breed=None):
        if isinstance(name, str) and len(name) > 0 and len(name) < 25:
            self.name = name
        elif name is not None:
            print("Name must be string between 1 and 25 characters.")

        

        if breed in APPROVED_BREEDS:
            self.breed = breed
        elif breed is not None:
            print("Breed must be in list of approved breeds.")
       
    
dog1 = Dog("Fido", "Pug")

     
        
        