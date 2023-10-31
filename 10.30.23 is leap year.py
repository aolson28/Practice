def is_leap_year(year):     
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# P bool
# R bool whether it is a leap year
# E 2000 = true, 1900 = false, 2020 = true, 2023 = false
# P leap year is every 4 years but not on years divisible by 100 unless it is divisible by 400