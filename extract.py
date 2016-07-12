__author__ = 'Scott Deng'
import os, string, shutil, re, sys
import pefile
from pefile import DIRECTORY_ENTRY

def parse_tables(absPath):
    f = open(absPath + ".out", 'w')
    print "file: " + absPath
    pe = pefile.PE(absPath)
    print "\n----Import table----"
    f.write("---Import table---\n")

    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print entry.dll
        for imp in entry.imports:
            print '\t', imp.name
            f.write(entry.dll + ","+ imp.name +"\n")

    print "\n----Export table----"
    f.write("----Export table----\n")
    for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print '\t', exp.name
        f.write(exp.name +"\n")

    f.close()

def main():
    fname = sys.argv[1]
    absPath = os.path.abspath(fname)
    parse_tables(absPath)


if __name__ == "__main__":
    main()
