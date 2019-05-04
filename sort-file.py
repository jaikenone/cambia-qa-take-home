print('start sort-file...')

with open('./input.csv', 'r') as ifp:
    with open('./output.csv', 'w') as ofp:
        for line in ifp:
            line = line.rstrip('\r\n')
            print(line)
            l = line.split(',')
            l.sort(reverse=True)
            ofp.writelines(','.join(l))
            print(','.join(l))

print('done.')