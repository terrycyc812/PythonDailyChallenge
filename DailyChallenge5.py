# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Daily Python Challenge 5
# %% [markdown]
# Create a function that given an n positive integer, it sums all the cubed values from 1 to n. Return the sum.

# %%
def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))


# %%
sum_cubes(5)


