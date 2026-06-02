contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No Contacts Found!")
        else:
            print("\n--- Contact List ---")
            for contact in contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print("-" * 30)

    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False
        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Contact Name to Update: ")

        found = False
        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("New Phone: ")
                contact["email"] = input("New Email: ")
                contact["address"] = input("New Address: ")
                print("Contact Updated Successfully!")
                found = True

        if not found:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter Contact Name to Delete: ")

        found = False
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Try Again.")