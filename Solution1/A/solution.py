#!/usr/bin/env python

def ParsingNumber():
    squence_num = 12345678910111213141516192021
    number_arry = [int(i) for i in str(squence_num)]
    return number_arry


def IndexOfNumber(value):
    for index,element in enumerate(ParsingNumber(), start=1):
        if index == value:
         print("%dth digit number is: %d" %(index, element))
        
def main():
    number = input("Please input your number: ")
    number = int(number)
    IndexOfNumber(number)


if __name__ == "__main__":    
    main()
