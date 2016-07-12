__author__ = 'Scott Deng'
import os, string, shutil, re, sys
import pefile
from pefile import DIRECTORY_ENTRY

def main():
    fname = sys.argv[1]
    #fname = "GIPSVoiceEngineDLL_MD.dll"

    absPath = os.path.abspath(fname)

    print "file: " + absPath
    pe = pefile.PE(absPath)

    print "\n----Import table----"
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print entry.dll
        for imp in entry.imports:
            print '\t', imp.name


    print "\n----Export table----"
    for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print '\t', exp.name

if __name__ == "__main__":
    main()
