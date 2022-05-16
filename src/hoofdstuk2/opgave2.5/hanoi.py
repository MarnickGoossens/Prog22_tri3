import pygame, time

lagen = int(input("Hoeveel lagen"))

"""
Recursive function to solve towers of Hanoi
"""


def towers_of_hanoi(n, source, destination, extra):
    if n == 1:
        print(f"Move disk {n} from tower {source} to tower {destination}")
    towers_of_hanoi(n - 1, source, extra, destination)
    print(f"Move disk {n} from tower {source} to tower {destination}")
    towers_of_hanoi(n - 1, source, destination, extra)


"""
Driver code
"""
n_disks = 3

# # To be used when visualising
# from visualise_hanoi import *
# make_disks(n_disks)
# update_visuals()
# time.sleep(2)

towers_of_hanoi(n_disks, "A", "C", "B")
