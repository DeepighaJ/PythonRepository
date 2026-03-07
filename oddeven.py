import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip()) #removing trailing spaces and convert as int

    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print('Wierd')
        else:
            print("Not Weird")
    else:
        print("Weird")

        #or do the below chat gpt code

    #if n % 2 != 0:  # odd number
        #print("Weird")
    #elif n % 2 == 0 and 2 <= n <= 5:
        #print("Not Weird")
    #elif n % 2 == 0 and 6 <= n <= 20:
       # print("Weird")
    #elif n % 2 == 0 and n > 20:
      #  print("Not Weird")