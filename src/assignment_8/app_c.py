"""Script to demonstrate the use of poetry."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])  # type : ignore
print(df.head())

df.plot(kind="scatter", x="a", y="b")
plt.show()
