#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint

import dlint_plugin_sys


class TestDlintSysChecker(dlint.test.base.BaseTest):

    def test_sys_usage(self):
        python_string = self.get_ast_node(
            """
            import sys

            sys.exit(0)
            """
        )

        linter = dlint_plugin_sys.DlintSysChecker()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint_plugin_sys.DlintSysChecker._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
