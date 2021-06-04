#!/usr/bin/env python
import sys

class Tower:
    def __init__(self, name, list):
        self.name = name
        self.list = list

    # add disk to tower
    def append(self, disk):
        self.list.append(disk)

    # move disk from self to dest
    def move(self, disk, dest):
        self.list.remove(disk)
        dest.list.insert(0, disk)
    
    # print the disks
    def show(self):
        print(self.list)

    # overload "-", A-1 => A.list[0] 
    def __sub__(self, a):
        return self.list[a-1]

# recurrsive function for solving Hanoi problem
def Hanoi(n, src, aux, dst):
    global steps 
    steps += 1
    if n == 1:
        print("Move plate {n} from {src} to {dst}." .format(n=n, src=src.name, dst=dst.name))
        src.move(n, dst)
        Show(Towers)  

    else:
        Hanoi(n-1, src, dst, aux)
        print("Move plate {n} from {src} to {dst}." .format(n=n, src=src.name, dst=dst.name))
        src.move(n, dst)
        Show(Towers)
        Hanoi(n-1, aux, src, dst)

# show the status of all Towers
def Show(list):
    for element in list:
        element.show()         

# main function
def main(x):
    A = Tower("A", [i+1 for i in range(x)])
    Towers.insert(0, A)
    Hanoi(x, A, B, C)
    print("\nTotal step: {}" .format(steps))

# global declaration
B = Tower("B", [])
C = Tower("C", [])
Towers = [B, C]
steps = 0

# take 1 argument as the total number of disks
if __name__ == "__main__":
    main(int(sys.argv[1]))
