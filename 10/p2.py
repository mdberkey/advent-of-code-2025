
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

with open("input") as f:
    lines = [line.strip() for line in f]
    res = 0

    for l in lines:
        items = l.split()
        buttons = items[1:-1]
        but_nums = []
        target = []

        for num in items[-1][1:-1].split(","):
            target.append(float(num))
        target = np.array(target)

        for but in buttons:
            but_set = set(int(num) for num in but[1:-1].split(","))
            but_nums.append([1. if i in but_set else 0. for i in range(len(target))])

        but_matrix = np.rot90(np.array(but_nums), axes=(1, 0))

        # linear programming solver
        c = np.ones(len(buttons)) 
        constraints = LinearConstraint(but_matrix, target, target)
        bounds = Bounds(lb=0, ub=np.inf)
        integrality = np.ones(len(buttons))
        opt_res = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

        res += int(round(opt_res.fun))

    print(res)
