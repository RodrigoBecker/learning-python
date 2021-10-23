"""
PEP8 - Python Enhacement Proposal

Zem of Python

--> import this (easter egg)

import this
-------------------------------------------------------------------------
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
--------------------------------------------------------------------------

PEP8 - Enhancement Proposal

[1] - Use CameCase for class name

example:
    class Employer:
         ....

[2] - Use snake_case for functions and variables

example:
    def get_user_by_id():
        ...
    employer_id=01

[3] - Use 4 space for indentition (Not recomended tab space)

example:

    def get_user_id():
    .... start block

[4] - Add Line blanck in finaly instruction

[5] - Use "import" should only be in one statement.

example:

    import database (Correct)
    import database, services (Wrong)

Execption notation:
    from types import StringType, ListType
    from typer import (
        Stringtype,
        ListType,
        DictType
    )

[6] - Not add space in expression and instructions

example:

    def get_by_id   (  params  ,   { dict_date:  "" }) (wrong)
    x =             1 (wrong)
    y=              2 (wrong)
"""
