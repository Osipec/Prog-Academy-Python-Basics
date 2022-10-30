#Lesson 3, Homework 4, Osypenko Kostiantyn

# 1. Find out the porch, floor and number by the flat number
flat = int(input('Enter the flat number\t'))
flats_on_floor, floors, porches = 4, 9, 4

porch = (flat - 1) // (flats_on_floor * floors) + 1
floor = ((flat - 1) % (flats_on_floor * floors)) // flats_on_floor + 1
flat_num = (flat - 1) % flats_on_floor + 1
answer = f'Porch number is {porch}, Floor number is {floor}, Flat on floor number is {flat_num}'
print(1 <= flat <= 144 and answer or 'No such flat number')

# 2. Check out if the yer is the year is leap
year = int(input('Enter a year to check if it\'s leap or not\t'))
if not year % 400 or year % 100 and not year % 4:
    print(366)
else:
    print(365)

# 3. Check the triangle
a, b, c = int(input('Side A ')), int(input('Side B ')), int(input('Side C '))
if a + b > c and a + c > b and b + c > a:
    print('The triangle can exist')
else:
    print('The triangle can not exist')