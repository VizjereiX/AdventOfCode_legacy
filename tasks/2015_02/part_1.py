def run(filename):
    acc = 0
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            sizes = list(int(e) for e in line.split("x"))
            area = sizes[0]*sizes[1]*sizes[2] // max(sizes)

            for i in range(0, 3):
                area += 2 * sizes[i] * sizes[(i+1)%3]
            print(f"{line}\t->\t{area}")
            acc+=area

    return str(acc)