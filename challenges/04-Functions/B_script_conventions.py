# A funny, but common thing you'll see in python scipts is that if __name__ ...
# block below

# To start off, just run this script and see what happens.

# Then run the test and note that it fails in a curious way!

print "I was run - maybe by a test?"

if __name__ == '__main__':

    # The problem is that this variable needs to be defined OUTSIDE the if
    # __name__ block. Can you move it above where it will be picked up by the
    # test?

    # Don't forget to fix the indentation!
    module_var = "I am totally defined"
    print "I'm being run directly"
    print "And module_var is:", module_var
