import unittest

from tests.test_add import TestAddBook
from tests.test_status import TestUpdateStatus
from tests.test_search import TestSearchBook
from tests.test_list import TestListBook
from tests.test_delete import TestDeleteBook
from tests.test_empty_list import TestEmptyListBook

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(TestAddBook))
suite.addTests(loader.loadTestsFromTestCase(TestUpdateStatus))
suite.addTests(loader.loadTestsFromTestCase(TestSearchBook))
suite.addTests(loader.loadTestsFromTestCase(TestListBook))
suite.addTests(loader.loadTestsFromTestCase(TestDeleteBook))
suite.addTests(loader.loadTestsFromTestCase(TestEmptyListBook))


runner = unittest.TextTestRunner()
runner.run(suite)
