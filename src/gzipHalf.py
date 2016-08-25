import gzip
import sys
import time

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python gzipHalf.py <filename.gz>'
        sys.exit(-1)

    gzip_filename = sys.argv[1]
    count = 0

    out_filename = 'out_' + gzip_filename

    last_out = None

    with gzip.open(out_filename, 'wb') as out_file:
        with gzip.open(gzip_filename, 'rb') as zipped_file:
            for line in zipped_file:
                count += 1
                if count % 2 == 0:
                    continue
                else:
                    out_file.write(str(line) + '\n')
                    if last_out is None or time.time() > last_out + 2:
                        last_out = time.time()
                        print count