from asyncore import file_dispatcher
from cgitb import html
from logging import exception
from msilib.schema import File
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Global Variable ------------------ #
# urlGrab = "https://www.aljazeera.com/"
exportFile = "export/scapped.html"
conversionType = "html.parser"
listObj = ['h1', 'h2', 'h3', 'h4']
# -------------------------- #


class urlScapper:
    # Default Value Declation #
    __url__ = ''
    __data__ = ''
    __wlog__ = None
    __soup__ = None
    # ---------------------- #

    # Constructor Method ------------- #
    def __init__(self, url, wlog):
        self.__url__ = url
        self.__wlog__ = wlog
    # ------------------------------- #

    # ------ Import Url Block ---------#
    def import_url(self):
        try:
            urlOpen = urlopen(self.__url__)
        except exception as e:
            # if Failed to open the through exception
            self.__wlog__.report(e)
        else:
            self.__data__ = urlOpen.read()
            if len(self.__data__) > 0:
                print("Retribe Successfully")
    # ---------------------------------- #

    # ---- Export/Write File Block  -------------- #
    def export_url(self, filepath=exportFile, data=''):
        try:
            with open(filepath, 'wb') as fileObj:
                if data:
                    fileObj.write(data)
                else:
                    fileObj.write(self.__data__)
        except exception as e:
            self.__wlog__.report(e)
    # ------------------------------------ #

    # ---- Read Local File/Exported File  -------------- #
    def read_local_file(self, filepath=exportFile):
        try:
            with open(filepath, 'wb') as fileObj:
                self.__data__ = fileObj.read()
        except exception as e:
            self.__wlog__.report(e)
    # ------------------------------------ #

    # If Needed to change Url -------- #
    def change_url(self, url):
        self.__url__ = url
    # ---------------------------- #

    def print_data(self):
        print(self.__data__)

    # BeautifulSoup Object Process -----#
    def covert_to_bs4(self):
        self.__soup__ = BeautifulSoup(self.__data__, conversionType)

    def export_soup_file(self):
        containList = self.__soup__.find_all(listObj)
    # ------------------------------ #
