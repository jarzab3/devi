from math import sqrt

def mean(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return (sum / len(lst))

def stddev(lst):
    sum = 0
    mn = mean(lst)
    for i in range(len(lst)):
        sum += pow((lst[i]-mn),2)
    return sqrt(sum/len(lst)-1)

lst = []  
           
print ("Welcome. \n When finish, please type any letter and press enter.") 
num = 1
numbers = []
while (num > 0):
    try:
        number = int(raw_input("Enter numbers: "))
        numbers.append( number );
        print ("current numbers are: ", numbers)
        
    except ValueError:
        input = str(number)
        print (input)
        accept = ('YES', 'Y')
        decline = ('NO', 'N')
        answer = raw_input("Do you want to finish? (yes/y or no/n):\n")
        if answer.strip().upper() in decline:
            #print 'Please enter a number!!!'
            continue
        if answer.strip().upper() in accept:
            break
       
print numbers

print stddev(numbers)