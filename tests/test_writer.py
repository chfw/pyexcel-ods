import os

from base import PyexcelWriterBase, PyexcelHatWriterBase
from pyexcel_io import get_data
from pyexcel_ods.odsw import ODSWriter as Writer


class TestNativeODSWriter:
    def test_write_book(self):
        self.content = {
            "Sheet1": [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
            "Sheet2": [[4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]],
            "Sheet3": [["X", "Y", "Z"], [1, 4, 7], [2, 5, 8], [3, 6, 9]],
        }
        self.testfile = "writer.ods"
        writer = Writer(self.testfile, "ods")
        writer.write(self.content)
        writer.close()
        content = get_data(self.testfile, library="pyexcel-ods")
        assert content == self.content

    def teardown_method(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)


class TestodsnCSVWriter(PyexcelWriterBase):
    def setup_method(self):
        self.testfile = "test.ods"
        self.testfile2 = "test.csv"

    def teardown_method(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)
        if os.path.exists(self.testfile2):
            os.unlink(self.testfile2)


class TestodsHatWriter(PyexcelHatWriterBase):
    def setup_method(self):
        self.testfile = "test.ods"

    def teardown_method(self):
        if os.path.exists(self.testfile):
            os.unlink(self.testfile)
