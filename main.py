# Pandas: GroupBy columns with NaN (missing) values

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ID': [1, 1, 1, 2, 2, 2],
    'Animal': ['Cat', 'Cat', np.nan, 'Dog', 'Dog', np.nan],
    'Max Speed': [25, 35, 45, 55, 65, 75]
})

# 👇️ without NA values
print(df.groupby(['Animal']).mean())

print('-' * 50)

# 👇️ with NA values
print(df.groupby(['Animal'], dropna=False).mean())