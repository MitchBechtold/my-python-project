#Mitchel Bechtold
#10/2/2025
import re 
import time

"""
Problem 1: Grouping and capturing
"""

dates_text = """
Important dates:
- Project due: 2024-03-15
- Meeting on: 12/25/2024
- Holiday: July 4, 2025
"""
pattern_iso = r"(\d{4})-(\d{2})-(\d{2})"
iso_dates = re.findall(pattern_iso, dates_text)
# re.findall returns list of tuples, so join them back
iso_dates = ["-".join(date) for date in iso_dates]


emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
pattern_email = r"(?P<username>[a-zA-Z0-9._]+)@(?P<domain>[a-zA-Z0-9._]+\.[a-zA-Z]{2,})"
matches = re.finditer(pattern_email, emails_text)
email_parts = [{"username": m.group("username"), "domain": m.group("domain")} for m in matches]

phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
pattern_phone = r"(?:\((\d{3})\)|(\d{3}))[- ](\d{3}-\d{4})"
matches = re.findall(pattern_phone, phones_text)

phone_numbers = [(m[0] if m[0] else m[1], m[2]) for m in matches]

repeated_text = "The the quick brown fox jumped over the the lazy dog"
pattern_repeated = r"\b(\w+)\s+\1\b"
repeated_words = re.findall(pattern_repeated, repeated_text, flags=re.IGNORECASE)


print("iso_dates:", iso_dates)
print("email_parts:", email_parts)
print("phone_numbers:", phone_numbers)
print("repeated_words:", repeated_words)

"""
Problem 2: Alteration performance
"""
files_text = """
Documents: report.pdf, notes.txt, presentation.pptx
Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
Code: script.py, program.java, style.css
"""
pattern_images = r"\b\w+\.(jpg|jpeg|png|gif)\b"
image_files = re.findall(pattern_images, files_text)

pattern_images = r"\b\w+\.(?:jpg|jpeg|png|gif)\b"
image_files = re.findall(pattern_images, files_text)


mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
# ISO (YYYY-MM-DD) | US (MM/DD/YYYY) | Text (Month DD, YYYY)
pattern_dates = r"\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|[A-Za-z]+ \d{1,2}, \d{4}"
all_dates = re.findall(pattern_dates, mixed_dates)


prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"

pattern_prices = r"(?:\$|USD|dollars|€|£)\s?\d+(?:\.\d{2})?"
prices = re.findall(pattern_prices, prices_text)


code_text = """
We use Python for data science, Java for enterprise apps,
JavaScript or JS for web development, and C++ or CPP for systems.
"""

pattern_langs = r"\b(?:Python|JavaScript|JS|Java|C\+\+|CPP)\b"
languages = re.findall(pattern_langs, code_text)


print("image_files:", image_files)
print("all_dates:", all_dates)
print("prices:", prices)
print("languages:", languages)

"""
Problem 3: Using re.findall and re.finditer
"""

log_text = """
[2024-03-15 10:30:45] INFO: Server started on port 8080
[2024-03-15 10:31:02] ERROR: Connection failed to database
[2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
[2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
[2024-03-15 10:32:30] ERROR: File not found: config.yml
"""

pattern_timestamp = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
timestamps = re.findall(pattern_timestamp, log_text)

pattern_log = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (\w+): (.*)"
log_entries = re.findall(pattern_log, log_text)  # returns list of (level, message)

pattern_ip = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
ip_addresses = []
for match in re.finditer(pattern_ip, log_text):
    ip_addresses.append({
        "ip": match.group(),
        "start": match.start(),
        "end": match.end()
    })

def highlight_errors(text):
    return re.sub(r"(ERROR)", r"**\1**", text)

highlighted_log = highlight_errors(log_text)

print("timestamps:", timestamps)
print("log_entries:", log_entries)
print("ip_addresses:", ip_addresses)
print("highlighted_log:\n", highlighted_log)

"""
Problem 4: Using re.sub for text transformation
"""

messy_phones = """
Contact list:
- John: 555.123.4567
- Jane: (555) 234-5678
- Bob: 555 345 6789
- Alice: 5554567890
"""

def standardize_phones(text):
    """
    Convert all phone number formats to (XXX) XXX-XXXX.
    """
    pattern = r"\D?(\d{3})\D?\s?(\d{3})\D?\s?(\d{4})"
    replacement = r"(\1) \2-\3"
    return re.sub(pattern, replacement, text)

cleaned_phones = standardize_phones(messy_phones)

sensitive_text = """
Customer: John Doe
SSN: 123-45-6789
Credit Card: 4532-1234-5678-9012
Email: john.doe@email.com
Phone: (555) 123-4567
"""

