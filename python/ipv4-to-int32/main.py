def ip_to_int32(ip):
    bin_num = ''.join([format(int(part), 'b').zfill(8) for part in ip.split('.')])
    return int(bin_num, 2)

assert ip_to_int32("128.114.17.104") == 2154959208, "wrong integer for ip: 128.114.17.104"
assert ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0"
assert ip_to_int32("128.32.10.1") == 2149583361, "wrong integer for ip: 128.32.10.1"
