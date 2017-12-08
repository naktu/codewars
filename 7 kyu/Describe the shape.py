# You will be given the number of angles of a shape with equal sides and angles, and you need to return the number of
# its sides, and the measure of the interior angles.
#
# Should the number be equal or less than 2, return:
#
# "this will be a line segment or a dot"
# Otherwise return the result in the following format:
#
# "This shape has s sides and each angle measures d degrees"
# (replace s with number of sides and d with the measure of the interior angles).
#
# Angle measure should be floored to the nearest integer.
#
# Number of sides will be tested from 0 to 180.
#
# Have Fun!


def describe_the_shape(angles):
    if angles < 3:
        return 'this will be a line segment or a dot'
    else:
        return "This shape has {0} sides and each angle measures {1}".format(angles, int((angles - 2)/angles * 180))