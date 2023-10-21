import re
def validate_pin(pin):
    pattern = re.match("^\\d{4}$", pin)
    pattern2 = re.match("^\\d{6}$", pin)
    return (bool(pattern) or bool(pattern2)) and (len(pin) == 4 or len(pin) == 6)

# P bool
# R bool if the string is 4 or 6 digits number digits
# E '1234.5' -> false, '123987' -> true
# P use re module, can use match(), simpler would be fullmatch() like bool(re.fullmatch("\d{4}|\d{6}", pin))