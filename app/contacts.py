class Contact_Operations(object):
 
    def __int__(self):
        self.contact_details = {}

    def add_contacts(self, user_id, contact_name, contact_number):
        self.contact_details["user"] = user_id
        self.contact_details["contact"] = contact_name
        self.contact_details["number"] = contact_number

        return contact_details;

    def update_contacts(self, user_id, contact_name, contact_number):
        self.contact_details["user"] = user_id
        self.contact_details["contact"] = contact_name
        self.contact_details["number"] = contact_number
        
        return contact_details;
