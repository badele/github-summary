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

    def generatesummary(self, args):
        githubsummary.generateSummary(args)

        self.assertTrue(os.path.isfile(EXAMPLE_RST) == 1)
        example = open(EXAMPLE_RST).read()
        self.assertIn('fabrecipes', example)
        self.assertIn('gitcheck', example)
        self.assertIn(' hours', example)

    def test_jsonfile(self):
        self.assertTrue(not githubsummary.openJSONFile('no_projects.json'))
        json = githubsummary.openJSONFile('example_projects.json')
        self.assertIs(type(json), dict)
        self.assertIn('github-summary', json)

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

    def test_withoutparams(self):
        # Test default value
        args = githubsummary.parse_arguments("".split())
        self.assertEqual(args.jsonfile, None)
        self.assertEqual(args.template, None)
        self.assertEqual(args.saveto, None)

        # Without saveto
        with self.assertRaises(SystemExit) as cm:
            githubsummary.generateSummary(args)
        self.assertEqual(cm.exception.code, 1)

        # With saveto
        cmd = "-s %s" % EXAMPLE_RST
        args = githubsummary.parse_arguments(cmd.split())
        self.deleteFile(EXAMPLE_RST)
        githubsummary.generateSummary(args)

        cmd = "-s %s -j example_projects.json" % EXAMPLE_RST
        args = githubsummary.parse_arguments(cmd.split())
        self.deleteFile(EXAMPLE_RST)
        githubsummary.generateSummary(args)

        # test content
        self.assertTrue(os.path.isfile(EXAMPLE_RST) == 1)
        example = open(EXAMPLE_RST).read()
        self.assertIn('fabrecipes', example)
        self.assertIn('gitcheck', example)
        self.assertIn(' hours', example)

    def test_params(self):
        # Test standard value
        cmdline = "-t rst/index-fr.rst -s %s -j example_projects.json" % EXAMPLE_RST
        args = githubsummary.parse_arguments(cmdline.split())
        self.assertEqual(args.jsonfile, 'example_projects.json')
        self.assertEqual(args.template, 'rst/index-fr.rst')
        self.assertEqual(args.saveto, EXAMPLE_RST)
        self.deleteFile(EXAMPLE_RST)
        githubsummary.generateSummary(args)

        # test content
        self.assertTrue(os.path.isfile(EXAMPLE_RST) == 1)
        example = open(EXAMPLE_RST).read()
        self.assertIn('fabrecipes', example)
        self.assertIn('gitcheck', example)
        self.assertIn(' heures', example)

        # Test bad template path
        cmdline = "-t rst/badpath.rst -s %s -j example_projects.json" % EXAMPLE_RST
        args = githubsummary.parse_arguments(cmdline.split())
        self.deleteFile(EXAMPLE_RST)
        with self.assertRaises(SystemExit) as cm:
            githubsummary.generateSummary(args)
        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
