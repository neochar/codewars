def nexus(users):
    umin = None
    vmin = None

    for i in sorted(users):
        v = abs(i - users[i])
        if vmin is None or vmin > v:
            vmin = v
            umin = i

    return umin
