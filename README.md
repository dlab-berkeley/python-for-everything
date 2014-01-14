python-fundamentals
===================

These resources are available at
http://github.com/dlab-berkeley/python-fundamentals

Materials for teaching and learning at the Python FUNdamentals workshop at UC
Berkeley's D-lab.

[Read only access to course slides.](http://j.mp/dlab-python-fun)

There are two approaches to going through this material. One is by going through
the numbered directories in order in the challenges directory. There, you can
use pytest (or your preferred test runner) to build up the requested code and
programs. Confusingly, the pytest command-line program is called `py.test` (for
historical reasons). From the root python-fundamentals directory (where you'll
also find this README.md file!), execute:

    cd challenges/01-Intro
    python A_<tab>

Note that &lt;tab&gt; above means "press the tab key" - that way you don't need to
type everything out. Now, you've executed your first python script! (or maybe
your 100th...) To continue, go through each python (.py) file alphabetically.
For each file, there's an associated test_A_...py file. You run this like so:

    py.test test_A<tab>

OR...

These materials may accompany the following lessons in [the Python
track at Codecademy](http://www.codecademy.com/tracks/python)

 - [What is Python, Python Syntax](http://www.codecademy.com/courses/introduction-to-python-6WeG3?curriculum_id=4f89dab3d788890003000096)
 - [Strings and Console](http://www.codecademy.com/courses/python-beginner-sRXwR?curriculum_id=4f89dab3d788890003000096)
 - [Conditionals and Control Flow](http://www.codecademy.com/courses/python-beginner-BxUFN?curriculum_id=4f89dab3d788890003000096)
 - [Functions](http://www.codecademy.com/courses/python-beginner-c7VZg?curriculum_id=4f89dab3d788890003000096)
 - [Lists and Dictionaries](http://www.codecademy.com/courses/python-beginner-en-pwmb1?curriculum_id=4f89dab3d788890003000096)
 - [Lists and Functions](http://www.codecademy.com/courses/python-beginner-nzzVa?curriculum_id=4f89dab3d788890003000096)
 - [Loops](http://www.codecademy.com/courses/python-beginner-en-cxMGf?curriculum_id=4f89dab3d788890003000096)
 - [Classes/Objects](http://www.codecademy.com/courses/python-intermediate-en-WL8e4?curriculum_id=4f89dab3d788890003000096)
 - [File Input and Output](http://www.codecademy.com/courses/python-intermediate-en-OGNHh?curriculum_id=4f89dab3d788890003000096)

Our "official" course textbook is [Think Python](http://www.greenteapress.com/thinkpython).

More help:

 - [Moral support](http://doc.pyschools.com/html/tao.html)
 - [Help fixing things](http://www.greenteapress.com/thinkpython/html/thinkpython021.html)

A more complete list of Python references:
    http://python.berkeley.edu

What's in this repository?
--------------------------

 - *cheat-sheets*: IPython notebooks illustrating basic concepts
 - *challenges*: python scripts (starting with capital letters) to progress through
as you learn, and test scripts (starting with `test_<capital letter>`) to
scaffold the approach.
