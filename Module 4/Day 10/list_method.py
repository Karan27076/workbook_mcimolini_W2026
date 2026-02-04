grades = [87, 53, 18, 29, 94]

print(f"Grades: {grades}")


#Sort out list:
grades.sort()

print(f"Sorted grades: {grades}")

# reverse sort
grades.sort(reverse=True)
print(f"Reverse sorted grades: {grades}")

#add items (append)
grades.append(100)
print(f"Longer list: {grades}")

#sort again after add
grades.sort()

# .insert(index, value)
grades.insert(3, 57)
print(f"Inserted list: {grades}")

# remove items by POP
#.pop(index)
popped_grade = grades.pop(3)
print(f"Shortened list: {grades}")
print(f"Popped: {popped_grade}")

# .remove(value) removes the first instance
grades.append(100)
print(f"Grades before remove: {grades}")

grades.remove(100)
print(f"Grades after remove: {grades}")

# to make remove safe, we need to check for values exits first
# 'In' can be used for that, and returns true or false if checked
if 0 in grades:
    print("Someone got 0!")
elif 100 in grades:
    print("Someone got 100!!!")

is_found = 100 in grades
if is_found:
    print("Hurrah!")


if 100 in grades:
    grades.remove(100)
print(f"{grades}")



