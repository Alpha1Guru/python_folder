class Verify:
    """PIUS PLS DO NOT DEL THIS CODE I WANT TO COLLECT IT FROM YOU COS THIS ONE DIFFERENT FROM THE ONE
    ON MY SYSTEM AND DON'T YET WRITE DOC STRING IF YOU HAVEN'T SEND IT😂🤣😉😉
    """
    
    wanted = '0123456789'
    unwanted = ''
    period_checker = 0
    
    def pint(self, user_input:str):
        if user_input == '':
            print(f">>>> EMPTY INPUT PROVIDED <<<<", end='\n\n')
            new_input = input(f"TRY AGAIN:  ")
            return self.pint(new_input)

        else:
            for char in user_input:
                if (user_input[0] == '+' or user_input[0] == '-'):
                    continue
      
                elif char in self.wanted:
                    continue
                    
                else:
                    print(f">>>> INVALID INPUT PROVIDED <<<<", end='\n\n')
                    new_input = input(f"TRY AGAIN:  ")
                    return self.pint(new_input)
                
            return int(user_input)
        

    def pfrac(self, user_input:str):
        
        if '.' in user_input:
            for char in user_input:
                if char == '.':
                    self.period_checker +=1
                    continue
                
            if self.period_checker > 1:
                self.period_checker = 0
                print(f">>>> INVALID INPUT PROVIDED <<<<", end='\n\n')
                new_input = input(f"TRY AGAIN:  ")
                user_input = new_input
                return self.pfrac(new_input)
                
            else:
                splitted_user_input = user_input.split('.')
    
                for char in splitted_user_input:
                    if user_input[0] == '-' or user_input[0] == '+':
                        continue
                    elif char not in self.wanted:
                        print(f">>>> INVALID INPUT PROVIDED <<<<", end='\n\n')
                        new_input = input(f"TRY AGAIN:  ")
                        return self.pfrac(new_input)                        

                return float(user_input)

        else:
            print(f">>>> FRACTIONAL NUMBER REQUIRED ONLY <<<<", end='\n\n')
            new_input = input(f"TRY AGAIN:  ")
            return self.pfrac(new_input)                        
            


val = input(f"Give me your number:  ")
instance1 = Verify()
print(instance1.pfrac(val))