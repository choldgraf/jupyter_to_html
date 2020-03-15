import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import altair as alt

# %% [markdown]
# ## Generate some data
# First we'll generate some data that we'll use to visualize below.

# %%
np.random.seed(1337)
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['a', 'b', 'c'])

# %% [markdown]
# ## See some outputs
# First we'll look at HTML dataframe output

# %%
df.head()

# %% [markdown]
# Now some simple matplotlib plots

# %%
df.plot.scatter('a', 'b')

# %% [markdown]
# Finally some fancier output
# note that HTML viz output can be tricky to turn into HTML
# I think because getting the JS dependencies loaded is unreliable

# %%
alt.Chart(df).mark_point().encode(
    x="a",
    y="b",
    size="c"
)
