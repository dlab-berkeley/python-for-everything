# Sometimes you want to avoid side effects (like print statements), you just
# want to get the values computed by a function and have complete control. In
# this case, we can move our print statements to one of those if __name__ ...
# blocks

# That's a nice way to have a quick way to run your script and see that it does
# something sensible, but allow those functions to be used by others

def exponentiate(x, y):
    return x ** y

print '2 ** 3 =', exponentiate(2,3)

if __name__ == '__main__':
    pass # This is python's "placeholder" do-nothing statement
         # What happens if you delete this without a replacement?
