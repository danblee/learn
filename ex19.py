# this is our function we'll be working with
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket. \n"

# this feeds the function the variables it needs directly    
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this offers up variables for the parameters and calls the function
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This will feed the same variables directly but with math first
print "We can even do math inside, too!"
cheese_and_crackers(10 + 20, 5 + 6)

# This will use the variables on lines 14 and 15 to do math then give it to the function
print "And we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)