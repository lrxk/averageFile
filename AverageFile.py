import os
import argparse

def args():
    parser=argparse.ArgumentParser(description="Arguments and their description",usage='%(prog)s [-h] [--p PATH] [-fe FILE_EXTENSION]',
                                         epilog="Use -h or --help to see more about arguments"
)
    parser.add_argument('--path','-p',default=os.path.curdir,type=str,help='Enter path to folder')
    parser.add_argument('--file_extension','-fe',type=str,help="Give the file extension (csv,txt etc)")
    args=parser.parse_args()
    return args