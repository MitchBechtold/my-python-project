def format_receipt(items, prices, quantities):
    """
    Create a formatted receipt using string methods.
    """
    lines = []
    line_width = 40  # total width for separators
    
    # Header
    lines.append("=" * line_width)
    lines.append(f"{'Item':<20}{'Qty':^5}{'Price':>8}")
    lines.append("=" * line_width)
    
    total = 0
    # Body rows
    for item, price, qty in zip(items, prices, quantities):
        subtotal = price * qty
        total += subtotal
        lines.append(f"{item:<20}{qty:^5}${subtotal:>7.2f}")
    
    # Footer with total
    lines.append("=" * line_width)
    lines.append(f"{'TOTAL':<25}${total:>7.2f}")
    lines.append("=" * line_width)
    
    return "\n".join(lines)

items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.99, 2.00]
quantities = [2, 1, 3]
print(format_receipt(items, prices, quantities))

#Part 1.2 
import re

def process_user_data(raw_data):
    """
    Clean and process user input data using string methods.
    """
    cleaned = {}

    # Clean name
    name = raw_data['name'].strip().title()  # " john DOE " -> "John Doe"
    cleaned['name'] = name

    # Clean email
    email = raw_data['email'].replace(" ", "").lower()
    cleaned['email'] = email

    # Clean phone (keep digits only)
    phone = re.sub(r"\D", "", raw_data['phone'])
    cleaned['phone'] = phone

    # Clean address
    address = " ".join(raw_data['address'].split()).title()
    cleaned['address'] = address

    # Create username
    parts = name.split()
    if len(parts) >= 2:
        username = f"{parts[0].lower()}_{parts[-1].lower()}"
    else:
        username = parts[0].lower()
    cleaned['username'] = username

    # Validation rules
    validation = {
        "email_valid": "@" in email and "." in email,
        "phone_valid": phone.isdigit() and len(phone) >= 10,
    }
    cleaned['validation'] = validation

    return cleaned
#example of use 
data = {
    'name': ' john DOE ',
    'email': ' JOHN.DOE @EXAMPLE.COM ',
    'phone': '(555) 123-4567',
    'address': '123 main street, apt 5'
}
result = process_user_data(data)

print(result['name'])      # John Doe
print(result['email'])     # john.doe@example.com
print(result['phone'])     # 5551234567
print(result['address'])   # 123 Main Street, Apt 5
print(result['username'])  # john_doe
print(result['validation'])

#Part 1.3

import re

def analyze_text(text):
    """
    Perform comprehensive text analysis using string methods.
    """
    lines = text.splitlines()

    words = re.findall(r"\b\w+\b", text)  # extracts words
    words_lower = [w.lower() for w in words]

    total_chars = len(text)

    total_words = len(words)

    total_lines = len(lines)

    avg_word_length = round(sum(len(w) for w in words) / total_words, 2) if total_words > 0 else 0

    most_common_word = None
    if words_lower:
        freq = {}
        for w in words_lower:
            freq[w] = freq.get(w, 0) + 1
        most_common_word = max(freq, key=freq.get)

    longest_line = max(lines, key=len) if lines else ""

    words_per_line = [len(re.findall(r"\b\w+\b", line)) for line in lines]

    sentences = re.findall(r"[^.!?]+[.!?]", text.strip())

    capitalized_sentences = sum(1 for s in sentences if s.strip()[0].isupper())

    questions = sum(1 for s in sentences if s.strip().endswith("?"))

    exclamations = sum(1 for s in sentences if s.strip().endswith("!"))

    return {
        'total_chars': total_chars,
        'total_words': total_words,
        'total_lines': total_lines,
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'longest_line': longest_line,
        'words_per_line': words_per_line,
        'capitalized_sentences': capitalized_sentences,
        'questions': questions,
        'exclamations': exclamations
    }

#example of use

text = """Hello world! How are you?
This is a test. Another line here!"""
result = analyze_text(text)

print("Total chars:", result['total_chars'])
print("Total words:", result['total_words'])
print("Total lines:", result['total_lines'])
print("Average word length:", result['avg_word_length'])
print("Most common word:", result['most_common_word'])
print("Longest line:", result['longest_line'])
print("Words per line:", result['words_per_line'])
print("Capitalized sentences:", result['capitalized_sentences'])
print("Questions:", result['questions'])
print("Exclamations:", result['exclamations'])

#Part 2.1
import re

def find_patterns(text, pattern):
    """
    Find all matches of a regex pattern in text.
    
    Args:
        text (str): The text to search
        pattern (str): Regex pattern (raw string required)
    
    Returns:
        list: All matches
    """
    matches = re.findall(pattern, text)
    return matches

#Example of use
print(find_patterns("abc123def456", r"\d+"))

#Part 2.2 
def validate_password(password):
    """
    Validate password strength.
    
    Rules:
    - At least 8 chars
    - Contains uppercase
    - Contains lowercase
    - Contains digit
    - Contains special character
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[^A-Za-z0-9]", password):  # special char
        return False
    return True

#Example of use
print(validate_password("Password1!"))  # True
print(validate_password("weakpass"))    # False

#Part 2.3
def extract_emails(text):
    """
    Extract all email addresses from text.
    """
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.findall(pattern, text)

#Example of use
print(extract_emails("Contact: test@example.com, admin@site.org"))


#Part 2.4

def split_sentences(text):
    """
    Split text into sentences based on ., !, or ?
    """
    pattern = r"[^.!?]+[.!?]"
    return [s.strip() for s in re.findall(pattern, text)]

#Example of use
print(split_sentences("Hello world! How are you? I'm fine."))


#Part 2.5

def mask_credit_card(card_number):
    """
    Mask all digits except last 4 in a credit card number.
    """
    return re.sub(r"\d(?=\d{4})", "*", card_number)

#Example of use
print(mask_credit_card("1234567812345678"))
