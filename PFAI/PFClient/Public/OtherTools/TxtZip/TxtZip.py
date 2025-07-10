import zlib
import gzip

f_in = open('StrFilter.txt', 'rb')
str_in = f_in.read()
print(str_in)
f_out = gzip.open('StrFilter.txt.gz', 'wb')
f_out.write(str_in)
f_out.close()
f_in.close()

