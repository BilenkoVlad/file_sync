import datetime
import filecmp
import os
import shutil
import time

from utils.logger.own_logger import OwnLogger
from utils.settings.settings import Settings


class SyncFileTask:
    def __init__(self):
        self.own_logger = OwnLogger().logger
        self.source_file = Settings().source_file
        self.replica_file = Settings().replica_file
        self.seconds_period = Settings().seconds_period

    def check_file_are_the_same(self) -> bool:
        is_same = filecmp.cmp(self.source_file, self.replica_file)
        self.own_logger.info(f"File {self.source_file} and {self.replica_file} is the same: {is_same}")
        return is_same

    def check_folders_are_exist(self) -> bool:
        if not os.path.exists(self.source_file):
            self.own_logger.info("Source file is not exist")
            return False
        if not os.path.exists(self.replica_file):
            self.own_logger.info("Replica file is not exist")
            with open(self.replica_file, 'w'):
                pass
            self.own_logger.info("Replica file is created")
            return True

    def copy_source_to_replica(self, is_same):
        if is_same:
            os.remove(self.replica_file)
            self.own_logger.info("Replica file was removed")
        else:
            shutil.copy2(self.source_file, self.replica_file)
            self.own_logger.info(f"Source file {self.source_file} is copied to {self.replica_file}")

    def sync_files(self):
        self.own_logger.info("Sync files is started")
        current_time = datetime.datetime.now()
        time_to_exit = current_time + datetime.timedelta(0, self.seconds_period)

        while True:
            time.sleep(1)

            self.check_folders_are_exist()
            is_files_the_same = self.check_file_are_the_same()
            self.copy_source_to_replica(is_same=is_files_the_same)

            if datetime.datetime.now() >= time_to_exit:
                self.own_logger.info("Sync files is finished")
                break
