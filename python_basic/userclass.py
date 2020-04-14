class User:
    """Simulate user info including first and last names."""
    
    def __init__(self, first_name, last_name, age, gender):
        """Initiate user instance with first/last name, age, and gender"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Print summary of user information based on input."""
        print("Here are the information according to your input:")
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender.title()}")

    def greet_user(self):
        """Print greetings for user."""
        print(f"Hello, {self.first_name.title()}, glad you are here with us!")
        
    def increment_login_attempts(self):
        """Increment login_attempts by 1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0
        
class Privileges:
    """Stores list of current admin privileges as attribute."""
    
    def __init__(self, current_privileges = []):
        self.current_privileges = current_privileges
        
    def show_privileges(self):
        """Print summary of admin privileges."""
        print(f"Hello, SysAdmin. Here are your current admin privileges: ")
        for privilege in self.current_privileges:
            print(f"- {privilege.capitalize()}")

class Admin(User):
    """A subclass of User that is an admin"""
    
    def __init__(self, first_name, last_name, age, gender, privileges):
        """Initiate admin with the superclass User"""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges(privileges)
        


matt = User('matt', 'chan', '34', 'male')
micaela = User('micaela', 'chan', '31', 'female')
rosalee = User('rosalee', 'chan', '29', 'female')

admin_privileges = ['can add post', 'can delete post', 'can ban user']
brian = Admin('brian', 'rodriguez', '37', 'male', admin_privileges)

matt.describe_user()
matt.greet_user()
micaela.describe_user()
micaela.greet_user()
rosalee.describe_user()
rosalee.greet_user()

brian.privileges.show_privileges()
    