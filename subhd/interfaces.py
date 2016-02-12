class IArchiveHandler(object):
    def __init__(self, *, archive):
        self.archive = archive

    def iter_files(self):
        raise NotImplementedError()

    def extract_subtitles(self):
        subtitles = []
        for subtitle_file in self.iter_files():
            subtitles.append(subtitle_file)
        return subtitles
