class Contact_Operations(object):

    def __init__(self):
        self.contact_details = {}



    #method to add a contact

    def add_contact(self, user_id, contact_name, contact_number):
        self.contact_details["user"] = user_id
        self.contact_details["contact"] = contact_name
        self.contact_details["number"] = contact_number

        return self.contact_details



    #method to update a contact

    def update_contact(self, user_id, contact_name, contact_number):
        self.contact_details["user"] = user_id
        self.contact_details["contact"] = contact_name
        self.contact_details["number"] = contact_number
        
        return self.contact_details



    #method to delete a contact

    def remove_contact( self, user_id, contact_number ):

        #get_contact is a method to retrive contact from a database

        victim = self.get_contact( user_id, contact_number )
        return victim



    #method to view contacts

    def view_contacts(self, user_id):
         
        #fetch_all_contacts is a method to retrive the user

        phone_book = self.fetch_all_contacts( user_id )
        return phone_book 



    #method to retrieve a specific contact 

    def get_contact( self, user_id, contact_number ):
        if( user_id and contact_number ):
            message = "delete"
            return message
        message = "Error"
        return false


    #method to retrieve a specific contact 

    def fetch_all_contacts( user_id ):
        if( user_id ):
            result = {}
        else:
            result = ""
        return result
        
