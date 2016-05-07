#: E111 E118
if x > 2:
  print x
#: E111 E118
if True:
     print
#: E112
if False:
print
#: E113
print
    print
#: E114 E116
mimetype = 'application/x-directory'
     # 'httpd/unix-directory'
create_date = False
#: E117 W191
if True:
		print
#: E111 E118
for a in 'abc':
    for b in 'xyz':
         print
#: E101 E118 W191
for a in 'abc':
    for b in 'xyz':
		print
#: E101 E111 E117 W191 W191 W191
for a in 'abc':
	print
	for b in 'xyz':
	     print
#: E101 E111 E117 W191 W191
for a in 'abc':
	for b in 'xyz':
	     print
#: E116 E116 E116
def start(self):
    if True:
        self.master.start()
        # try:
            # self.master.start()
        # except MasterExit:
            # self.shutdown()
        # finally:
            # sys.exit()
#: E115 E115 E115 E115 E115 E115
def start(self):
    if True:
#       try:
#           self.master.start()
#       except MasterExit:
#           self.shutdown()
#       finally:
#           sys.exit()
        self.master.start()
