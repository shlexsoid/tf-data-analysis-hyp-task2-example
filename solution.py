import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 399623382 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    res = anderson_ksamp([x,y])
    return res.pvalue < 0.07

