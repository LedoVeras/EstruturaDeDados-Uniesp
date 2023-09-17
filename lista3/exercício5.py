def primo(num:int):
    for l in range(2 , num):
        if(num % l == 0):
            return False
    
    return True