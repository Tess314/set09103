import sqlite3

def convertToBinaryData(filename):
    #convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
