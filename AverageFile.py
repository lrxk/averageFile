import os
import argparse
import math
def args():
    parser=argparse.ArgumentParser(description="Arguments and their description",usage='%(prog)s [-h] [--p PATH] [-fe FILE_EXTENSION]',
                                         epilog="Use -h or --help to see more about arguments"
)
    parser.add_argument('--path','-p',default=os.path.curdir,type=str,help='Enter path to folder (if not give will read current folder)',required=False)
    parser.add_argument('--file_extension','-fe',type=str,help="Give the file extension (csv,txt etc)",required=True)
    args=parser.parse_args()
    return args
def get_files_and_their_sizes(args):
    directory_path=args.path
    extension=args.file_extension
    file_that_match_the_extension=[]
    file_size_that_match_the_extension=[]
    for file in os.listdir(directory_path):
        if file.endswith(extension):
            file_that_match_the_extension.append(file)
            file_size_that_match_the_extension.append(os.path.getsize(os.path.join(directory_path,file)))
    return file_that_match_the_extension,file_size_that_match_the_extension    
    