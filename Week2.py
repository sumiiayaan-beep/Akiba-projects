#student result hard code
student="Emi poster"
phyton="50"
english="70"
mathematics="87"
history="85"
geography="65"
 # arthimetic
total_points = int(mathematics) + int(english) + int(history) + int(geography) + int(phyton)
            
number_of_subjects = 5
average_points = total_points / number_of_subjects


# 4. Display the formatted summary
print("\n" + "="*40)
print(f"            STUDENT RESULT                   ")
print("="*40)
print(f"Student   : {student}")
print("-"*40)
print(f"Total Points   : {total_points:.2f}")
print(f"Average Points : {average_points:.2f}")
print("="*40)

