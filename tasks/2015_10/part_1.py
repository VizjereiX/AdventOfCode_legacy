logger = None

def run(filename):
    with open(filename, "r") as f:
        data, rpt = f.read().splitlines()
        data = data.strip()
        rpt = int(rpt.strip())

    data = data + "X"  # sentinel
    for i in range(rpt):
        new_data = ""
        j = 0
        num = None
        count = 0
        while j < len(data):
            if num is None:
                num = data[j]
                count = 1
                j+=1
                continue
            if data[j] == num:
                count += 1
                j+=1
                continue
            new_data += str(count)
            new_data += str(num)
            num = None    
            
        data = new_data + "X"  # sentinel

    return len(data)-1  # remove sentinel  
