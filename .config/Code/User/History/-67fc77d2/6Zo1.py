print('Welcome to my simple body analysis!')


gender=input('Enter your gender:')

men_r=0.73

women_r=0.66


weight= float(input('Enter your weight:'))

number_of_drinks=input('Enter the number of drinks you can have: ')

number_of_alcohol_per_drink_consumed=input('Alcohol consumed:')

Hours_since_the_last_drink=int(input('Number of times since last drink: '))

if gender==men:
    Blood_Alcohol_Content= (number_of_alcohol_per_drink_consumed * 5.14 / weight * men_r)

else:
    Blood_Alcohol_Content= (number_of_alcohol_per_drink_consumed *5.14 /weight * women_r)

print(Blood_Alcohol_Content)



