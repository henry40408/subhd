import rarfile

from subhd.interfaces import IArchiveHandler
from subhd.utils import SubtitleFile


class RarHandler(IArchiveHandler):
    def iter_files(self):
        archive = rarfile.RarFile(self.archive)
        for file_info in archive.infolist():
            file = archive.open(file_info.filename)
            yield SubtitleFile(filename=file_info.filename,
                               content=file.read())