def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    year=2024-age
    print(f"Hello {name}, you were born in {year}")

def my_country(country = "Uganda"):
    print(f"Hello Akirachix from {country}")
    
def greet(*names):
    for name in names:
        print(f"Hello {name}")


def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence+=word
        sentence+= " "
    return sentence


def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=x
    f=kwargs["first_name"]
    l=kwargs["last_name"]
    greeting = f"Hello {f} {l}, total of your numbers is {total}"
    return greeting


