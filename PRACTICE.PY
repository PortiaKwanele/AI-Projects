#creating a list with student names
students = ["Abraham (ID : 678)", "Jollof (ID : 5678)", "Ryan (ID : 345)"]
print(students)

#Adding the five students to the beginning of the list:insert cmd
students.insert(0, "Portia (ID : 5647)")
students.insert(0, "Hilary (ID : 67589)")
students.insert(0, "Kwanele  (ID : 3467)")
students.insert(0, "Tafadzwa (ID : 5647)")
students.insert(0, "Layla  (ID : 5647)")
print(students)

#Adding John to the end of the list :append cmd
students.append("John (ID : 673)") 
print(students)

# cHECKING IF eLIZABETH IS A PART OF THE STUDENTS LIST
if "Elizabeth" in students :
    indexElizabeth = students.index("Elizabeth")#position of elizabeth
    indexElizabeth != -1 and indexElizabeth < len(students) - 1 
    del students[indexElizabeth + 1]
elif students.index("Elizabeth")    :
    print("Elizabeth is not part of the students list")
    
students.insert(0, "Elizabeth (ID : 673)")
   

        