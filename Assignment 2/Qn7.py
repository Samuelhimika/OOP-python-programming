
year = 2022
default=  'Mark Daniels'
def  paul_details ():
      [ name, birth_year, weight]
name = input('What is your name?........')
birth_year = int(input( 'Enter your birth_year?.......'))

if birth_year ==  2002:
 if not   name:
     name = default 
weight= int(input( 'What is your weight?......'))
print ( 'Your name is.....',name)
print('Born in ', birth_year)
print('With a weight of ...',weight,'kgs')

 
age =( year- birth_year)
print( 'Your age is', age)
  
paul_details() 



