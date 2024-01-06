from processor.buffer import Buffer


def buffer_test(txt):
    buffer = Buffer()
    for c in txt:
        res = buffer.write_char(c)
        if res[1]:
            print('processed sentence')
        print(res[0])
