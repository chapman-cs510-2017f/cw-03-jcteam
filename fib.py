#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Cynthia Parks
# Student ID: 2299636, 2303535
# Email: gardnerh@chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 3
###

from sequences import fibonacci
import sys

def main(local_argv):
    x = local_argv
    try:
        type(x) == int
        
    except ValueError:
        print("Invalid input")
        
    print(fibonacci(x)[-1])
    return(fibonacci(x)[-1])

if __name__ == "__main__":
    main(sys.argv)