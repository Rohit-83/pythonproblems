#Tower of hanoi problem
'''
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzleis to move the entire stack to another rod, obeying the following simple rules: 

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.

'''

def TowerOfHanoi(n,first_rod,last_rod,helper_rod):
    if n == 1:
        print("move disk 1 from rod",first_rod,"to rod",last_rod)
        return
    TowerOfHanoi(n-1,first_rod,helper_rod,last_rod)
    print("move disk",n,"from rod",first_rod,"to rod",last_rod)
    TowerOfHanoi(n-1,helper_rod,last_rod,first_rod)


print(TowerOfHanoi(3,"A","C","B"))
