# -------------------------
# Developed by Anisuzzaman
# Web Scrapping Main
# pip install beautifulsoup4
# -------------------------

from tools import wlog
errorPath = "error_log/error.log"

# Handle Exception
wlog.set_custom_log_info(errorPath)
# --------------------

# Try Exception Block Dummy Testing --------
# try:
#     raise Exception
# except Exception as e:
#     wlog.report(str(e))
# -------------------------------
