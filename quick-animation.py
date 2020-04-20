from matplotlib import pylab as plt

# idea: instead of plt.show() I compute the values, call plt.draw() and then plt.pause()
xaxis = plt.arange(0, plt.pi*4, 0.1)

plt.figure("Sin and Cosine Animation")


for i in xaxis:

    series1 = plt.sin(xaxis-i)

    series2 = plt.cos(xaxis-i)
    plt.plot(xaxis, series1, "--", label="Sin")
    plt.plot(xaxis, series2, ":", label="Cos")
    plt.legend()
    plt.draw()
    plt.pause(0.5)
    plt.clf()




