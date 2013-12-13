#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = 'Bruno Adelé <bruno@adele.im>'
__copyright__ = 'Copyright (C) 2013 Bruno Adelé'
__description__ = """A tool to generate a
                  github summary in multiples formats
                   (TXT, Markdown, reStructuredText, HTML, etc ..."""
__license__ = 'GPLv3'
__version__ = '1.0'

import os
import sys
import json
import jinja2
import argparse
from github import Github
from collections import Counter, defaultdict, OrderedDict


# Load config file
if os.path.isfile(os.path.expanduser("~/.github-summary.py")):
    configfile = os.path.expanduser("~/.github-summary.py")
else:
    pydir = os.path.dirname(os.path.realpath(__file__))
    configfile = "%s/config.py" % pydir

execfile(configfile)


def generateSummary(args):
    """Generate github summary"""

    pydir = os.path.dirname(os.path.realpath(__file__))

    # Check if template exists
    tplfile = os.path.abspath("%s/templates/%s" % (
        pydir,
        args.template)
    )

    # Search if relative template path
    if not os.path.isfile(tplfile):
        tplfile = args.template

    if not os.path.isfile(tplfile):
        print "%s template not found" % tplfile
        sys.exit(1)

    # Clocktable
    clocktable = None
    if args.jsonfile:
        clocktable = openJSONFile(args.jsonfile)
        total_contribute = 0
        for key, value in clocktable.iteritems():
            total_contribute += int(value)

    # Create github instance
    g = Github(GITHUB_TOKEN)

    # Repos
    repos = g.get_user().get_repos()
    owner = sortReposBypopularity(filterRepos(repos, forked=False))
    contrib = sortReposBypopularity(filterRepos(repos, forked=True))
    countrepos = len(owner) + len(contrib)

    # Language
    reposlangs = convertPercent(summaryLanguages(repos))
    reposlanguages = OrderedDict(sorted(reposlangs.items(), key=lambda t: 100 - t[1]))
    ownerlangs = convertPercent(summaryLanguages(owner))
    ownerlanguages = OrderedDict(sorted(ownerlangs.items(), key=lambda t: 100 - t[1]))
    contriblangs = convertPercent(summaryLanguages(contrib))
    contriblanguages = OrderedDict(sorted(contriblangs.items(), key=lambda t: 100 - t[1]))

    # Prepare template
    tplenv = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath="/")
    )
    template = tplenv.get_template(os.path.abspath(tplfile))

    # Render
    content = template.render(
        {
            'g': g,
            'repos': repos,
            'owner': owner,
            'contrib': contrib,
            'countrepos': countrepos,
            'reposlanguages': reposlanguages,
            'ownerlanguages': reposlanguages,
            'contriblanguages': reposlanguages,
            'clocktable': clocktable,
            'total_contribute': total_contribute,
        }
    )

    saveto(args.saveto, content.encode('utf-8'))


def saveto(filename, content):
    out = open(filename, 'wb')
    out.write(content)
    out.close()


def openJSONFile(filename):
    jsonfile = os.path.abspath(filename)
    if not os.path.isfile(jsonfile):
        return None

    json_data = open(jsonfile)
    return json.load(json_data)


def convertPercent(obj):
    """Convert counter/dict in percent"""
    total = sum(obj.values())

    for key, value in obj.iteritems():
        obj[key] = int(round(value * 100 / total, 0))

    return obj


def summaryLanguages(repos, countbyte=False):
    """Analyse repos language and sort mos used language"""
    langs = defaultdict(float)
    total = 0

    for r in repos:
        for lang, value in r.get_languages().iteritems():
            if lang not in LANGUAGE_IGNORE:
                if countbyte:
                    langs[lang] += value
                    total += value
                else:
                    langs[lang] += 1
                    total += 1

    return dict(Counter(langs).most_common(LANGUAGE_NB))


def filterRepos(repos, forked=False):
    """Filter by forked repos"""
    result = list()

    for r in repos:
        if r.name not in PROJECT_IGNORE and r.fork == forked:
            result.append(r)

    return result


def sortReposBypopularity(repos):
    """Sort  by popularity"""
    return sorted(
        repos,
        key=lambda t: (
            t.forks + t.watchers,
            t.pushed_at.strftime('%s')
        ),
        reverse=True
    )


def parse_arguments():
    """Parse the arguments"""

    # Template default value
    tplfile = None
    pydir = os.path.dirname(os.path.realpath(__file__))

    # Check if template exists
    checkfile = os.path.abspath("%s/templates/%s" % (
        pydir,
        DEFAULT_TEMPLATE)
    )

    if os.path.isfile(checkfile):
        tplfile = DEFAULT_TEMPLATE

    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-c', '--config',
        action='store',
        dest='configfile',
        default=None,
        help='Config file'
    )

    parser.add_argument(
        '-j', '--jsonfile',
        action='store',
        dest='jsonfile',
        default=None,
        help='JSON project time file'
    )

    parser.add_argument(
        '-t', '--template',
        action='store',
        dest='template',
        default=tplfile,
        help='Template file'
    )

    parser.add_argument(
        '-s', '--saveto',
        action='store',
        dest='saveto',
        help='Save to'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__)
    )

    a = parser.parse_args()

    # TODO: make unit test for testing default values
    if not a.template:
        print "Please indicate the template file"
        sys.exit(1)

    if not a.saveto not in a:
        print "Please indicate filename to save"
        sys.exit(1)

    return a


def main():
    # Parse arguments
    args = parse_arguments()

    # Generate github summary
    generateSummary(args)


if __name__ == '__main__':
    main()
