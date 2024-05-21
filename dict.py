chicken = {
    'name': 'gray',
    'breed': 'silky', 
    'eggs': 12,
    'egg_chart' : {
        'M': True,
        'T': True,
        'W': True,
        'TH': True,
        'F': True,
        'S': False,
        'SU': True,
    },
    'coop_mates' : ['butters', 'lindy', 'mac']
}

#  CAN LOOP THROUGH KEYS
print(chicken.keys())

# LOOP THROUGH VALUES 
print(chicken.values())
# GRAB ITEMS
print(chicken.items())


# DICTIONARY METHODS
# .keys()

# .values()

# .items()

# .get(x, default)

# .copy()

# .popitem()

# .clear()

# .fromkeys()

# .update()