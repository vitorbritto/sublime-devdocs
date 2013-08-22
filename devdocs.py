# Written by Vitor Britto (code@vitorbritto.com.br / vitorbritto.com.br)
# based on Can I Use It Search Plugin by Tim Kleinschmidt (tim.kleinschmidt@gmail.com)

import sublime
import sublime_plugin
import re


# Outside pattern compilation to have better performance for multi selection
CLEAN_CSS_PATTERN = re.compile(r'([a-z-]+)', re.IGNORECASE)
BASE_URL = 'http://devdocs.io/#q='


class DevDocsCommand(sublime_plugin.TextCommand):
    """
    This will search a word or a selection.
    Default binding recommendation: "ctrl + alt + d"
    """

    def run(self, edit):
        for region in self.view.sel():
            # Get the start point of the region of the selection
            point = region.begin()
            scope = self.view.extract_scope(point)
            search = self.view.substr(scope)
            # Clean the selection
            re_search = CLEAN_CSS_PATTERN.search(search)
            if re_search:
                search = re_search.group()
            self.view.window().run_command('open_url', \
                {"url": BASE_URL + search})
