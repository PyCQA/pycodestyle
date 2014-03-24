#: E101 W191
for a in 'abc':
    for b in 'xyz':
        print a  # indented with 8 spaces
	print b  # indented with 1 tab
#: E101 E122 W191 W191
if True:
	pass

change_2_log = \
"""Change 2 by slamb@testclient on 2006/04/13 21:46:23

	creation
"""

p4change = {
    2: change_2_log,
}


class TestP4Poller(unittest.TestCase):
    def setUp(self):
        self.setUpGetProcessOutput()
        return self.setUpChangeSource()

    def tearDown(self):
        pass

#
#: E101 W191 W191
if True:
	foo(1,
	    2)
#: E101 E101 W191 W191
def test_keys(self):
    """areas.json - All regions are accounted for."""
    expected = set([
	u'Norrbotten',
	u'V\xe4sterbotten',
    ])
#:
