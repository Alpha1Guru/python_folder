def show_magicians(magicians):
    """ prints the name of each magicians in the list"""
    for magician in magicians:
        print(f"What a wonderful performance {magician.title()}!")
def make_great(normal_magicians):
    """ adds great to the magicians"""
    ## This won't work 
    # for magician in magicians:
    #     great_magician = "Great " + magician
    # This will work
    for magician_no in range(len(normal_magicians)):
        normal_magicians[magician_no] = "Great " + normal_magicians[magician_no]
magicians = ["May","Eric","Clavy","Kalix","Mirah","Fonto"]
show_magicians(magicians)
make_great(magicians[:])
show_magicians(magicians)