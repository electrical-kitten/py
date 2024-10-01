import pytest
from employee_class import Employee

@pytest.fixture

def initialize_person():
    test_person = Employee('vladislav', 'borodinsky', 0)
    return test_person

def test_give_default_raise(initialize_person):
    initialize_person.give_raise()
    assert initialize_person.anual_salary == 5000

def test_give_custom_raise(initialize_person):
    initialize_person.give_raise(10000)
    assert initialize_person.anual_salary == 10000 





