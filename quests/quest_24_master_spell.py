def ask_for_age():
    age = int(input("Please enter your age: "))
    return age

def can_they_vote(age):
    print()
    if age >= 18:
        print(f"At {age} years old, you ARE eligible to vote. Go make your voice heard!")
    else:
        years_left = 18 - age
        print(f"At {age} years old, you are not yet eligible to vote.")
        print(f"You'll be eligible in {years_left} year(s). Stay curious until then!")
        print ()
user_age = ask_for_age()
can_they_vote(user_age)        
