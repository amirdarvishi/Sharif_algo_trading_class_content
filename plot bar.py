import matplotlib.pyplot as plt 

# define series
labels = ['A', 'B', 'C']
values = [10,14,9]

# plot
bars = plt.bar(labels,values)

# set hatch for adding style to bars
bars[1].set_hatch('/')
bars[0].set_hatch('*')

plt.show()
