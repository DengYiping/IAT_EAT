import os
import sys
import pefile
import esm

def parse(absPath):
    print "file: " + absPath
    pe_file = pefile.PE(absPath)

    c = []
    for entry in pe_file.DIRECTORY_ENTRY_IMPORT:
        #print entry.dll
        for imp in entry.imports:
            #print '\t', imp.name
            c.append(imp.name)

    return set(list(c))


if __name__ == "__main__":
    filelist = ['1.exe','2.exe','3.exe', '4.exe']

    lst = []

    for f_comp in filelist:
        lst.append(parse(f_comp))

    u = set.intersection(*lst)
    print u
