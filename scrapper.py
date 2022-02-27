# -------------------------
# Developed by Anisuzzaman
# Web Scrapping Main
# pip install beautifulsoup4
# -------------------------

from tools import wlog
from tools import wscrape

# ----- Global Variable ----- #
errorPath = "error_log/error.log"
# urlGrab = "https://bangladeshkantha.com/"
# ------------------------------- #

# Handle Exception
wlog.set_custom_log_info(errorPath)

scapper = wscrape.UrlScappers(wscrape.urlGrab, wlog)
scapper.import_url()
scapper.export_url()
scapper.covert_to_bs4()
# scapper.print_data()
scapper.export_soup_file()

# Try Exception Block Dummy Testing --------
try:
    raise Exception
except Exception as e:
    wlog.report(e)
# -------------------------------
