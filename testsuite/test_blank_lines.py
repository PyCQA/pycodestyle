"""
Tests for the blank_lines checker.

It uses dedicated assertions which work with TestReport.
"""
import unittest

import pycodestyle
from testsuite.support import InMemoryReport


class BlankLinesTestCase(unittest.TestCase):
    """
    Common code for running blank_lines tests.
    """

    def check(self, content):
        """
        Run checks on `content` and return the the list of errors.
        """
        sut = pycodestyle.StyleGuide()
        reporter = sut.init_report(InMemoryReport)
        sut.input_file(
            filename='in-memory-test-file.py',
            lines=content.splitlines(True),
        )
        return reporter.in_memory_errors

    def assertNoErrors(self, actual):
        """
        Check that the actual result from the checker has no errors.
        """
        self.assertEqual([], actual)


class TestBlankLinesDefault(BlankLinesTestCase):
    """
    Tests for default blank with 2 blank lines for top level and 1
    blank line for methods.
    """

    def test_initial_no_blank(self):
        """
        It will accept no blank lines at the start of the file.
        """
        result = self.check("""def some_function():
    pass
""")

        self.assertNoErrors(result)

    def test_initial_lines_one_blank(self):
        """
        It will accept 1 blank lines before the first line of actual
        code, even if in other places it asks for 2
        """
        result = self.check("""
def some_function():
    pass
""")

        self.assertNoErrors(result)

    def test_initial_lines_two_blanks(self):
        """
        It will accept 2 blank lines before the first line of actual
        code, as normal.
        """
        result = self.check("""

def some_function():
    pass
""")

        self.assertNoErrors(result)

    def test_method_less_blank_lines(self):
        """
        It will trigger an error when less than 1 blank lin is found
        before method definitions.
        """
        result = self.check("""# First comment line.
class X:

    def a():
        pass
    def b():
        pass
""")
        self.assertEqual([
            'E301:6:5',  # b() call
        ], result)

    def test_method_less_blank_lines_comment(self):
        """
        It will trigger an error when less than 1 blank lin is found
        before method definition, ignoring comments.
        """
        result = self.check("""# First comment line.
class X:

    def a():
        pass
    # A comment will not make it better.
    def b():
        pass
""")
        self.assertEqual([
            'E301:7:5',  # b() call
        ], result)

    def test_top_level_fewer_blank_lines(self):
        """
        It will trigger an error when less 2 blank lines are found
        before top level definitions.
        """
        result = self.check("""# First comment line.
# Second line of comment.

def some_function():
    pass

async def another_function():
    pass


def this_one_is_good():
    pass

class SomeCloseClass(object):
    pass


async def this_async_is_good():
    pass


class AFarEnoughClass(object):
    pass
""")
        self.assertEqual([
            'E302:4:1',  # some_function
            'E302:7:1',  # another_function
            'E302:14:1',  # SomeCloseClass
        ], result)

    def test_top_level_more_blank_lines(self):
        """
        It will trigger an error when more 2 blank lines are found
        before top level definitions.
        """
        result = self.check("""# First comment line.
# Second line of comment.



def some_function():
    pass


def this_one_is_good():
    pass



class SomeFarClass(object):
    pass


class AFarEnoughClass(object):
    pass
""")
        self.assertEqual([
            'E303:6:1',  # some_function
            'E303:15:1',  # SomeFarClass
        ], result)

    def test_method_more_blank_lines(self):
        """
        It will trigger an error when more than 1 blank line is found
        before method definition
        """
        result = self.check("""# First comment line.


class SomeCloseClass(object):


    def oneMethod(self):
        pass


    def anotherMethod(self):
        pass

    def methodOK(self):
        pass



    def veryFar(self):
        pass
""")
        self.assertEqual([
            'E303:7:5',  # oneMethod
            'E303:11:5',  # anotherMethod
            'E303:19:5',  # veryFar
        ], result)

    def test_initial_lines_more_blank(self):
        """
        It will trigger an error for more than 2 blank lines before the
        first line of actual code.
        """
        result = self.check("""


def some_function():
    pass
""")
        self.assertEqual(['E303:4:1'], result)

    def test_blank_line_between_decorator(self):
        """
        It will trigger an error when the decorator is followed by a
        blank line.
        """
        result = self.check("""# First line.


@some_decorator

def some_function():
    pass


class SomeClass(object):

    @method_decorator

    def some_method(self):
        pass
""")
        self.assertEqual(['E304:6:1', 'E304:14:5'], result)

    def test_blank_line_decorator(self):
        """
        It will accept the decorators which are adjacent to the function
        and method definition.
        """
        result = self.check("""# First line.


@another_decorator
@some_decorator
def some_function():
    pass


class SomeClass(object):

    @method_decorator
    def some_method(self):
        pass
""")
        self.assertNoErrors(result)

    def test_top_level_fewer_follow_lines(self):
        """
        It will trigger an error when less than 2 blank lines are
        found between a top level definitions and other top level code.
        """
        result = self.check("""
def a():
    print('Something')

a()
""")
        self.assertEqual([
            'E305:5:1',  # a call
        ], result)

    def test_top_level_fewer_follow_lines_comments(self):
        """
        It will trigger an error when less than 2 blank lines are
        found between a top level definitions and other top level code,
        even if we have comments before
        """
        result = self.check("""
def a():
    print('Something')

    # comment

    # another comment

# With comment still needs 2 spaces before,
# as comments are ignored.
a()
""")
        self.assertEqual([
            'E305:11:1',  # a call
        ], result)

    def test_top_level_good_follow_lines(self):
        """
        It not trigger an error when 2 blank lines are
        found between a top level definitions and other top level code.
        """
        result = self.check("""
def a():
    print('Something')

    # Some comments in other parts.

    # More comments.


# With the right spaces,
# It will work, even when we have comments.
a()
""")
        self.assertNoErrors(result)

    def test_method_fewer_follow_lines(self):
        """
        It will trigger an error when less than 1 blank line is
        found between a method and previous definitions.
        """
        result = self.check("""
def a():
    x = 1
    def b():
        pass
""")
        self.assertEqual([
            'E306:4:5',  # b() call
        ], result)

    def test_method_nested_fewer_follow_lines(self):
        """
        It will trigger an error when less than 1 blank line is
        found between a method and previous definitions, even when
        nested.
        """
        result = self.check("""
def a():
    x = 2

    def b():
        x = 1
        def c():
            pass
""")
        self.assertEqual([
            'E306:7:9',  # c() call
        ], result)

    def test_method_nested_less_class(self):
        """
        It will trigger an error when less than 1 blank line is found
        between a method and previous definitions, even when used to
        define a class.
        """
        result = self.check("""
def a():
    x = 1
    class C:
        pass
""")
        self.assertEqual([
            'E306:4:5',  # class C definition.
        ], result)

    def test_method_nested_ok(self):
        """
        Will not trigger an error when 1 blank line is found
        found between a method and previous definitions, even when
        nested.
        """
        result = self.check("""
def a():
    x = 2

    def b():
        x = 1

        def c():
            pass

    class C:
        pass
""")
        self.assertNoErrors(result)


