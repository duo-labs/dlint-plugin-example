#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import dlint


class DlintSysChecker(dlint.linters.helpers.bad_module_use.BadModuleUseLinter):
    off_by_default = False

    _code = 'DUO401'
    _error_tmpl = 'DUO401 use of "sys" not allowed'

    @property
    def illegal_modules(self):
        return [
            'sys',
        ]
