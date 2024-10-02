grade_percentage = float(input("What is your grade percentage: "))
                    
if grade_percentage >= 90:
  print (str('Your grade lette is: A'))
elif grade_percentage >= 80:
  print (str('Your grade letter is: B'))
elif grade_percentage >= 70:
  print (str('Your grade letter is: C'))
elif grade_percentage >= 60:
  print (str('You grade letter is: D'))
elif grade_percentage < 60:
  print (str('You grade letter is: F'))

if grade_percentage in range (70, 100):
  print (str('Exceltent! You pass the class.'))
else:
  print ('You did not pass the class, Keep trying...')