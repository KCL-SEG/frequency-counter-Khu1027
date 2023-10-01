"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        key = str(item)
        #checks if the key exists
        if frequencies.get(key) == None:
            frequencies.update({key: 1})
        else:
            frequencies.update({key: frequencies.get(key)+1})
    return frequencies
