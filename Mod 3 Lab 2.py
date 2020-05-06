"""
CTEC 121
Ilya Panasevich
Module 3 Lab 2
Class demos
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    try:
        print(4/0)
    except ZeroDivisionError:
        print("\nThere was a divide by zero error. Exiting\n")
        exit
    except:
        print("\nunknown exception\n")
        exit
    

main()    