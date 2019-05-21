#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import dlint


class DlintAbsChecker(dlint.linters.helpers.bad_builtin_use.BadBuiltinUseLinter):
    off_by_default = False

    _code = 'DUO400'
    _error_tmpl = 'DUO400 use of "abs" not allowed'

    @property
    def illegal_builtin(self):
        return 'abs'
