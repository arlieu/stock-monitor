import multiprocessing
import threading


totalCpus = 0
stockAllocation = 0
remainder = 0


def updateProcessCount():
    global totalCpus
    totalCpus = multiprocessing.cpu_count()


def distribueStocks():
    stockCount = 505
    global totalCpus
    global stockAllocation
    global remainder
    if stockCount % totalCpus > 0:
        remainder = stockCount % totalCpus

    stockAllocation = stockCount // totalCpus


if __name__ == "__main__":
    updateProcessCount()
    distribueStocks()
    print("TOTAL CPUS: %d\nSTOCKS PER CORE: %d\nREMAINDER: %d" % (totalCpus, stockAllocation, remainder))