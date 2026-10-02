running_total = 0

num_of_friends = 4

appetizers = 35.99
main_courses = 60.48
desserts = 42.12
drinks = 64.25

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.15
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill , 2)
print('Each person pays:', each_pays)