student_name = "Bryant Dickerson"
current_gpa = 4.0
study_hours = 112
social_points = 50
stress_level = 50
# social_points was evaluated on a scale of 0-50.
# stress_level was evaluated on a scale of 0-100.
# TEST CASE 1 PRINTS
print(f"Student Name: {student_name}")
print(f"Current GPA: {current_gpa:.2f}")
print(f"Study hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")


# TEST CASE 2 CODE
diff_choice = input("Choose the difficulty of your course: ")
easy_mode = "Easy Difficulty: 12 Credits"
medium_mode = "Medium Difficulty: 15 Credits"
hard_mode = "Hard Difficulty: 18 Credits"


# TEST 2 Prints
print("")
print(diff_choice)
print("")
if diff_choice == "Easy":
    print(f"Mode chosen: {easy_mode}")
    print(f"Current GPA: {current_gpa}")
    print(f"Study hours: {study_hours}")
    print(f"Social Points: {social_points + 20}")
    print(f"Stress Level: {stress_level - 30}")
elif diff_choice == "Medium":
    print(f"Mode chosen: {medium_mode}")
    print(f"Current GPA: {current_gpa}")
    print(f"Study hours: {study_hours}")
    print(f"Social Points: {social_points - 20}")
    print(f"Stress Level: {stress_level + 15}")
elif diff_choice == "Hard":
    print(f"Mode chosen: {hard_mode}")
    print(f"Current GPA: {current_gpa}")
    print(f"Study hours: {study_hours + 12}")
    print(f"Social Points: {social_points - 25}")
    print(f"Stress Level: {stress_level + 25}")
else:
    print("Invalid Choice: Choose again.")

# TEST CASE 3 CODE
# SIDE NOTE: In zyBooks, Test Case 3 kept failing for me, and I still have no idea why. Maybe I missed a couple of similar inputs.
studying_ops = ["COMP 163", "MATH 110", "HIS 106", "ENG 101"]
study_choice = input("Which Class do you want to study for?: ")
print("")
print(studying_ops)
print("")
print("If COMP 163 (OR MATH 110) is chosen: ")
print(f" Weekly Study hours: {study_hours - 25} hours left.")
print(f"Social Points: {social_points - 30} Social points left.")
print("")
print("If HIS 106 is chosen: ")
print(f"Possible Study hours loss: {study_hours - 15} hours left.")
print(f"Possible Social Points loss: {social_points - 8} Social points left.")
if study_choice in studying_ops:
    if study_choice not in studying_ops:
        print("Not an available class.")
    elif study_choice == "COMP 163":
        print(f" Weekly Study hours: {study_hours - 20} hours left.")
        print(f"Social Points: {social_points - 20} Social points left.")
    elif study_choice == "MATH 110":
        print(f" Weekly Study hours: {study_hours - 24} hours left.")
        print(f"Social Points: {social_points - 22} Social points left.")
    elif study_choice == "HIS 106" and current_gpa >= 3.5:
        print(f"Weekly Study hours: {study_hours - 15} hours left.")
        print(f"Social Points: {social_points - 7} Social points left.")
    elif study_choice == "ENG 101" or (study_choice == "HIS 106" and current_gpa >= 3.5):
        print(f"Weekly Study hours: {study_hours - 9} hours left.")
        print(f"Social Points: {social_points - 12} Social points left.")
    elif study_choice not in studying_ops:
        print("Not an available class.")
    if study_choice != "COMP 163" or "MATH 110":
        print("You're probably better off studying for COMP 163 or MATH 110..")
        print(f"Not studying for COMP 163 has left you with {study_hours - 40} study hours.")
        print(f"Not studying for MATH 110 has left you with {study_hours - 30} study hours.")
        print(f"However, you ended up gaining {social_points + 45} social points. At what cost?")
        
