# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇

sum_hight = 0
for hight in student_heights:
  sum_hight += hight
quantity_students = 0
for quantity in student_heights:
  quantity_students += 1

average_hight = round(sum_hight / quantity_students)
print(average_hight) 