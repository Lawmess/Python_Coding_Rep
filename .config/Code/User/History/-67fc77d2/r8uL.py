print('Welcome to my simple body analysis!')

gender = input('Enter your gender (men/women): ')

men_r = 0.73
women_r = 0.66

weight = float(input('Enter your weight: '))

number_of_drinks = float(input('Enter the number of drinks you have had: '))

number_of_alcohol_per_drink_consumed = float(input('Alcohol consumed per drink (in ounces): '))

hours_since_the_last_drink = int(input('Hours since the last drink: '))

if gender.lower() == 'men':
    Blood_Alcohol_Content = (number_of_alcohol_per_drink_consumed * number_of_drinks * 5.14 / weight * men_r) - (0.015 * hours_since_the_last_drink)
else:
    Blood_Alcohol_Content = (number_of_alcohol_per_drink_consumed * number_of_drinks * 5.14 / weight * women_r) - (0.015 * hours_since_the_last_drink)

print(f'Your estimated Blood Alcohol Content (BAC) is: {Blood_Alcohol_Content:.4f}')