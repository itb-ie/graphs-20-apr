from matplotlib import pylab as plt
# we can replace range with arange - matplotlib
# xseries = list(range(0, 30))
# arange allows us to set the step as a floating point value
xseries = plt.arange(0, 30, 0.1)
print(xseries)

series1 = []
series2 = []
series3 = plt.sin(xseries)
maxvalues_xaxis = plt.arange(plt.pi/2, 30, plt.pi)
maxvalues_yaxis = plt.sin(maxvalues_xaxis)

for i in xseries:
    series1.append(i)
    series2.append(i/2)

# create individual sub figures with subplot (number means: xyz - x row, y col, z - position
plt.subplot(211)
plt.plot(xseries, series1, label="Faster Linear Progression")
plt.plot(xseries, series2, "y:", label="Slower Linear Progression")
plt.legend()

# plot the sinus
plt.subplot(212)
# let us change colors, third paramter is the style(color(r,g,b,c,m,y, k-black), line style, marker)
plt.plot(xseries, series3, "k--", label="Sin function")
plt.plot(maxvalues_xaxis, maxvalues_yaxis, "r^", label="Extreme Values of Sin")
# we use plt.text() to put a text inside the graph
for i in range(len(maxvalues_xaxis)):
    plt.text(maxvalues_xaxis[i], maxvalues_yaxis[i], str(maxvalues_yaxis[i]))
plt.ylim(-2, 4)
plt.legend(loc="upper left")

#always do plt.show
plt.show()
