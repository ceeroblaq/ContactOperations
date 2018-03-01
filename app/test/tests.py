import unittest
from app.contacts import Contact_Operations
 
class Contact_operations_tests(unittest.TestCase):

#user can add a new contact
    def test_add_phone_number(self):
        contact = Contact_Operations()
        result = contact.add_contact( "user_id", "contact_name", 0755326545 )
        params = len(result)
        self.assertEqual(3, params)

#user can update a new contact
    def test_update_phone_number(self):
        contact = Contact_Operations()
        result = contact.update_contact( "user_id", "contact_name", 0755326545 )
        params = len(result)
        self.assertEqual(3, params)

#user can delete a new contact
    def test_delete_phone_number(self):
        contact = Contact_Operations()
        result = contact.remove_contact( "user_id", "contact_name" )
        self.assertEqual("delete", result)

#user can view their contacts
    def test_view_contacts(self):
        contact = Contact_Operations()
        result = contact.view_contacts( "user_id" )
        self.assertEqual("present", result)

#user is in control of the contact in question
    def test_get_phone_number(self):
        contact = Contact_Operations()
        result = contact.get_contact( "user_id", 0755326545 )
        self.assertEqual("delete", result)

#user has a valid id able to access contacts
    def test_get_user(self):
        contact = Contact_Operations()
        result = contact.fetch_all_contacts( "user_id" )
        self.assertEqual("dict", type(result))

