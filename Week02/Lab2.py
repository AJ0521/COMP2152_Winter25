import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("Elements: ", elements)
# git add . && git commit -m "add elements array" && git push

#def funct_name():
#   return True
#def say_greeting(name, message):
 #   print(f" {message}, {name}")
  #  say_greeting("AJ")
   # say_greeting("AJ", "Hello")

def get_valid_int_input(prompt):
    while True:
      try:
        return int(input(print))
      except ValueError:
       print("Error: Please enter a valid integere!")
       continue






try:
    elements_selected = get_valid_int_input("Select an element: ")
#rool dice
    elementRool = random.randint(1,6)
    totalNum =  elements_selected + elementRool

    #print the result based on the totalNum
    if elementRool <= 2:
        print("You rolled a week element, Friend.")
    elif elementRool <= 4:
        print("yor element is Moderate.")
    else:
        print("Nice element. ")
except IndexError:
    print("Error: Invalid element index!")
except Exception as e:
    print(f"An unexpected error occurred: ")


