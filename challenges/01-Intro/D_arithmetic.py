# Here we'll do some basic arithmetic - the basis of (quantitative) computing with data!

# I've defined some variables here for you

one_hand = 20
the_other = 22

# How on earth will you compute the sum?
## add those values together (using only variable names, NOT numbers), and put
## the results in a variable called the_answer

print "The answer is", the_answer

# exponentiation
## You already got +, -, *, and / (and maybe //)
## You can also do exponents with the ** (and NOT the ^) operator
## Can you fix this function with the correct operator?

def exponentiate(base, exponent):
    return base * exponent

print "2 to the 10th power is", exponentiate(2, 10)

# Modulus
## Rounding out our arithmetic, we find another approach to remainders and
## integer division

## Remember how integer arithmetic works?
print "5 / 2 =", 5 / 2

## The modulus operator gives us what's left: %
## To find out what's left, substitute % for / in the following expression

remainder = 5 / 2
print "After 5 / 2,", remainder, "is left"

# Getting a different "right" answer
## And how would we get the division to give us the fractional answer (including
## amounts after the decimal point? (there are at least two "easy" ways)

fractional = 5 / 2
print "In my world of fractions, 5 / 2 is", fractional

