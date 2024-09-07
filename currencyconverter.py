#Store conversation rates for different currencies in dictionary
convertCurrencies = {
  "euro": 1.17, #Rate for Euro
  "usd": 1.27, #Rate for US Dollar
  "aud": 1.95, #Rate for Australian Dollar
  "cad": 1.73, #Rate for Canadaina Dollar
  "cny": 9.02, #Rate for Chinese Yuan
  "npr": 168.49, #Rate for Nepalese Rupee
  "jpy": 192.38 #Rate for Japanese Yen
}

#It will keep the program running until user press 5
while True:
  #Ask the user for the amount in GBP
  yourCurrency = float(input("Enter your amount(GBP): £"))
  #Show the available currency options for conversion
  print("EURO : Euro")
  print("USD : United States Dollar")
  print("AUD : Australian Dollar")
  print("CAD : Canadian Dollar")
  print("CNY : Chinese Yuan")
  print("NPR : Nepalese Rupee")
  print("JPY : Japanese Yen")
  print("Press 5 to stop")
#Ask the user to choose a currency to convert
  foreignCurrency = input("Choose the currency: ")
#Check if the user wants to exit
  if foreignCurrency == "5":
      print("Goodbye!")
      break
#Check if the chosen currency is supported
  if foreignCurrency in convertCurrencies:
    #Display the exchange rate and the converted amount
      print(f"GBP/{foreignCurrency.upper()} = {convertCurrencies[foreignCurrency]}")
      print(yourCurrency * convertCurrencies[foreignCurrency])
  else: 
    #Notify the user if the chosen currency isnt supported
      print("Currency not supported")
