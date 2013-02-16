import sublime, sublime_plugin
import re


class GaryutenCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        clip = sublime.get_clipboard()
        if re.search('\n$', clip):
            n = re.sub('\n$', '', clip)
            self.view.replace(edit, self.view.sel()[0], n)
        else:
            self.view.replace(edit, self.view.sel()[0], clip)
