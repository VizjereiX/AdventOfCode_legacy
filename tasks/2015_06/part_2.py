logger = None

def run(filename):
    light_map = []
    for i in range(0, 1000):
        light_map.append([])
        for j in range(0, 1000):
            light_map[i].append(0)

    def toggle(i, j):
        light_map[i][j] += 2

    def turn_on(i, j):
        light_map[i][j] += 1
        
    def turn_off(i, j):
        light_map[i][j] = max(0, light_map[i][j]-1)

    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()

            fn_to_call = None
            if "off " in line:
                fn_to_call = turn_off
                coords = line[9::]
            elif "on " in line:
                fn_to_call = turn_on
                coords = line[8::]
            else:
                fn_to_call = toggle
                coords = line[7::]
            start, stop = coords.split(" through ")
            start_x, start_y = start.split(",")
            stop_x,  stop_y  =  stop.split(",")

            for x in range(int(start_x), int(stop_x) + 1):
                for y in range(int(start_y), int(stop_y) + 1):
                    fn_to_call(x, y)

    acc = 0
    for i in range(0, 1000):
        acc += sum(light_map[i])

    return str(acc)

