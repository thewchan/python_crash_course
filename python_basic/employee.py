class Employee:
    """A deposit of indiviudal employee information."""
    
    def __init__(self, first, last, salary):
        """
        Initiate employee object with first and last name, and annual salary.
        """
        self.first = first
        self.last = last
        self.salary = int(salary)
    
    def give_raise(self, amount=5000):
        """Add $5,000 to the annual salary by default but accepts argument."""
        self.salary += amount
        