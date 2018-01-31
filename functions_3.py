# Keyword Arguments

def progLangs(**details):
    print(details)  # converts to a dict
    for n, v in details.items():
        print(n, v)


progLangs(Java=9, C=1992, Python=3, JavaScript="ES6")
