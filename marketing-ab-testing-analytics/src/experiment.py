import numpy as np
from math import sqrt

def two_proportion_ztest(control_success, control_total, treatment_success, treatment_total):
    p1 = control_success / control_total
    p2 = treatment_success / treatment_total
    pooled = (control_success + treatment_success) / (control_total + treatment_total)
    se = sqrt(pooled * (1-pooled) * (1/control_total + 1/treatment_total))
    z = (p2-p1) / se
    return {'control_rate': p1, 'treatment_rate': p2, 'uplift': (p2/p1)-1, 'z_score': z}

if __name__ == '__main__':
    print(two_proportion_ztest(1200, 10000, 1380, 10000))
