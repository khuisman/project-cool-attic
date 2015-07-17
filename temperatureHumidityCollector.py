import HTU21DF


def getTempAndHumidity():
  medianTemp = getMedianTemperature()
  temp_fahrenheit = celcius_to_fahrenheit(medianTemp)
  humidity = getHumidity(medianTemp)

  return(temp_fahrenheit, humidity, medianTemp)


def celcius_to_fahrenheit(celcius):
  return (celcius * 1.8) + 32


def median(x):
  m,r= divmod(len(x),2)
  if r:
    return sorted(x)[m]
  return sum(sorted(x)[m-1:m+1])/2

def getTemperature():
  HTU21DF.htu_reset()
  return HTU21DF.read_temperature()

def getMedianTemperature():
  tempList = []
  for x in range(100):
     tempList.append(
       getTemperature()
     )
  return median(tempList)

def getHumidity(temperature):
  tempList = []
  for x in range(100):
     HTU21DF.htu_reset
     tempList.append(HTU21DF.read_humidity(temperature))
  return median(tempList)

if __name__ == '__main__':
  main()
