# IDLEX EXTENSION
##    """
##    Copyright(C) 2011 The Board of Trustees of the University of Illinois.
##    All rights reserved.
##
##    Developed by:   Roger D. Serwy
##                    University of Illinois
##
##    Permission is hereby granted, free of charge, to any person obtaining
##    a copy of this software and associated documentation files (the
##    "Software"), to deal with the Software without restriction, including
##    without limitation the rights to use, copy, modify, merge, publish,
##    distribute, sublicense, and/or sell copies of the Software, and to
##    permit persons to whom the Software is furnished to do so, subject to
##    the following conditions:
##
##    + Redistributions of source code must retain the above copyright
##      notice, this list of conditions and the following disclaimers.
##    + Redistributions in binary form must reproduce the above copyright
##      notice, this list of conditions and the following disclaimers in the
##      documentation and/or other materials provided with the distribution.
##    + Neither the names of Roger D. Serwy, the University of Illinois, nor
##      the names of its contributors may be used to endorse or promote
##      products derived from this Software without specific prior written
##      permission.
##
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
##    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
##    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
##    IN NO EVENT SHALL THE CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR
##    ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
##    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
##    THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE SOFTWARE.
##
##
##
##
##    Pep8 Check Extension
##
##      by zhang jifu, zaazbb@163.com .
##
##    About:
##
##        Pep8 cheack.
##
##    Usage:
##        click Edit>Pep8 Check, or press Ctrl+p, run the pep8 checker.
##
##    Install:
##        1 - install pep8 from pypi: https://pypi.python.org/pypi/pep8 .
##          $ pip install pep8
##        2 - install as a idle/idlex extersion.
##          for idlex, just copy to idlexlib/extensions/ dir.
##          for official idle:
##              copy to Python??/Lib/idlelib/ .
##              add below configs to Python??/Lib/idlelib/config-extensions.def.
##                  [Pep8Check]
##                  enable=1
##                  enable_shell=0
##
##
##    """


config_extension_def = """
[Pep8Check]
enable=1
enable_shell=0

[Pep8Check_cfgBindings]
pep8-check=<Alt-Key-p>

"""

import sys

if sys.version < '3':
    from Tkinter import *
else:
    from tkinter import *

    
import io

import pep8


PEP8_LIST_HEIGHT = 10


class Pep8Check:
    menudefs = [
        ('edit', [
            None, # Separator
            ('Pep8 Check', '<<pep8-check>>'),
         ])
    ]

    def __init__(self, editwin):
        self.editwin = editwin
        self.text = editwin.text
        self.frame = None

        editwin.text.bind('<<pep8-check>>', self.pep8_check_event)


    def pep8_check_event(self, event=None):
        if not self.frame:
            self.text['height'] -= PEP8_LIST_HEIGHT - 1

            self.frame = frame = Frame(self.editwin.top)
            list_ = Listbox(frame, height=PEP8_LIST_HEIGHT, setgrid=1)
            scroll = Scrollbar(frame)
            scroll['command'] = list_.yview
            list_['yscroll'] = scroll.set
            list_.pack(side='left', fill='x', expand=1)
            scroll.pack(side='left', fill='y')
            frame.pack(side='bottom', fill='x', before=self.editwin.text_frame)

            stdout = sys.stdout
            sys.stdout = file = io.StringIO() 
    
            pep8style = pep8.StyleGuide(
                    format='%(row)4d:%(col)2d: %(code)5s %(text)s')
            error_count = pep8style.input_file('stdin',
                    lines=self.text.get('1.0', 'end').splitlines(keepends=True))
            list_.insert(0, *file.getvalue().splitlines())

            self.text.tag_configure('pep8',
                                    background=self.text['selectbackground'])
            
            def set_view(event):
                s = list_.get(list_.curselection())
                cols = s.split(':', 2)
                row = int(cols[0])
                col = int(cols[1]) - 1
                self.text.yview(row - 1)
                self.text.tag_remove('pep8', '1.0', 'end')
                self.text.tag_add('pep8', '%i.%i' % (row, col) , '%i.end' % row)

            list_.bind('<Double-1>', set_view)

            sys.stdout = stdout

        else:
            self.text['height'] += PEP8_LIST_HEIGHT - 1
            self.text.tag_delete('pep8')
            self.frame.destroy()
            self.frame = None
