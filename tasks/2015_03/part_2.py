logger = None

def run(filename):
    map = {(0, 0)}
    i=[0, 0]
    j=[0, 0]
    santaType = 0
    with open(filename, "r") as f:
        chr = f.read(1)
        while chr:
            if chr =="<": i[santaType]-=1
            elif chr ==">": i[santaType]+=1
            elif chr =="v": j[santaType]-=1
            elif chr =="^": j[santaType]+=1
            map.add((i[santaType], j[santaType]))
            # print(chr, len(map), (i, j))
            # print(map)
            santaType = (santaType + 1)%2
            chr = f.read(1)

    return str(len(map))
