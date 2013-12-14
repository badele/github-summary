#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = 'Bruno Adelé <bruno@adele.im>'
__copyright__ = 'Copyright (C) 2013 Bruno Adelé'
__description__ = """Unittest"""
__license__ = 'GPLv3'


import os
import unittest

from githubsummary import githubsummary

EXAMPLE_RST = 'example.rst'


class TestPackages(unittest.TestCase):

    def deleteFile(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def test_convertPercent(self):
        langa = {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
        planga = githubsummary.convertPercent(langa)
        self.assertEqual(
            planga['a'],
            20
        )

        langb = {'a': 33, 'b': 33, 'c': 33, 'd': 33}
        plangb = githubsummary.convertPercent(langb)
        self.assertEqual(
            plangb['a'],
            25
        )

        langc = {'a': 12, 'b': 12, 'c': 12}
        plangc = githubsummary.convertPercent(langc)
        self.assertEqual(
            plangc['a'],
            33
        )

    def test_params(self):
        # Test default value
        with self.assertRaises(SystemExit) as cm:
            args = githubsummary.parse_arguments()

            self.assertEqual(args.template, 'rst/index-en.rst')
        self.assertEqual(cm.exception.code, 1)

        # Test with saveto
        self.deleteFile(EXAMPLE_RST)
        cmd = "-s %s -j example_projects.json" % EXAMPLE_RST
        args = githubsummary.parse_arguments(cmd.split())
        githubsummary.generateSummary(args)

        self.assertTrue(os.path.isfile(EXAMPLE_RST) == 1)
        example = open(EXAMPLE_RST).read()
        self.assertIn('fabrecipes', example)
        self.assertIn('gitcheck', example)
        self.assertIn(' hours', example)


if __name__ == "__main__":
    unittest.main(verbosity=2)
