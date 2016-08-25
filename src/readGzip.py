import gzip
import sys

if __name__ == '__main__':
    arg_length = len(sys.argv)
    if arg_length < 2:
        print 'Usage: python gzipHalf.py <filename.gz> [number of lines to display]'
        sys.exit(-1)

    gzip_filename = sys.argv[1]
    if arg_length < 3:
        max = None
    else:
        max = int(sys.argv[2])

    count = 0
    with gzip.open(gzip_filename, 'rb') as zipped_file:
        for line in zipped_file:
            if max is None or count < max:
                print line
            count += 1