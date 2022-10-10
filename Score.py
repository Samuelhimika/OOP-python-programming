


while True:
      Score =( input('Enter the score......'))

      if  (Score  >= '0.9' and Score <="1.0"):

       print ('A' ) 
      elif   (Score   >=  '0.8' and Score < '0.9'):
       print(  ' B ')
 


 

      elif   (Score   >=  '0.7' and Score < '0.8'):

           print('C')

      elif  (Score   >=  '0.6' and Score <= '0.7'):
       print('D')

      elif   (Score  <'0.6' and Score > '0.0'):

        print('F')
      elif  Score =="stop":
            break

      else:
          print('Bad Score')
          