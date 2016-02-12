import argparse
import re
import sys

import inflect
from tabulate import tabulate

from subhd.search import SubHDSearch

p = inflect.engine()


def save_subtitle(subtitle, new_filename):
    with open(new_filename, mode="w", encoding="utf8") as f:
        f.write(subtitle.content)


class SubHDApp(object):
    def __init__(self):
        self.filename = None
        self.search = None
        self.prepare_arguments()

    def prepare_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("filename")

        args = parser.parse_args()
        self.filename = args.filename

    def subtitle_filename(self, subtitle):
        ext = subtitle.filename.split(".")[-1]

        locale = subtitle.filename.split(".")[-2]
        if re.match(r"(chs|cht)", locale):
            locale = [locale]
        else:
            locale = []

        return ".".join([self.filename] + locale + [ext])

    def choose_subtitle(self):
        try:
            self.search = SubHDSearch(keyword=self.filename)

            table = [[i + 1, e.name]
                     for i, e in enumerate(self.search.entries())]
            table = [["#", "Name"]] + table
            print(tabulate(table, headers="firstrow"))

            return int(input("Number of subtitle to download (Ctrl+D to abort): "))
        except EOFError as e:
            print("Aborted.")
            sys.exit(0)

    def main(self):
        choice = self.choose_subtitle()
        subtitle = self.search.select_subtitle(choice=choice)

        subtitles = subtitle.translate_subtitles()
        for subtitle in subtitles:
            new_filename = self.subtitle_filename(subtitle)
            save_subtitle(subtitle, new_filename)
            print("{0} => {1}".format(subtitle.filename, new_filename))

        plural = p.plural("subtitle", len(subtitles))
        print("{0} {1} downloaded.".format(len(subtitles), plural))


if __name__ == "__main__":
    app = SubHDApp()
    app.main()
