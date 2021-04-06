'''Given an integer N, the task is to check whether the given number is a pangram or not. 
Note: A Pangram Number contains every digit [0- 9] at least once.'''

def pangram(num):

    n = str(num)
    new_set = set(n)

    if len(new_set)==10:
        return True
    return False

N = 103876540022
print(pangram(N))
        
    
