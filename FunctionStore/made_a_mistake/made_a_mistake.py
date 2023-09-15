def made_a_mistake(func, *args, **kwargs):
    """Reruns a function when a mistake is made
    """    
    def func_type():
        """Determines the number and type of arguments passed to the function
        """        
        if args:
            if kwargs:
                return func(*args, **kwargs)
            else:
                return func(*args)
        elif kwargs:
            return func(**kwargs)
        else:
            return func()

    while True:
        mistake = input("Made a mistake? [y/n]: ").strip()
        if mistake.lower() == "y":
            return func_type()
        elif mistake.lower() == "n":
            print("Done!\n")
            return None
        else:
            print("Didn't catch that")