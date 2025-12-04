logger = None

def run(filename):
    map = {(0, 0)}
    i, j = 0, 0
    with open(filename, "r") as f:
        chr = f.read(1)
        while chr:
            if chr =="<": i-=1
            elif chr ==">": i+=1
            elif chr =="v": j-=1
            elif chr =="^": j+=1
            map.add((i, j))
            # print(chr, len(map), (i, j))
            # print(map)

            chr = f.read(1)

    return str(len(map))
