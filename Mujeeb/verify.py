def check_unwanted(integer):
    unwanted = []
    wanted = '0123456789'
    if integer == '':
        unwanted.append(True)
    for i in range(len(integer)):
        if i==0 and (integer[i]=='-' or integer[i]=='+'):
            print(f'''
            Negative integer is not allowed''')
            unwanted.append(True)
        elif integer[i] not in wanted:
            unwanted.append(True)
    return unwanted

def verify(integer):    
    result = check_unwanted(integer)
    while True in result:
        print('''
        Your input is not an integer
        ''')
        integer = input('Give me an integer:    ').strip()
        result = check_unwanted(integer)
    return int(integer)