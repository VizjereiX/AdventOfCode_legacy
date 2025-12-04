logger = None

vovels = "aeiou"
bad_strs = ["ab", "cd", "pq", "xy"]

def is_nice(word):
    for s in bad_strs:
        if s in word:
            return False
    
    vovels_count = sum(1 for c in word if c in vovels)
    if vovels_count < 3: return False

    for i in range(0, len(word) -1):
        if word[i] == word[i+1]: return True

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
