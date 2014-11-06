########Python Syntax
monty = True
python = 1.234
monty_python = python**2

#######Tip Calculator
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax

total = meal + meal *tip
print("%.2f" % total)


######Date and Time
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)



##########Strings & Console Output
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)



###########Conditionals & Control Flow
def the_flying_circus():
    if (2 <= 2) or (5 <= 2):    
        return True
    elif (5 <= 2) and (2 <= 2):
        return False
        
###########PygLatin
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    new_word[1:]
    print original
else:
    print 'empty'
    
    
    
###########Functions
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
        
        