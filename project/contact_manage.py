class ContactBook:
  contact_data = []

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
      if contact.name == search_name:
        return contact.number

    return f"Not contact Found this name {search_name}"
  
  @classmethod
  def delete_contact(cls,name):
    for contact in cls.contact_data:
      if contact.name == name:
        cls.contact_data.remove(contact)
        return "Delete contact successfully!"
    
    return f"No contact of this name {name}"

c= ContactBook("Ram",8294322434)
c1 = ContactBook("Ali",8002938316)
c1 = ContactBook("Salma",8651530267)
#ContactBook.show_all_contact()

print(ContactBook.delete_contact("Ram"))
print(ContactBook.show_all_contact())
print(ContactBook.search_contact("ram"))