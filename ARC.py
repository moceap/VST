#!/usr/bin/env python3

#########################
# UPM Python Tester 0.1 #
# By                    #
# Mosaab Alzoubi        #
# Mohammad Bayazid      #
# Khaled Redhwan        #
# Moayad Shbair         #
#########################

## THE SAMPLE - ADMISSION RATE CALCULATOR ##

import sys

ver = "0.1"

def help():
    print("\n -=-= ADMISSION RATE CALCULATOR %s =-=-\n\n \
    USAGE:\n \n \
    arc [Secondary school] [Qudrat] [Tahseeli]\n \
    \n You should enter three integers." % ver)

if len(sys.argv) != 4:
    help()
    quit()

if not (sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[3].isdigit()):
    help()
    quit()

highSchoolGrade = int(sys.argv[1])
QudaratGrade = int(sys.argv[2])
TahsiliGrade = int(sys.argv[3])



if (highSchoolGrade > 100 or QudaratGrade > 100 or TahsiliGrade > 100):
    print('grades cannot exceed 100 peease re-enter your grades')
    sys.exit()
    
if (highSchoolGrade < 0 or QudaratGrade < 0 or TahsiliGrade < 0):
    print('grades cannot be less than 0 peease re-enter your grades')
    sys.exit()
        
cumulativeAR = (0.4*highSchoolGrade+0.3*QudaratGrade+0.3*TahsiliGrade)
print("Your Cumulative AR is: "+ str(cumulativeAR))

if (cumulativeAR > 90):
    print("You can register in College of Engineering, College of Computer Science, and College of Business Management")

elif (cumulativeAR > 80):
    print("You can register in College of Computer Science and College of Business Management")

elif (cumulativeAR > 70):
    print("You can only register in College of Business Management")

else:
    print("Sorry, your AR does not allow you to register in any of our programs")

print("Good Luck!")
    