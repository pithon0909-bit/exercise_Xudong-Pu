#for n in range(10, 1314):  # 1314 so that 1313 is included
if n % 13 == 0 and n % 5 == 0:
        print(n)
        
65
130
195
260
325
390
455
520
585
650
715
780
845
910
975
1040
1105
1170
1235
1300

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

str_repeat = "ACGT" * 3 + "TTATT" * 5
print("Short tandem repeat:")
print(str_repeat)

print("\nAll suffixes:")
for i in range(len(str_repeat), -1, -1):
    print(str_repeat[i:])

print("\nAll substrings of length 3:")
for i in range(len(str_repeat) - 3 + 1):
    print(str_repeat[i:i+3])

print("\nUnique substrings of length 3:")
seen = set()
for i in range(len(str_repeat) - 3 + 1):
    sub = str_repeat[i:i+3]
    if sub not in seen:
        print(sub)
        seen.add(sub)
        
Short tandem repeat:
ACGTACGTACGTTTATTTTATTTTATTTTATTTTATT

All suffixes:

T
TT
ATT
TATT
TTATT
TTTATT
TTTTATT
ATTTTATT
TATTTTATT
TTATTTTATT
TTTATTTTATT
TTTTATTTTATT
ATTTTATTTTATT
TATTTTATTTTATT
TTATTTTATTTTATT
TTTATTTTATTTTATT
TTTTATTTTATTTTATT
ATTTTATTTTATTTTATT
TATTTTATTTTATTTTATT
TTATTTTATTTTATTTTATT
TTTATTTTATTTTATTTTATT
TTTTATTTTATTTTATTTTATT
ATTTTATTTTATTTTATTTTATT
TATTTTATTTTATTTTATTTTATT
TTATTTTATTTTATTTTATTTTATT
TTTATTTTATTTTATTTTATTTTATT
GTTTATTTTATTTTATTTTATTTTATT
CGTTTATTTTATTTTATTTTATTTTATT
ACGTTTATTTTATTTTATTTTATTTTATT
TACGTTTATTTTATTTTATTTTATTTTATT
GTACGTTTATTTTATTTTATTTTATTTTATT
CGTACGTTTATTTTATTTTATTTTATTTTATT
ACGTACGTTTATTTTATTTTATTTTATTTTATT
TACGTACGTTTATTTTATTTTATTTTATTTTATT
GTACGTACGTTTATTTTATTTTATTTTATTTTATT
CGTACGTACGTTTATTTTATTTTATTTTATTTTATT
ACGTACGTACGTTTATTTTATTTTATTTTATTTTATT

All substrings of length 3:
ACG
CGT
GTA
TAC
ACG
CGT
GTA
TAC
ACG
CGT
GTT
TTT
TTA
TAT
ATT
TTT
TTT
TTA
TAT
ATT
TTT
TTT
TTA
TAT
ATT
TTT
TTT
TTA
TAT
ATT
TTT
TTT
TTA
TAT
ATT

Unique substrings of length 3:
ACG
CGT
GTA
TAC
GTT
TTT
TTA
TAT
ATT

balance = float(input("Enter initial balance: "))

while True:
    user_input = input("Enter expense/revenue (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting program.")
        break

    try:
        transaction = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")
        continue

    if balance + transaction < 0:
        print("Operation not permitted: insufficient funds.")
    else:
        balance += transaction
        print(f"New balance: {balance:.2f}")
        
Enter initial balance: 1000
Enter expense/revenue (or 'exit' to quit): -300
New balance: 700.00
Enter expense/revenue (or 'exit' to quit): 600
New balance: 1300.00
Enter expense/revenue (or 'exit' to quit): -800
New balance: 500.00
Enter expense/revenue (or 'exit' to quit): 200
New balance: 700.00
Enter expense/revenue (or 'exit' to quit): -800
Operation not permitted: insufficient funds.
Enter expense/revenue (or 'exit' to quit): exit
Exiting program.

squares = {}

x = 1
while x**2 < 100:
    squares[x**2] = x
    x += 1

for square, num in squares.items():
    print(f"{square} is the square of {num}")
    
1 is the square of 1
4 is the square of 2
9 is the square of 3
16 is the square of 4
25 is the square of 5
36 is the square of 6
49 is the square of 7
64 is the square of 8
81 is the square of 9

countries = {
    'The Netherlands': {
        'capital': 'Amsterdam',
        'population': 17283008,
        'continent': 'Europe',
    },
    'France': {
        'capital': 'Paris',
        'population': 67186638,
        'continent': 'Europe',
    },
    'USA': {
        'capital': 'Washington, D.C.',
        'population': 327167434,
        'continent': 'North America',
    }
}

while True:
    country_name = input("Enter country name (or 'exit' to finish): ")
    if country_name.lower() == "exit":
        break

    capital = input(f"Enter the capital of {country_name}: ")

    while True:
        try:
            population = int(input(f"Enter the population of {country_name}: "))
            break
        except ValueError:
            print("Population must be an integer. Please try again.")

    continent = input(f"Enter the continent of {country_name}: ")

    countries[country_name] = {
        'capital': capital,
        'population': population,
        'continent': continent
    }
    
Enter country name (or 'exit' to finish): Italy
Enter the capital of Italy: Rome
Enter the population of Italy: 45000000
Enter the continent of Italy: Europe
Enter country name (or 'exit' to finish): China
Enter the capital of China: Beijing
Enter the population of China: 1400000000
Enter the continent of China: Asia
Enter country name (or 'exit' to finish): exit

max_country = max(countries.items(), key=lambda item: item[1]['population'])
name, info = max_country
print(f"\n{name} has the largest population, of {info['population']} people.")

China has the largest population, of 1400000000 people.

query_continent = input("\nEnter a continent to count countries from: ")
count = sum(1 for info in countries.values() if info['continent'].lower() == query_continent.lower())
print(f"There are {count} countries from {query_continent}.")

Enter a continent to count countries from: Europe
There are 3 countries from Europe.
