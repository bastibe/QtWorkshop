from subprocess import Popen, STDOUT, PIPE
import sys
import os
import re

def qml_magic(args, cell):
    """Execute a block of QML code using qmlscene.

    This requires `qmlscene` to be available in your path. `qmlscene`
    does not read QML code from stdin, so this will create a temporary
    file that contains the cell's QML code. This file is deleted after
    `qmlscene` exits. All error messages referring to this file are
    redacted so they don't show the file name any more.

    All output of the QML program is printed in real time.

    If you want to pass additional arguments to `qmlscene` just append
    them to the `%%qml` magic. For instance, `%%qml -h` will print the
    `qmlscene` help text instead of executing your code.

    """
    filename = '.ipython_temp.qml'
    with open(filename, 'w') as f:
        f.write(cell)
    process = Popen(['qmlscene', args, filename],
                    stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    while True:
        nextline = process.stdout.readline()
        if not nextline:
            break
        # replace temp file url with line number
        sys.stdout.write(re.sub('file:.*{}:([0-9]+)'.format(filename),
                                r'line \1:', nextline))
        sys.stdout.flush()

    os.remove(filename)

get_ipython().register_magic_function(qml_magic, "cell", "qml")
