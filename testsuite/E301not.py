class X:

    def a():
        pass

    # comment
    def b():
        pass

    # This is a
    # ... multi-line comment

    def c():
        pass


# This is a
# ... multi-line comment

@some_decorator
class Y:

    def a():
        pass

    # comment

    def b():
        pass

    @property
    def c():
        pass


try:
    from nonexistent import Bar
except ImportError:
    class Bar(object):
        """This is a Bar replacement"""


def with_feature(f):
    """Some decorator"""
    wrapper = f
    if has_this_feature(f):
        def wrapper(*args):
            call_feature(args[0])
            return f(*args)
    return wrapper


try:
    next
except NameError:
    def next(iterator, default):
        for item in iterator:
            return item
        return default