class TestBlankLinesTwisted(BlankLinesTestCase):
    """
    Tests for blank_lines with 3 blank lines for top level and 2 blank
    line for methods as used by the Twisted coding style.
    """

    def setUp(self):
        self._original_lines_config = pycodestyle.BLANK_LINES_CONFIG.copy()
        pycodestyle.BLANK_LINES_CONFIG['top_level'] = 3
        pycodestyle.BLANK_LINES_CONFIG['method'] = 2

    def tearDown(self):
        pycodestyle.BLANK_LINES_CONFIG = self._original_lines_config

    def test_initial_lines_one_blanks(self):
        """
        It will accept less than 3 blank lines before the first line of
        actual code.
        """
        result = self.check("""


def some_function():
    pass
""")

        self.assertNoErrors(result)

    def test_initial_lines_tree_blanks(self):
        """
        It will accept 3 blank lines before the first line of actual
        code, as normal.
        """
        result = self.check("""


def some_function():
    pass
""")

        self.assertNoErrors(result)

    def test_top_level_fewer_blank_lines(self):
        """
        It will trigger an error when less 2 blank lines are found
        before top level definitions.
        """
        result = self.check("""# First comment line.
# Second line of comment.


def some_function():
    pass


async def another_function():
    pass



def this_one_is_good():
    pass

class SomeCloseClass(object):
    pass



async def this_async_is_good():
    pass



class AFarEnoughClass(object):
    pass
""")
        self.assertEqual([
            'E302:5:1',  # some_function
            'E302:9:1',  # another_function
            'E302:17:1',  # SomeCloseClass
        ], result)

    def test_top_level_more_blank_lines(self):
        """
        It will trigger an error when more 2 blank lines are found
        before top level definitions.
        """
        result = self.check("""# First comment line.
# Second line of comment.




def some_function():
    pass



def this_one_is_good():
    pass




class SomeVeryFarClass(object):
    pass



class AFarEnoughClass(object):
    pass
""")
        self.assertEqual([
            'E303:7:1',  # some_function
            'E303:18:1',  # SomeVeryFarClass
        ], result)

    def test_the_right_blanks(self):
        """
        It will accept 3 blank for top level and 2 for nested.
        """
        result = self.check("""


def some_function():
    pass



# With comments.
some_other = code_here



class SomeClass:
    '''
    Docstring here.
    '''

    def some_method():
        pass


    def another_method():
        pass


    # More methods.
    def another_method_with_comment():
        pass


    @decorator
    def another_method_with_comment():
        pass
""")

        self.assertNoErrors(result)
