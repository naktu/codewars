# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
# items. We want to create the text that should be displayed next to such an item.
#
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who
# like an item. It must return the display text as shown in the examples:
#
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


def likes(names):
    likes = ' likes this'
    like = ' like this'
    if len(names)<1:
        return 'no one' + likes
    elif len(names)<2:
        return names[0] + likes
    elif len(names)<3:
        return '{0} and {1}{2}'.format(names[0], names[1], like)
    elif len(names)<4:
        return '{0}, {1} and {2}{3}'.format(names[0], names[1], names[2], like)
    else:
        return '{0}, {1} and {2} others{3}'.format(names[0], names[1], len(names[2:]), like)
    