def redact_sensitive(text):
    """
    Replace SSN with XXX-XX-XXXX and
    Credit Card with XXXX-XXXX-XXXX-XXXX.
    """
    text = re.sub(r"\d{3}-\d{2}-\d{4}", "XXX-XX-XXXX", text)  # SSN
    text = re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "XXXX-XXXX-XXXX-XXXX", text)  # CC
    return text

redacted_text = redact_sensitive(sensitive_text)

markdown_text = """
Check out [Google](https://google.com) for search.
Visit [GitHub](https://github.com) for code.
Read documentation at [Python Docs](https://docs.python.org).
"""

def markdown_to_html(text):
    """
    Convert markdown links [text](url) to HTML anchor tags.
    """
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    replacement = r'<a href="\2">\1</a>'
    return re.sub(pattern, replacement, text)

html_text = markdown_to_html(markdown_text)

template = """
Dear {name},
Your order #{order_id} for {product} has been shipped.
Tracking number: {tracking}
"""

values = {
    'name': 'John Smith',
    'order_id': '12345',
    'product': 'Python Book',
    'tracking': 'TRK789XYZ'
}

def fill_template(template, values):
    """
    Replace all {key} placeholders with values from dictionary.
    """
    def replacer(match):
        key = match.group(1)
        return values.get(key, f"{{{key}}}")  
    return re.sub(r"\{(\w+)\}", replacer, template)

filled_template = fill_template(template, values)

print("cleaned_phones:\n", cleaned_phones)
print("redacted_text:\n", redacted_text)
print("html_text:\n", html_text)
print("filled_template:\n", filled_template)

"""
Problem 5: Pattern Compilation and optimization
"""
class PatternLibrary:
    """
    Library of compiled regex patterns for common use cases.
    """

    EMAIL = re.compile(
        r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$",
        re.IGNORECASE
    )

    URL = re.compile(
        r"^(https?://)?(www\.)?[a-z0-9.-]+\.[a-z]{2,}(/.*)?$",
        re.IGNORECASE
    )

    ZIP_CODE = re.compile(
        r"^\d{5}(-\d{4})?$"
    )

    PASSWORD = re.compile(r"""
        ^                   
        (?=.*[A-Z])         
        (?=.*[a-z])         
        (?=.*\d)            
        (?=.*[!@#$%^&*])    
        .{8,}               
        $                   
    """, re.VERBOSE)

    CREDIT_CARD = re.compile(
        r"^(?:\d{4}[- ]?){3}\d{4}$"
    )


test_data = {
    'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
    'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
    'zips': ['12345', '12345-6789', '1234', '123456'],
    'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
    'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
}

validation_results = {
    'emails': [bool(PatternLibrary.EMAIL.match(e)) for e in test_data['emails']],
    'urls': [bool(PatternLibrary.URL.match(u)) for u in test_data['urls']],
    'zips': [bool(PatternLibrary.ZIP_CODE.match(z)) for z in test_data['zips']],
    'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
    'cards': [bool(PatternLibrary.CREDIT_CARD.match(c)) for c in test_data['cards']]
}

# Print results
print(validation_results)

"""
Problem 6: Benchmarking regex performance
"""
log_data = """
192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5234
192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401 234
192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200 1234
192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200 15234
192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
"""

log_pattern = re.compile(r"""
    (?P<ip>\d+\.\d+\.\d+\.\d+)      
    \s+-\s+-\s+
    \[(?P<timestamp>[^\]]+)\]        
    \s+"(?P<method>[A-Z]+)\s        
    (?P<path>[^\s]+)                 
    \sHTTP/\d\.\d"                  
    \s(?P<status>\d{3})             
    \s(?P<size>\d+)                  
""", re.VERBOSE)

parsed_logs = []
for match in log_pattern.finditer(log_data):
    parsed_logs.append({
        'ip': match.group('ip'),
        'timestamp': match.group('timestamp'),
        'method': match.group('method'),
        'path': match.group('path'),
        'status': int(match.group('status')),
        'size': int(match.group('size'))
    })

analysis = {
    'total_requests': len(parsed_logs),
    'unique_ips': sorted(set(log['ip'] for log in parsed_logs)),
    'error_count': sum(1 for log in parsed_logs if 400 <= log['status'] < 600),
    'total_bytes': sum(log['size'] for log in parsed_logs),
    'most_requested_path': Counter(log['path'] for log in parsed_logs).most_common(1)[0][0],
    'methods_used': sorted(set(log['method'] for log in parsed_logs))
}

results = {
    'parsed_logs': parsed_logs,
    'analysis': analysis
}

print(results)








