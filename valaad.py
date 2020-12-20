#AAdhar number validation program



mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
		[1, 2, 3, 4, 0, 6, 7, 8, 9, 5], 
		[2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], 
		[4, 0, 1, 2, 3, 9, 5, 6, 7, 8], 
		[5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], 
		[7, 6, 5, 9, 8, 2, 1, 0, 4, 3], 
		[8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
		
perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
		[1, 5, 7, 6, 2, 8, 3, 0, 9, 4], 
		[5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], 
		[9, 4, 5, 3, 1, 2, 6, 8, 7, 0], 
		[4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], 
		[7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]


def Validate(aadharNum):
    try:
        i = len(aadharNum)
        j = 0
        x = 0

        while i > 0:
            #print('i = ', i)
            i -= 1
            x = mult[x][perm[(j % 8)][int(aadharNum[i])]]
            j += 1
            #print('x = ',x)
        if x == 0:
            return '----- Valid Aadhar Number -----'
        else:
            return 'xxxxx Invalid Aadhar Number xxxxx'

    except ValueError:
        return 'xxxxx Invalid Aadhar Number xxxxx'
    except IndexError:
        return 'xxxxx Invalid Aadhar Number xxxxx'


print("Use exit or Ctrl + C to exit")

while True:
    aadharNum = input("\nEnter 12 digit aadhar number : ")
    if aadharNum == 'exit':
        break
    elif (len(aadharNum) == 12 and aadharNum.isdigit()):
        print(Validate(aadharNum))
    elif (len(aadharNum) != 12):
        print("\nNot a 12 digit number")
    elif(aadharNum.isalpha()):
        print("\nCannot contain characters")
    elif( aadharNum.isalnum()):
        print("\nEnter only digits")		
    else:
        print('xxxxx Invalid Aadhar Number xxxxx')