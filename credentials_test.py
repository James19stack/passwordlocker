import unittest # Importing the unittest module
from credentials import Credentials  # Importing the credentials class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("James","Mirara","Jefferson","Jefferson_22","mirarajames29@gmail.com")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        ''' 

        self.assertEqual(self.new_credentials.first_name,"James")
        self.assertEqual(self.new_credentials.last_name,"Mirara")
        self.assertEqual(self.new_credentials.user_name,"Jefferson")
        self.assertEqual(self.new_credentials.password,"Jefferson_22")
        self.assertEqual(self.new_credentials.email,"mirarajames29@gmail.com")


    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the credentials object is saved into
        the contact list
        '''

        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1) 

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Charles","Mirara","Charleston","Charles_22","charlesmirara@gmail.com") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

# other test cases here

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple contact
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Charles","Mirara","Charleston","Charles_22","charlesmirara@gmail.com") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Charles","Mirara","Charleston","Charles_22","charlesmirara@gmail.com") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a contact object

            self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_email(self):
            '''
            test to check if we can find a credentials by email and display information
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Charles","Mirara","Charleston","Charles_22","charles.com") # new credentials 

            test_credentials.save_credentials()

            found_credentials = Credentials.find_by_email("charles.com")

            self.assertEqual(found_credentials.first_name, test_credentials.first_name)

    def test_credentials_exists(self):
            '''
            test to check if we can return a Boolean if we cannot find the credentials
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Charles","Mirara","Charleston","Charles_22","charles.com") # new credentials 
            test_credentials.save_credentials()

            credentials_exists = Credentials.credentials_exist("charles.com")

            self.assertTrue(credentials_exists) 
    def test_display_all_credentials(self):
            '''
            method that returns a list of all credentials saved
            '''

            self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()           
