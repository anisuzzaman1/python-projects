from asyncio import Handle

# Handle Exception

from fileinput import filename
import logging


def set_custom_log_info(filename):
    logging.basicConfig(filename=filename, level=logging.INFO)


def report(e: Exception):
    logging.exception(str(e))
