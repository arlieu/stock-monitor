import multiprocessing


def updateProcessCount():
    return multiprocessing.cpu_count()


def distribueStocks(cpus):
    stockCount = 505
    remainder = 0
    if stockCount % cpus > 0:
        remainder = stockCount % cpus

    stockAllocation = stockCount // cpus

    return stockAllocation, remainder


# if __name__ == "__main__":
    # updateProcessCount()
    # distribueStocks()
    # print("TOTAL CPUS: %d\nSTOCKS PER CORE: %d\nREMAINDER: %d" % (cpus, stockAllocation, remainder))