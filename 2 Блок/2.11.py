bits = int(input(""))
bytes = bits / 8
kilobytes = bytes // 1024
megabytes = kilobytes // 1024
gigabytes = megabytes // 1024
terabytes = gigabytes // 1024
print(terabytes, 'Tb,', gigabytes, 'Gb,', megabytes, 'Mb,', kilobytes, 'Kb,', bytes, 'bytes,', bits-bytes*8, 'bits')