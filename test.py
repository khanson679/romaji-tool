import romkan_src as rk

while True:
    x = raw_input('1> ')
    y = raw_input('2> ')
    if x == '' or y == '': break
    print rk._kanpat_cmp(x.decode("utf8"),y.decode("utf8"))