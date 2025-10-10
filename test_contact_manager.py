# test_contacts.py
from dictionary import * 

def run_tests():
    contacts_db = {}

    # Test Add Contact
    print("\n--- Testing Add Contact ---")
    contact1 = {
        "first_name": "Alice",
        "last_name": "Smith",
        "phone": "123-456-7890",
        "email": "alice@example.com",
        "address": "New York, NY",
        "category": "family"
    }
    cid1 = add_contact(contacts_db, contact1)
    print("Added contact:", cid1)

    # Test Search
    print("\n--- Testing Search by Name ---")
    results = search_contacts_by_name(contacts_db, "Alice")
    print("Search Results:", results)

    # Test Update
    print("\n--- Testing Update Contact ---")
    update_contact(contacts_db, cid1, {"phone": "999-999-9999"})
    display_contact(contacts_db, cid1)

    # Test Statistics
    print("\n--- Testing Statistics ---")
    stats = generate_contact_statistics(contacts_db)
    print(stats)

    # Test Export
    print("\n--- Testing Export by Category ---")
    export = export_contacts_by_category(contacts_db, "family")
    print(export)

if __name__ == "__main__":
    run_tests()