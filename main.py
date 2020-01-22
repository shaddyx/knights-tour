import gen
import moves

XM, YM = 8, 8

class DepthCounter:
    depth = 0
    maxDepth = 0
    oldMaxDepth = 0
field = gen.generate(XM, YM)

def formatField():
    res = []
    for y in range(YM):
        res.append(" ".join(map(lambda x: str(x).ljust(2, " "), field[y])))
    return "\n".join(res)

def check(x, y):
    return field[y][x]

def goto(x, y):
    if field[y][x]:
        raise RuntimeError("Already moved to {}, {} \n {}".format(x, y, formatField()))
    field[y][x] = DepthCounter.depth + 1
    DepthCounter.depth += 1
    DepthCounter.maxDepth = max(DepthCounter.maxDepth, DepthCounter.depth)
    if DepthCounter.maxDepth != DepthCounter.oldMaxDepth:
        DepthCounter.oldMaxDepth = DepthCounter.maxDepth
        print(DepthCounter.maxDepth)
        print(formatField())

def rm(x, y):
    if not field[y][x]:
        raise RuntimeError("Already removed to {}, {} \n {}".format(x, y, formatField()))
    field[y][x] = 0
    DepthCounter.depth -= 1

def checkMove(x, y):
    return x >= 0 and y >= 0 and x < XM and y < YM and not check(x, y)

def move(x, y):
    goto(x, y)
    for nextMoveI in range(len(moves.MOVES)):
        hypX, hypY = moves.nextMove(x, y, nextMoveI)
        if checkMove(hypX, hypY):
            move(hypX, hypY)
    rm(x, y)

for xx in range(XM):
    for yy in range(YM):
        print(xx, yy)
        move(xx, yy)


