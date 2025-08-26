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
