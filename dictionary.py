import datetime

def create_contact():
    """
    Creates a contact dictionary with required and optional fields.
    Includes input validation and auto-generated timestamps.
    """

    # Required fields
    while True:
        first_name = input("Enter first name (required): ").strip()
        if first_name:
            break
        print("First name cannot be empty.")

    while True:
        last_name = input("Enter last name (required): ").strip()
        if last_name:
            break
        print("Last name cannot be empty.")

    while True:
        phone = input("Enter phone number (required): ").strip()
        if phone:
            break
        print("Phone number cannot be empty.")

    # Optional fields
    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()
    notes = input("Enter notes (optional): ").strip()

    # Use current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create contact dictionary
    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email if email else "",
        "address": address if address else "",
        "notes": notes if notes else "",
        "created_date": timestamp,
        "last_modified": timestamp
    }

    return contact


# Example usage
if __name__ == "__main__":
    new_contact = create_contact()
    print("\nContact Created:")
    for key, value in new_contact.items():
        print(f"{key}: {value}")
import datetime

def add_contact(contacts_db, contact_data):
    # Check required fields
    if not contact_data.get("first_name"):
        print("First name is required.")
        return None
    if not contact_data.get("last_name"):
        print("Last name is required.")
        return None
    if not contact_data.get("phone"):
        print("Phone number is required.")
        return None

    # Generate contact ID (just use the length of dictionary)
    contact_id = "contact_" + str(len(contacts_db) + 1).zfill(3)

    # Add timestamps
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "created_date" not in contact_data:
        contact_data["created_date"] = now
    contact_data["last_modified"] = now

    # Save to database
    contacts_db[contact_id] = contact_data
    return contact_id


def display_contact(contacts_db, contact_id):
    if contact_id not in contacts_db:
        print("Contact not found.")
        return False

    contact = contacts_db[contact_id]
    print("\nContact ID:", contact_id)
    for key in contact:
        print(key, ":", contact[key])
    return True


def list_all_contacts(contacts_db):
    if not contacts_db:
        print("No contacts yet.")
        return

    print("\nAll Contacts:")
    for cid, data in contacts_db.items():
        print(cid, "->", data["first_name"], data["last_name"], "|", data["phone"])
def search_contacts_by_name(contacts_db, search_term):
    """
    Search contacts by first or last name (case-insensitive partial match).
    """
    results = {}
    search_term = search_term.lower()  # make it case-insensitive

    for contact_id, data in contacts_db.items():
        if (search_term in data["first_name"].lower()) or (search_term in data["last_name"].lower()):
            results[contact_id] = data

    return results


def search_contacts_by_category(contacts_db, category):
    """
    Find all contacts in a specific category.
    (Assumes contacts have a 'category' field, e.g., 'family', 'work', 'friends')
    """
    results = {}

    for contact_id, data in contacts_db.items():
        if "category" in data and data["category"].lower() == category.lower():
            results[contact_id] = data

    return results


def find_contact_by_phone(contacts_db, phone_number):
    """
    Find contact by phone number (exact match).
    """
    for contact_id, data in contacts_db.items():
        if data.get("phone") == phone_number:
            return contact_id, data

    return None, None
import datetime

def update_contact(contacts_db, contact_id, field_updates):
    """
    Update specific fields of an existing contact.
    Automatically update last_modified timestamp.
    """
    if contact_id not in contacts_db:
        print("Contact not found.")
        return False

    contact = contacts_db[contact_id]

    # Update the fields
    for field, value in field_updates.items():
        if field in contact:
            contact[field] = value
        else:
            print(f"Field '{field}' does not exist, skipping.")

    # Update last_modified
    contact["last_modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Contact {contact_id} updated.")
    return True


def delete_contact(contacts_db, contact_id):
    """
    Remove a contact from the database with confirmation.
    """
    if contact_id not in contacts_db:
        print("Contact not found.")
        return False

    confirm = input(f"Are you sure you want to delete {contact_id}? (y/n): ").lower()
    if confirm == "y":
        del contacts_db[contact_id]
        print(f"Contact {contact_id} deleted.")
        return True
    else:
        print("Deletion cancelled.")
        return False


