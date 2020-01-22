def generate(x, y):
    res = []
    for yy in range(y):
        yRes = []
        for xx in range(x):
            yRes.append(0)
        res.append(yRes)
    return res

