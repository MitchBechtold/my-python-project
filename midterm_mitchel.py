# Problem 1
# Shopping cart dictionary

#1: 
def add_item (cart, item_name, price, quantity):
    if price <= 0 or quantity <= 0 or not isinstance(quantity, int):
        return False
    if item_name in cart:
        cart[item_name]["quantity"] += quantity
    else:
        cart[item_name] = {"price": price, "quantity": quantity}
    return True

if __name__ == "__main__":
    cart = {}
    print(add_item(cart, "Milk", 3.50, 2)) # Should print True
    print(add_item(cart, "Eggs", -1.00, 1)) # Should print False (negative price)
    print(add_item(cart, "Bread", 2.00, 3)) # Should print True
"""
# Problem 2
# Club Membership System

def add_student_to_club(clubs_dict, club_name, student_name):
    if club_name not in clubs_dict:
        clubs_dict[club_name] = set()  # create new club
    clubs_dict[club_name].add(student_name)  # add student to club
    return True


def get_students_in_multiple_clubs(clubs_dict):
    student_count = {}
    for club, members in clubs_dict.items():
        for student in members:
            student_count[student] = student_count.get(student, 0) + 1
    
    return {student for student, count in student_count.items() if count >= 2}


def find_exclusive_members(clubs_dict, club1_name, club2_name):
    if club1_name not in clubs_dict or club2_name not in clubs_dict:
        return set()  # One or both clubs missing
    
    return clubs_dict[club1_name] - clubs_dict[club2_name]

# Test your function
if __name__ == "__main__":
    clubs = {}
    
    # Add students to clubs
    add_student_to_club(clubs, "Math", "Alice")
    add_student_to_club(clubs, "Math", "Bob")
    add_student_to_club(clubs, "Science", "Alice")
    add_student_to_club(clubs, "Science", "Charlie")
    add_student_to_club(clubs, "Art", "David")
    
    print("Clubs:", clubs)
    print("In multiple clubs:", get_students_in_multiple_clubs(clubs))
    print("Math only:", find_exclusive_members(clubs, "Math", "Science"))

# Problem 3
# Score anlysis with NumPy
import numpy as np

def create_score_array(num_students, num_exams):
    return np.random.randint(60, 101, size=(num_students, num_exams))

def find_struggling_students(scores, threshold):
    averages = np.mean(scores, axis=1)
    return averages < threshold

    return stats

# Test your functions
if __name__ == "__main__":
    # Create test scores 
    scores = create_score_array(6, 4)
    print("Original scores:\n", scores)
    # Find struggling students (average < 75) 
    struggling = find_struggling_students(scores, 75)
    print(f"\nStruggling students (avg < 75): {struggling}")

# Probelm 4
# Text message cleaner
import re 
def clean_message(message):
    msg = message.lower().strip()
    msg = " ".join(msg.split())
    msg = re.sub(r"[.!?]+$", "", msg)
    return msg
if __name__ == "__main__":
    # Test cleaning
    msg1 = " Hello WORLD!!! "
    print(f"Original: '{msg1}'")
    print(f"Cleaned: '{clean_message(msg1)}'")

# Problem 5 
# Pattern Matching with regex
import re 
def valiadte_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+=\-]{8,20}$"
    return bool(re.match(pattern, password))
if __name__ == "__main__":
    
    # Test password validation
    passwords = ["Pass1234", "weakpass", "NoDigits!", "12345678", "GoodPass99"]
    for pwd in passwords:
        print(f"Password '{pwd}': {valiadte_password(pwd)}")
    print()
"""