def merge_contacts(contacts_db, contact_id1, contact_id2):
    """
    Merge two contacts, keeping the most recent information.
    Prompt user for conflicts in overlapping fields.
    """
    if contact_id1 not in contacts_db or contact_id2 not in contacts_db:
        print("One or both contacts not found.")
        return None

    contact1 = contacts_db[contact_id1]
    contact2 = contacts_db[contact_id2]

    # Decide which contact to keep (use the latest modified one)
    if contact1["last_modified"] >= contact2["last_modified"]:
        merged_contact = contact1.copy()
        other_contact = contact2
        keep_id = contact_id1
    else:
        merged_contact = contact2.copy()
        other_contact = contact1
        keep_id = contact_id2

    # Resolve conflicts field by field
    for field in other_contact:
        if field in merged_contact:
            if merged_contact[field] != other_contact[field]:
                choice = input(f"Conflict in '{field}' - "
                               f"{merged_contact[field]} vs {other_contact[field]}. "
                               f"Which one to keep? (1/2): ")
                if choice == "2":
                    merged_contact[field] = other_contact[field]
        else:
            merged_contact[field] = other_contact[field]

    # Update timestamp
    merged_contact["last_modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save merged contact and delete the other one
    contacts_db[keep_id] = merged_contact
    delete_id = contact_id1 if keep_id == contact_id2 else contact_id2
    del contacts_db[delete_id]

    print(f"Contacts {contact_id1} and {contact_id2} merged into {keep_id}")
    return keep_id
def generate_contact_statistics(contacts_db):
    """
    Generate comprehensive statistics about the contact database.
    """
    stats = {
        "total_contacts": len(contacts_db),
        "contacts_by_category": {},
        "contacts_by_state": {},
        "average_contacts_per_category": 0.0,
        "most_common_area_code": None,
        "contacts_without_email": 0
    }

    area_codes = {}

    for contact_id, data in contacts_db.items():
        # Count by category
        category = data.get("category", "Uncategorized")
        stats["contacts_by_category"][category] = stats["contacts_by_category"].get(category, 0) + 1

        # Count by state (from address, assuming "City, State" format)
        address = data.get("address", "")
        if "," in address:
            state = address.split(",")[-1].strip()
            stats["contacts_by_state"][state] = stats["contacts_by_state"].get(state, 0) + 1

        # Count missing emails
        if not data.get("email"):
            stats["contacts_without_email"] += 1

        # Count area codes (first 3 digits of phone)
        phone = data.get("phone", "")
        if "-" in phone:
            area = phone.split("-")[0]
            area_codes[area] = area_codes.get(area, 0) + 1

    # Average contacts per category
    if stats["contacts_by_category"]:
        stats["average_contacts_per_category"] = round(
            stats["total_contacts"] / len(stats["contacts_by_category"]), 2
        )

    # Most common area code
    if area_codes:
        stats["most_common_area_code"] = max(area_codes, key=area_codes.get)

    return stats


def find_duplicate_contacts(contacts_db):
    """
    Identify potential duplicate contacts.
    """
    duplicates = {
        "phone_duplicates": [],
        "email_duplicates": [],
        "name_duplicates": []
    }

    phone_map = {}
    email_map = {}
    name_map = {}

    for cid, data in contacts_db.items():
        # Phone
        phone = data.get("phone")
        if phone:
            if phone in phone_map:
                duplicates["phone_duplicates"].append([phone_map[phone], cid])
            else:
                phone_map[phone] = cid

        # Email
        email = data.get("email")
        if email:
            if email in email_map:
                duplicates["email_duplicates"].append([email_map[email], cid])
            else:
                email_map[email] = cid

        # Name
        fullname = data.get("first_name", "") + " " + data.get("last_name", "")
        if fullname.strip():
            if fullname in name_map:
                duplicates["name_duplicates"].append([name_map[fullname], cid])
            else:
                name_map[fullname] = cid

    return duplicates


def export_contacts_by_category(contacts_db, category):
    """
    Export contacts from a specific category as a formatted string.
    """
    output = f"Contacts in category '{category}':\n"
    output += "-" * 40 + "\n"

    found = False
    for cid, data in contacts_db.items():
        if data.get("category", "").lower() == category.lower():
            found = True
            output += f"ID: {cid}\n"
            for key, value in data.items():
                output += f"{key.capitalize()}: {value}\n"
            output += "-" * 40 + "\n"

    if not found:
        output += "No contacts found in this category.\n"

    return output