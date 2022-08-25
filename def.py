def toVolt(read):
    return read * 3.3 / 1023

def toRead(volt):
    return volt * 1023 / 3.3

