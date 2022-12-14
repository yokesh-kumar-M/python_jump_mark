#Python project to print the jump value of student from previous to current ranks

#Function to print the name of student who stood first comparing two set of rank
def NMU(names , marks , updates , n):
    
	#Array of students
    x = [[0 for j in range(3)] for i in range(n)]
    for i in range(n):

        #Store the name of the student
        x[i][0] = names[i]

        #Update the marks of the student
        x[i][1] = marks[i]  +  updates[i]

        #Store the current rank of the student
        x[i][2] = i + 1
        high = x[0]
        for k in range(1, n):
            if (x[k][1] >= high[1]):
                high = x[k]
        #Print the name and jump in rank
        print('Name : ',high[0], ' , jump : ',abs(high[2] - 1),sep="")

#Main code

#Name of the students
names = ['x','y','z']

#Marks of the students
marks = [ 90 , 85 , 89 ]

#Updates that are to be done
updates = [ 0, -9, 10 ]

#Number of students
n = len(marks)
NMU( names , marks , updates , n)
 
