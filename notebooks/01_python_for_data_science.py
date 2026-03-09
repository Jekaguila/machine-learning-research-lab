import pandas as pd
import numpy as np

data = {
    "students":[1,2,3,4],
    "score":[80,90,75,88]
}

df = pd.DataFrame(data)

df.describe()
