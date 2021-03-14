
class User:
    """A class to store a user's data.

    ---Attributes---
    vax - has the user been vaccinated? (Boolean)
    first_name - user's first name (String)
    last_name - user's last name (String)
    birthday - user's date of birth (int: YYYYMMDD)
    # TODO
    """

    def __init__(self):
        self._vax = None
        self._first_name = ""
        self._last_name = ""
        self._birthday = 0
        #TODO

    def get_user_string(self):
        """Returns a succinct representation of the users attributes."""
        birthday_string = str(self._birthday)
        birthday_string = birthday_string[0:4] + "/" + birthday_string[4:6] + "/" + birthday_string[6:8]
        
        
        vax_string = "Not Vaccinated"
        if self._vax is True:
            vax_string = "Vaccinated"
        
        user_string = ""
        user_string = ("Name: {} {}Date of Birth: {}Vaccination Status: {}".format(self._first_name, self._last_name, birthday_string, vax_string))

        print(user_string)
        
        return user_string #TODO
    
    def create_user(self):
        # asks vaccination status (must be 'Yes' or 'No')
        vax_input = ""
        while vax_input not in ['Yes', 'yes', 'No', 'no']:
            vax_input = input("Have you been vaccinated? (Yes or No): ")
        
        # converts to Boolean
        if vax_input == "Yes":
            self._vax = True
        else:
            self._vax = False
            
        # gets name
        self._first_name = input("What is your first name?: ")
        self._last_name = input("What is your last name?: ")
        
        # gets birthday (must be 8 digits)
        while self._birthday < 10000000 or self._birthday > 99999999:
            self._birthday = int(input("What is your date of birth? (YYYYMMDD): "))
        
        
        '''if vax == True:
            print("{} {} has been vaccinated.".format(first_name, last_name))
        else:
            print("{} {} has not been vaccinated.".format(first_name, last_name))'''
        
        return


        

