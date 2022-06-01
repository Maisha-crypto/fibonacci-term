# Fibonacci Algorithm Program

## Table of Contents

* [Introduction](#Introduction)
* [Problem description](#problem-description)
* [How the program works](#how-the-program-works)
* [Error checking](#error-checking)
* [Required libraries](#required-libraries)


## Introduction

A Fibonacci sequence is described by the recurence relation:

F_n = F_(n-1) + F_(n-2), where F_1 = 1, F_2 = 1.

Example of the first 12 terms of the sequence:

F_1 = 1

F_2 = 1

F_3 = 2

F_4 = 3

F_5 = 5

F_6 = 8

F_7 = 13

F_8 = 21

F_9 = 34

F_10 = 55

F_11 = 89

F_12 = 144

### In the sequence:

* The 7th term is the first term to contain two digits.
* The 12th term is the first term to contain 3 digits.

## Problem Description

The task at hand was to write a program that is able to generate the Fibonacci sequence and find the first term to have N digits, where N is passed in on the command line.

## How the program works

The program allows a user to enter a value ***N***, where ***N*** respresents the number of digits in a Fibonacci term. 


* ### Generating the Fibonacci sequence

    * A fibonacci_sequence function is created to generate the fibonacci sequence. In the function, a while loop is used to generate Fibonacci terms until the first term to have N digits is found.

    * Once the term with N digits is found, a boolean variable is used to terminate the while loop.

* ### Finding the first term to contain ***N*** digits

    * A Get_Number_of_Digits function is called for every while loop itteration. This function checks and returns the number of digits in each fibonacci term.

    * This function makes use of the base 10 logarithmic function to check for number of digits. 

## Error Checking

A few error generating scenarions where taken into concideration during the development of the program.

* User enters a negative value ***(N<0)*** in the command line, the program prompts the user to "enter a positive intiger".

* User enters a value ***(N=0)***, since an intiger cannot have 0 digits. The program prompts the user to enter a value N > 0.

* User enters a string or nothing in the command prompt. The program promts the user to enter an intiger value to support mathematical operations.

* The program crashes for N > 20, because the fib term is too long for the log function


## Required Libraries

* Python v:3.10.4 was used while building the docker image "fibonacci-term"

* Installation of numpy is a pre-requisite to run this program.

* To run the docker file in interactive mode use the ***"docker run -t -i fibonacci-term"***


