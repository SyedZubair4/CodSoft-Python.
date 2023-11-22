# Displaying guide for contact book
print('''CONTACT BOOK
Store\'s name, email, phone number, address
Please select the option from below
1) Add a new contact
2) Delete an existing contact
3) Update the contact(pre-existing)
4) Search for contact
5) View contacts
6) Quit''')

class Contact_book:

    def __init__(self, name, email, phone_number, address):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.address=address

    @classmethod
    def add_contact(cls):
        global contacts
        name=input('Enter the name:')
        email=input('Enter email:')
        phone_number=input('Enter phone number:')
        address=input('Enter address:')
        detail=Contact_book(name, email, phone_number, address)
        contacts.append(detail)
        print('Added successfully.')
        return

    @classmethod
    def view_contact_book(cls):
        for contact in contacts:
            print(f'{contact.name} - {contact.phone_number} - {contact.email} - {contact.address}')
        return

    @classmethod
    def delete_contact(cls, contacts, word):
        found = 0
        for contact in contacts:
            if contact.name.lower()==word.lower() or contact.phone_number==word:
                contacts.remove(contact)
                print(f'contact {contact.name} deleted successfully')
                found = 1

        if found == 0:
            print(f'contact {word} Not Found')
        return

    @classmethod
    def update_contact(cls, update, contacts):
        found = 0
        for contact in contacts:
            if contact.name.lower()==update.lower() or contact.phone_number==update:
                found=1
                uname=input('Enter name:')
                uemail=input('Enter email:')
                uphone_number=input('Enter phone number:')
                uaddress=input('Enter address:')

                contact.name=uname
                contact.email=uemail
                contact.phone_number=uphone_number
                contact.address=uaddress

                print(f'contact {contact.name} updated successfully with new details as, {contact.phone_number}, {contact.email}, {contact.address}')

        if found == 0:
            print(f"contact with name/phone_number: '{update}' not found")

        return

    @classmethod
    def search_in_contact_book(cls, search, contacts):
        found=0
        for contact in contacts:
            if contact.name.lower()==search.lower() or contact.phone_number==search:
                print(f'contact with name {contact.name} and phone number {contact.phone_number} was found with details, email {contact.email} and address {contact.address}')
                found=1

        if found == 1:
             print(f'Contact with name/phone_number {search} not found')

        return

# main program starts from here
contacts=[]
temp=0
while True:
    choice = input('\n\nEnter your choice:')

    # for adding contacts
    if choice=='1':
        Contact_book.add_contact()

    # for deleting contact
    elif choice=='2':
        while True:
            if temp==1:
                break
            cho = input('Do you want to display your Contact Book?(y/n):')

            if cho == 'y':
                Contact_book.view_contact_book()
                temp=1
            elif cho == 'n':
                temp=1
                break
            else:
                continue
        word=input('Enter the contact you want to delete:')
        Contact_book.delete_contact(contacts, word)

    #for updating contacts
    elif choice=='3':
        while True:
            if temp==1:
                break
            cho = input('Do you want to display your Contact Book?(y/n):')
            if cho == 'y':
                temp=1
                Contact_book.view_contact_book()
            elif cho == 'n':
                temp=1
                break
            else:
                continue

        update=input('Enter the name or phone number of the contact you want to update:')
        Contact_book.update_contact(update, contacts)

    #for searching a contact
    elif choice=='4':
        search=input('Enter the name or phone number you want to search:')
        Contact_book.search_in_contact_book(search, contacts)

    #for viewing contacts
    elif choice=='5':
        Contact_book.view_contact_book()

    #for quiting
    elif choice=='6':
        print('Thank you!!')
        break

    else:
        print('Invalid Input')
        continue
