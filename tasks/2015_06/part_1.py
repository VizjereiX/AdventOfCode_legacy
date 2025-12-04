logger = None

def run(filename):
    light_map= set()

    def toggle(i, j):
        if (i, j) in light_map:
            turn_off(i, j)
        else:
            turn_on(i, j)
        pass
    def turn_on(i, j):
        light_map.add((i, j))
        
    def turn_off(i, j):
        try:
            light_map.remove((i, j))
        except Exception:
            pass

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

    return str(len(light_map))

