import os
import time

from datetime import datetime

class Output():
    def __init__(self) -> None:
        self.startTime = time.time()

    def printHeader(self):
        print("################################################################################")
        print("")
        print("zeek_to_sqlite by 5f0")
        print("Creates a sqlite db from zeek logs")
        print("")
        print("Current working directory: " + os.getcwd())
        print("")
        print("Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("################################################################################")
        print("")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("################################################################################")
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")