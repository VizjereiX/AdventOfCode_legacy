def run(filename):
    acc = 0
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            sizes = list(int(e) for e in line.split("x"))
            volume = sizes[0]*sizes[1]*sizes[2]
            len = 2 * (sizes[0]+sizes[1]+sizes[2]-max(sizes))
            acc+=len + volume

    return str(acc)