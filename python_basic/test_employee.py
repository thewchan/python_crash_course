import unittest, random
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the employee class."""
    
    def setUp(self):
        """Creat an employee to use for all test methods."""
        first_name = 'Matt'
        last_name = 'Chan'
        salary = 48_000
        self.current_salary = int(salary)
        self.generic_employee = Employee(first_name, last_name, salary)
        
    
    def test_give_default_raise(self):
        """Test if defualt $5000 raise holds."""
        self.generic_employee.give_raise()
        self.assertEqual(
            self.generic_employee.salary, self.current_salary + 5000,
            )
        
    def test_give_custom_raise(self):
        """Test if custom raise holds."""
        raise_amount = random.randint(3000, 7000)
        self.generic_employee.give_raise(raise_amount)
        self.assertEqual(
            self.generic_employee.salary, self.current_salary + raise_amount,
            )

if __name__ == '__main__':
    unittest.main()