import argparse

import inflect

from subhd.search import SubHDSearch
from subhd.utils import truncate

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
        locale_and_ext = subtitle.filename.split(".")[-2:]
        return ".".join([self.filename] + locale_and_ext)

    def choose_subtitle(self):
        self.search = SubHDSearch(keyword=self.filename)
        for index, entry in enumerate(self.search.entries()):
            print("{0:02d}) {1}".format(index + 1, truncate(entry.name, 73)))
        choice = int(input("Number of subtitle to download: "))
        return choice

    def main(self):
        choice = self.choose_subtitle()
        subtitle = self.search.select_subtitle(choice=choice)

        subtitles = subtitle.translate_subtitles()
        for subtitle in subtitles:
            new_filename = truncate(self.subtitle_filename(subtitle))
            save_subtitle(subtitle, new_filename)
            print("{0} => {1}".format(truncate(subtitle.filename),
                                      new_filename))

        plural = p.plural("subtitle", len(subtitles))
        print("{0} {1} downloaded.".format(len(subtitles), plural))


if __name__ == "__main__":
    app = SubHDApp()
    app.main()
