range_start = int(input ("Please, Enter the Lowest Range Value: "))  
range_end = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers are: ")  
for number in range (range_start, range_end + 1):  
    if number > 1: 
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  