def show_magicians(magicians):
    """ prints the name of each magicians in the list"""
    for magician in magicians:
        print(f"What a wonderful performance {magician.title()}!")
magicians = ["May","Eric","Clavy","Kalix","Mirah","Fonto"]
show_magicians(magicians)