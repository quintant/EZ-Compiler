import os, sys
import time
############################################
filename = os.path.basename(os.path.realpath(sys.argv[0]))
dirname = os.path.dirname(os.path.realpath(sys.argv[0]))
############################################
# os.system("")
os.system("color 5F")
os.system('cd ' + dirname)
os.system('title EZ Compiler')
os.system("cls")
print('Welcome to this simple python script that makes compiling')
print('python programs easier and quicker')
print('################################################')
name_of_script = input('Please type the name of the python script to compile (excluding .py in the end and DO NOT USE SPACES!)  > ') + '.py'



name_of_program = '-n ' + input('please name your .exe file (do not add .exe at the end and DO NOT USE SPACES!)  > ')

icon2 = '-i '
icon3 = input('Please type the full filename of the icon (including the .ico or .icon)  > ')
icon1 = icon2 + icon3 + ' '

compil = 'pyinstaller ' + '-F ' +  icon1 + name_of_program + ' ' + name_of_script
os.system(compil)



