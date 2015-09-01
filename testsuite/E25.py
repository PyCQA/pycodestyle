#: E251 E251
def foo(bar = False):
    '''Test function with an error in declaration'''
    pass
#: E251
foo(bar= True)
#: E251
foo(bar =True)
#: E251 E251
foo(bar = True)
#: E251
y = bar(root= "sdasd")
#: E251:2:29
parser.add_argument('--long-option',
                    default=
                    "/rather/long/filesystem/path/here/blah/blah/blah")
#: E251:1:45
parser.add_argument('--long-option', default
                    ="/rather/long/filesystem/path/here/blah/blah/blah")
#: E251:3:8 E251:3:10
foo(True,
    baz=(1, 2),
    biz = 'foo'
    )
#: Okay
foo(bar=(1 == 1))
foo(bar=(1 != 1))
foo(bar=(1 >= 1))
foo(bar=(1 <= 1))
(options, args) = parser.parse_args()
d[type(None)] = _deepcopy_atomic

# Annotated Function Definitions
#: Okay
def munge(input: AnyStr, sep: AnyStr = None, limit=1000) -> AnyStr:
    pass
