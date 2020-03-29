# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0..255 (included).
#
# Input to the function is guaranteed to be a single string.
#
# Examples
# // valid inputs:
# 1.2.3.4
# 123.45.67.89
#
# // invalid inputs:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!


def is_valid_IP(strng):
    ip = strng.split('.')
    if len(ip) != 4:
        return False
    for i in ip:
        try:
            oct = int(i)
        except:
            return False
        if (str(oct) != i) or not (oct >= 0 and oct < 256):
            return False
    return True