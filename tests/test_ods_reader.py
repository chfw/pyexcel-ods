import os

from base import ODSCellTypes
from pyexcel_ods.odsr import ODSBook
from pyexcel_ods.odsw import ODSWriter
from pyexcel_io.reader import Reader


class TestODSReader(ODSCellTypes):
    def setup_method(self):
        r = Reader("ods")
        r.reader_class = ODSBook
        r.open(os.path.join("tests", "fixtures", "ods_formats.ods"))
        self.data = r.read_all()
        for key in self.data.keys():
            self.data[key] = list(self.data[key])
        r.close()


class TestODSWriter(ODSCellTypes):
    def setup_method(self):
        r = Reader("ods")
        r.reader_class = ODSBook
        r.open(os.path.join("tests", "fixtures", "ods_formats.ods"))
        r.close()
        self.data1 = r.read_all()
        self.testfile = "odswriter.ods"
        w = ODSWriter(self.testfile, "ods")
        w.write(self.data1)
        w.close()
        r.open(self.testfile)
        self.data = r.read_all()
        for key in self.data.keys():
            self.data[key] = list(self.data[key])

    def teardown_method(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)
