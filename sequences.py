#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Cynthia Parks
# Student ID: 2299636, 2303535
# Email: gardnerh@chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 3
###



# This is the body of the module.  Place all global constants, function 
# definitions, and class definitions here.  No free-floating executable
# code should appear in a module.

# Minimize the use of global constants like this one.
#CONSTANT1 = 0


def fibonacci(x):
    """Function docstring
    The fibonacci() function will take in a value x and give the numbers in the
    fibonacci sequence up to the x number.
    
    Args:
        x(int): parameter 1
    
    Returns:
        fiblist: The list of fibonacci sequence numbers up to the input value
    """
    if x > 1:
        try:
            fiblist = [1]
            a,b = 1,1
            for i in range(x-1):
                a,b = b, a+b
                fiblist.append(a)
            return fiblist
        except:
            #error
            return



# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

#if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
#    import sys
#    main(sys.argv)