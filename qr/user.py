
class User:
    """A class to store a user's data.

    ---Attributes---
    vax - has the user been vaccinated? (Boolean)
    first_name - user's first name (String)
    last_name - user's last name (String)
    birthday - user's date of birth (int: YYYYMMDD)
    # TODO
    """

    def __init__(self, first_name, last_name, birthday):
        self._vax = None
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = birthday
        #TODO

    def get_user_string(self) -> str:
        """Returns a succinct representation of the users attributes."""
        return None #TODO

