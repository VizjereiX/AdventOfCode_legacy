logger = None

vovels = "aeiou"
bad_strs = ["ab", "cd", "pq", "xy"]

def is_nice(word):
    for i in range(0, len(word) -2):
        if word[i] == word[i+2]: break
    else:
        return False
    
    for i in range(0, len(word)-3):
        for j in range(i+2, len(word)-1):
            if word[i] == word[j] and word[i+1] == word[j+1]: return True
    
    return False

def run(filename):
    acc = 0
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            if is_nice(line):
                acc+=1

    return str(acc)
