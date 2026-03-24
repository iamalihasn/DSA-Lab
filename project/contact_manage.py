class ContactBook:
  contact_data = []

  # constructor or initializer-called when we create object of class

  def __init__(self,name,contact_number):
    self.name = name
    self.number = contact_number
    ContactBook.contact_data.append(self)
  

  def show_contact(self):
    return f"Name : {self.name} and Contact : {self.number}"
  
  @classmethod
  def show_all_contact(cls):
    if not cls.contact_data:
      return "Empty Contact list"
    else:
      for contact in cls.contact_data:
        print(contact.show_contact())

  @classmethod
  def search_contact(cls,search_name):
    for contact in cls.contact_data:
      if contact.name.lower() == search_name.lower():
        return contact.number

    return f"Not contact Found this name {search_name}"
  
  @classmethod
  def delete_contact(cls,name):
    for contact in cls.contact_data:
      if contact.name.lower() == name.lower():
        cls.contact_data.remove(contact)
        return "Delete contact successfully!"
    
    return f"No contact of this name {name}"
  
  @staticmethod
  def validate_contact_number(contact_number):
    if len(str(contact_number)) == 10 and str(contact_number).isdigit():
      return True
    else:
      return False


no_of_contact = int(input("How many contact you want to add : "))
for i in range(no_of_contact):
  name = input("Enter contact name : ")
  contact_number = int(input("Enter contact number : "))
  if ContactBook.validate_contact_number(contact_number):
    ContactBook(name,contact_number)
  else:
    print("Invalid contact number! Please enter a valid 10-digit number.")

print("======================================================")
print("All Contacts:")
ContactBook.show_all_contact()