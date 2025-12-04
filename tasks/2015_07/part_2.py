logger = None

signals = {}
wire_ops = {}

def binaryOpDecompose(data, op):
    lop, rop = data.split(op)
    if lop.isnumeric():
        lValue = int(lop)
    else:
        lValue = signals.get(lop, None)
        if lValue is None:
            lValue = evaluate(wire_ops[lop])

    if rop.isnumeric():
        rValue = int(rop)
    else:
        rValue = signals.get(rop, None)
        if rValue is None:
            rValue = evaluate(wire_ops[rop])

    return int(lValue), int(rValue)

def evaluate(input):
    if isinstance(input, int)  or input.isnumeric(): return int(input)

    if " AND " in input:
        lValue, rValue =  input.split(" AND ")
        return evaluate(lValue) & evaluate(rValue)
    
    if " OR" in input:
        lValue, rValue =  input.split(" OR ")
        return evaluate(lValue) | evaluate(rValue)
    if "LSHIFT" in input:
        lValue, rValue =  input.split(" LSHIFT ")
        return evaluate(lValue) << evaluate(rValue)
    if "RSHIFT" in input:
        lValue, rValue =  input.split(" RSHIFT ")
        return evaluate(lValue) >> evaluate(rValue)
    if "NOT" in input:
        _, lValue = input.split(" ")
        return  ~evaluate(lValue)
    
    if signals.get(input, None) is not None:
        return evaluate(signals.get(input))
    
    val = evaluate(wire_ops[input])
    signals[input]  = val
    return val


def run(filename):
    target_wire = "a" if "data" in filename else "z"

    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()

            input, output = line.split(" -> ")
            output = output.strip()
            input = input.strip() 

            try:
                for op in [" AND ", " OR ", " LSHIFT ", " RSHIFT ", "NOT"]:
                    if op in input:
                        wire_ops[output] = input
                        break
                else:
                    if input.isnumeric():
                        signals[output] = input
                    else:
                        wire_ops[output] = input

            except ValueError:
                wire_ops[output] = input

    default_signals = signals.copy()

    a = evaluate(target_wire)
    signals.clear()
    signals.update(default_signals)
    signals["b"] = a
    a = evaluate(target_wire)
    return str(a)

   