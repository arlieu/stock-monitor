from multiprocessing import *


def update_process_count():
    return cpu_count()


def distribue_stocks(cpus):
    stock_count = 505
    remainder = 0
    if stock_count % cpus > 0:
        remainder = stock_count % cpus

    stock_allocation = stock_count // cpus

    return stock_allocation, remainder
