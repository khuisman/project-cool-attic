import time
import HTU21DF



def median(x):
  m,r= divmod(len(x),2)
  if r:
    return sorted(x)[m]
  return sum(sorted(x)[m-1:m+1])/2

def average(x):
  return sum(x)/len(x)


tempList = []
for x in range(1000):
   HTU21DF.htu_reset
   tempList.append(HTU21DF.read_temperature())


print 'median is {0}'.format(median(tempList))
print 'average is {0}'.format(average(tempList))
print 'minimum value is {0}, maximum value is {1}'.format(min(tempList), max(tempList))
print 'difference is {0}'.format(max(tempList) - min(tempList))