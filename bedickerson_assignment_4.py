student_name = "Bryant Dickerson"
current_gpa = 4.0
study_hours = 6
social_points = 35
stress_level = 70
# ADDED THE CODE BELOW AFTER FIRST COMMIT**
diff_choice = input()
easy_mode = ("Easy Difficulty: (12 Credits)")
medium_mode = ("Medium Difficulty: (15 Credits)")
hard_mode = ("Hard Difficulty: 18 Credits")

# social_points was evaluated on a scale of 0-50.
# stress_level was evaluated on a scale of 0-100.
print(f"Student Name: {student_name}")
print(f"Current GPA: {current_gpa:.2f}")
print(f"Study hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

print("")
print("Enter your choice:")
if diff_choice == easy_mode:
    print(f"Mode chosen: {easy_mode}")
elif diff_choice == medium_mode:
    print(f"Mode chosen: {easy_mode}")
elif diff_choice == hard_mode:
    print(f"Mode chosen: {hard_mode}")
else:
    print("Invalid Choice: Choose again.")
