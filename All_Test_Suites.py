import unittest
from EEprojectFinal.test_signup import signup
from EEprojectFinal.test_login import login
from EEprojectFinal.test_addtocart import Addtocart
from EEprojectFinal.test_contact import contact
from EEprojectFinal.test_search import search

#Importing all the tests from each functionality

t1 = unittest.TestLoader().loadTestsFromTestCase(signup)
t2 = unittest.TestLoader().loadTestsFromTestCase(login)
t3 = unittest.TestLoader().loadTestsFromTestCase(Addtocart)
t4 = unittest.TestLoader().loadTestsFromTestCase(contact)
t5 = unittest.TestLoader().loadTestsFromTestCase(search)

#Creating test suites
Authentication = unittest.TestSuite([t1,t2])

Functionalities = unittest.TestSuite([t3,t4,t5])

Master = unittest.TestSuite([t1,t2,t3,t4,t5])

unittest.TextTestRunner().run(Master)