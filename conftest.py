import os
from typing import Dict

from utils.settings.settings import Settings


def pytest_addoption(parser):
    parser.addoption("--source_file", default=f"{os.path.dirname(os.path.realpath(__file__))}/file1.txt",
                     help="Source file path")
    parser.addoption("--replica_file", default=f"{os.path.dirname(os.path.realpath(__file__))}/file2.txt",
                     help="Replica file path")
    parser.addoption("--seconds_period", default=10, help="Period of time to make sync (in seconds)")


options: Dict[str, str] = {}


def pytest_configure(config):
    global options
    options["source_file"] = config.getoption("source_file")
    options["replica_file"] = config.getoption("replica_file")
    options["seconds_period"] = config.getoption("seconds_period")
    Settings.update_settings(options)
