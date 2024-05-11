# input
student_score = 80

# Process: Your Solution Code Here
num_input = input("Enter score =  ")
num = int(num_input)
grade = " "

if num >= 80 :
    grade = "A"
elif num >= 65 :
    grade = "B+"
elif num >= 50 :
    grade = "B"
elif num >= 35 :
    grade = "C"
else :
    grade = "D"

# Output "Nilai A"
print("with the num" , num , "will give grade" , grade)