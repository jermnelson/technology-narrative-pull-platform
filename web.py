#-------------------------------------------------------------------------------
# Name:        web
# Purpose:     Lightweight web server for Code4Lib Article
#
# Author:      Jeremy Nelson
#
# Created:     2014/07/31
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     GPLv2
#-------------------------------------------------------------------------------
import markdown
import os
import re

from flask import abort, Flask

filepath_re = re.compile(r"\((.+)\)")
article = Flask(__name__)

@article.route("/")
def index():
    raw_article = open('README.md').read()
    summary = open('SUMMARY.md').read()
    for row in summary.splitlines():
        result = filepath_re.search(row)
        if result is not None:
            filename = result.groups()[0]
            raw_article += open(filename).read()
    return markdown.markdown(raw_article)

def main():
    host = '0.0.0.0'
    port = 8200
    article.run(
        host=host,
        port=port,
        debug=True)

if __name__ == '__main__':
    main()
