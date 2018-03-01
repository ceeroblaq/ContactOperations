import unittest
from app.contacts import Contact_Operations
 
class Contact_operations_tests(unittest.TestCase):

    def test_add_phone_number(self):
        contact = Contacts()
        result = contact.add_contacts("user_id", "contact_name","contact_number")
        params = len(result)
        self.assertEqual(3, params)


    def test_update_phone_number(self):
        contact = Contacts()
        result = contact.remove_contacts("user_id", "contact_name","contact_number")
        params = len(result)
        self.assertEqual(3, params)

