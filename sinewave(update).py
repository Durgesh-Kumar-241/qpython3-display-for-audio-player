"""
License

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


__author__='Durgesh Kumar,MNNIT ALLAHABAD'
__copyright__='all rights reserved by Qpython:Python for ANDROID:durgesh-kumar-241(Github)'
'''display for audio player'''
'''fill screen with random bars'''
'''first play your favorite audio song in background,then run the script,rotate your device'''
import time


import random

import os


      
while True:   
    for i in range(1,100):
        for j in range (1,5):
            print(f"\033[1;%d;40m "%(random.randint(30,36)))
           
        for j in range (1,random.randint(1,17)):
            print('%',end='%')
            
        print(f"\033[1;%d;40m "%(random.randint(30,36)))
        for j in range (1,5):
            print('|')
           
        for j in range (1,random.randint(1,17)):
            print('%',end='%')
            
        print(f"\033[1;%d;40m "%(random.randint(30,36)))
        for j in range (1,5):
            print('|')
           
        for j in range (1,random.randint(1,17)):
            print('%',end='%')
            
        print(f"\033[1;%d;40m "%(random.randint(30,36)))
        for j in range (1,5):
            print('|')
           
        for j in range (1,random.randint(1,17)):
            print('%',end='%')
            
        print(f"\033[1;%d;40m "%(random.randint(30,36)))
        
        for j in range (1,5):
            print('|')
           
        for j in range (1,random.randint(1,17)):
            print('%',end='%')
            
        print(f"\033[1;%d;40m "%(random.randint(30,36)))
        for j in range (1,5):
            print('|')
           
        for j in range (1,random.randint(1,17)):
            print('%',end='%')
            
        print(f"\033[1;%d;40m "%(random.randint(30,36)))
        
        time.sleep(random.randint(1,10)/90)
        os.system("clear")  
    
    