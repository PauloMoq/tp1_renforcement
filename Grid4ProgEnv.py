states = ["s" + str(i) for i in range(4)]
actions = ["right", "down", "left", "up"]

def transitions(state, action):
    def get_next(s, a):
        if s == "s0" and a == "down": return "s1"
        if s == "s1" and a == "up":   return "s0"
        if s == "s1" and a == "right": return "s2"
        if s == "s2" and a == "left":  return "s1"
        if s == "s2" and a == "up":    return "s3"
        return s

    perpendiculaires = {
        "right": ["up", "down"],
        "left": ["up", "down"],
        "up": ["left", "right"],
        "down": ["left", "right"],
    }

    result = {}

    s_main = get_next(state, action)
    result[s_main] = result.get(s_main, 0) + 0.8

    for perp in perpendiculaires[action]:
        s_perp = get_next(state, perp)
        result[s_perp] = result.get(s_perp, 0) + 0.1

    return result

def rewards(state, action):
    if state == "s2" and action == "up":
        return 10
    elif state == "s3":
        return 0
    else:
        return -1

def isTerminal(state):
    return state == "s3"