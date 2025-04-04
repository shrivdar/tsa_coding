def main():

  print("In order to convert the provided temperature please input the temperature and first initial of the scale (F- Fahrenheit, C - Celsius, K - Kelvin)")
  int K;
  int C;
  int F;
  String unit;
  int converted_temperature;

  
  try
  def kelvinToCelsius(temperature):
    K = temperature + 273.15
  def celciusToKelvin(temperature):
    C = temperature - 273.15
  def kelvinToFahrenheit(temperature):
    F = (temperature-273.15)(9/5) + 32
  def FahrenheitToKelvin(temperature):
    K = (temperature-32)(5/9) + 273.15
  def FahrenheitToCelsius(temperature):
    C = (temperature-32)(5/9)
  def CelciusToFahrenheit(temperature):
    F = temperature*(9/5) + 32
    

  
  print("In order to convert the provided temperature please input the temperature and first initial of the scale (F- Fahrenheit, C - Celsius, K - Kelvin)")
  degree = input("Please enter temperature and scale: ")
  scale = degree[-1]
  temperature = int(degree[:-1])
  print("Conversion Options: #1. Convert to Celsius #2. Convert to Fahrenheit #3. Convert to Kelvin")
  statement = input("Please select the scale you wish to convert your temperature to: ")
  
  if degree == "C":
    print(
      elif statement == "1":
        print("Temperature is already in the desired scale")
        
      elif statement == "2":
        CelciusToFahrenheit(temperature)

      elif statement == "3":
        celciusToKelvin(
          
    if degree == "F":
    print(
      elif statement == "1":
        FahrenheitToCelsius(
        
      elif statement == "2":
        print("Temperature is already in the desired scale")

      elif statement == "3":
        FahrenheitToKelvin(

    if degree == "C":
    print(
      elif statement == "1":
        kelvinToCelsius(
        
      elif statement == "2":
        kelvinToFahrenheit(

      elif statement == "3":
        print("Temperature is already in the desired scale")
  print("Converted Temperature: [converted_temperature]")


  
