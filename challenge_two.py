def main()

  #user input
  #reverse input as user input flipped
  #input check

  
  print("Palindrome Detector")

  userInput = ("Please enter a value to be checked: ") 
  reverseInput = userInput[::-1]
  if reverseInput == userInput:
      print("Results: " + userInput + " is a palindrome")
    else
      print("Results: " + userInput + " is not a palindrome")
