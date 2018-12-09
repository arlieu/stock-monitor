from multiprocessing import *


def updateProcessCount():
    return cpu_count()


def distribueStocks(cpus):
    stockCount = 505
    remainder = 0
    if stockCount % cpus > 0:
        remainder = stockCount % cpus

    stockAllocation = stockCount // cpus

    return stockAllocation, remainder
