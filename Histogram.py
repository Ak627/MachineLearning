from matplotlib import pyplot
import numpy

#randint() will generate 20 numbers from 1-99, store output in list named "numList"
numList = numpy.random.randint(200, size = 50)

#print to console for testing
print("the list of numbers we generated is:", numList)

#this creates a graphical window of size x inches by y inches
screen = pyplot.figure(figsize = (12,8))

#1)set up a histogram, let pyplot use default bins
#pyplot.hist(numList)
#2)set up a histogram, set number of bins:
#pyplot.hist(numList, 10)
#3) set up a histogram, set edges of bins:
pyplot.hist(numList, bins = [0,20,40,60,80, 100, 120, 130, 140, 160, 180,200])

#set title
pyplot.title("Professionally professional histogram")

#show plot

pyplot.show()
