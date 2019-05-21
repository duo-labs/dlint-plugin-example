#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint

import dlint_plugin_abs


class TestDlintAbsChecker(dlint.test.base.BaseTest):

    def test_abs_usage(self):
        python_string = self.get_ast_node(
            """
            result = abs(0)
            """
        )

        linter = dlint_plugin_abs.DlintAbsChecker()
        linter.visit(python_string)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=9,
                message=dlint_plugin_abs.DlintAbsChecker._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
