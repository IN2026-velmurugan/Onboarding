"""Script to demonstrate the use of poetry."""

import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore

df = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])  # type: ignore
print(df.head())

df.plot(kind="scatter", x="a", y="b")
plt.show()
