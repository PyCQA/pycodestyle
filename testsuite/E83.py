#: E803
class Foo(object):
    @classmethod
    def mmm(cls, ads):
        pass

    @classmethod
    def bad(self, ads):
        pass

    @calling()
    def test(self, ads):
        pass
