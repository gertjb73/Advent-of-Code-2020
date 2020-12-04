# Advent of Code
# Day 04-01 - Passport Processing
#
# https://adventofcode.com/2020/day/4#part2
#
# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole
# Credentials instead of your passport. While these documents are extremely
# similar, North Pole Credentials aren't issued by a country and therefore
# aren't actually valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long
# line has formed for the automatic passport scanners, and the delay could
# upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to
# solve both of these problems at the same time.
#
# The automatic passport scanners are slow because they're having trouble
# detecting which passports have all required fields. The expected fields are
# as follows:
#
# - byr (Birth Year)
# - iyr (Issue Year)
# - eyr (Expiration Year)
# - hgt (Height)
# - hcl (Hair Color)
# - ecl (Eye Color)
# - pid (Passport ID)
# - cid (Country ID)
#
# Passport data is validated in batch files (your puzzle input). Each
# passport is represented as a sequence of key:value pairs separated by
# spaces or newlines. Passports are separated by blank lines.
#
# Here is an example batch file containing four passports:
#
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
#
# The first passport is valid - all eight fields are present. The second
# passport is invalid - it is missing hgt (the Height field).
#
# The third passport is interesting; the only missing field is cid, so it
# looks like data from North Pole Credentials, not a passport at all! Surely,
# nobody would mind if you made the system temporarily ignore missing cid
# fields. Treat this "passport" as valid.
#
# The fourth passport is missing two fields, cid and byr. Missing cid is
# fine, but missing any other field is not, so this passport is invalid.
#
# According to the above rules, your improved system would report 2 valid
# passports.
#
# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?
#
# Your puzzle answer was 222.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# The line is moving more quickly now, but you overhear airport security
# talking about how passports with invalid data are getting through. Better
# add some data validation, quick!
#
# You can continue to ignore the cid field, but each other field has strict
# rules about what values are valid for automatic validation:
#
# - byr (Birth Year) - four digits; at least 1920 and at most 2002.
# - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# - hgt (Height) - a number followed by either cm or in:
#   - If cm, the number must be at least 150 and at most 193.
#   - If in, the number must be at least 59 and at most 76.
# - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# - pid (Passport ID) - a nine-digit number, including leading zeroes.
# - cid (Country ID) - ignored, missing or not.
#
# Your job is to count the passports where all required fields are both
# present and valid according to the above rules. Here are some example
# values:
#
# byr valid:   2002
# byr invalid: 2003
#
# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190
#
# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc
#
# ecl valid:   brn
# ecl invalid: wat
#
# pid valid:   000000001
# pid invalid: 0123456789
#
# Here are some invalid passports:
#
# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
#
# Here are some valid passports:
#
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
#
# Count the number of valid passports - those that have all required fields
# and valid values. Continue to treat cid as optional. In your batch file,
# how many passports are valid?

def read_passport_file(name_of_passport_file):
    passport_file = open(name_of_passport_file, "r")
    passport_data = passport_file.read().splitlines()
    passport_file.close()
    return passport_data


def put_passports_together(passport_data):
    one_passport = ""
    processed_passports = []
    for passport_line in passport_data:
        # As long as you haven't found an empty line add lines together
        # Empty lines marks a new passport
        if passport_line != "":
            one_passport = one_passport + passport_line + " "
        # You have found an empty line, so on the next line it will be a new passport
        else:
            processed_passports.append(one_passport.rstrip())
            one_passport = ""
    # And don't forget to process the last passport
    processed_passports.append(one_passport)
    return processed_passports


def check_validity_of_passport(passport):
    # Expected fields
    expected_fields = {
        "byr": False,  # Birth Year
        "iyr": False,  # Issue Year
        "eyr": False,  # Expiration Year
        "hgt": False,  # Height
        "hcl": False,  # Hair Color
        "ecl": False,  # Eye Color
        "pid": False,  # Passport ID
        "cid": False   # Country ID
    }
    passport_list = [passport]
    for passport_element in passport_list:
        element_split = passport_element.split()
        for list_item in element_split:
            key, value = list_item.split(':')
            expected_fields[key] = switch_on_passport_key(key, value)
    # Check all field from passport
    passport_still_valid = True
    for key, value in expected_fields.items():
        if not value and key != 'cid':
            passport_still_valid = False
    return passport_still_valid


def check_birth_year(value):
    byr_valid = True if 1920 <= int(value) <= 2002 else False
    # print("BYR Value", value, byr_valid)
    return byr_valid


def check_issue_year(value):
    iyr_valid = True if 2010 <= int(value) <= 2020 else False
    # print("IYR Value", value, iyr_valid)
    return iyr_valid


def check_expiration_year(value):
    eyr_valid = True if 2020 <= int(value) <= 2030 else False
    # print("EYR Value", value, eyr_valid)
    return eyr_valid


def check_height(value):
    # Check to see if the value is in 'cm' or in 'in'.
    # If height doesn't contain this, then it's invalid anyway
    hgt_indicator = value.find("cm")
    if hgt_indicator > 0:
        height = int(value[:hgt_indicator])
        hgt_valid = True if 150 <= height <= 193 else False
        return hgt_valid

    hgt_indicator = value.find("in")
    if hgt_indicator > 0:
        height = int(value[:hgt_indicator])
        hgt_valid = True if 59 <= height <= 76 else False
        return hgt_valid

    if hgt_indicator < 0:  # No 'cm' or 'in' found
        height = 0
        hgt_valid = False
        return hgt_valid


def check_hair_color(value):
    print("HCL Value", value)


def check_eye_color(value):
    print("ECL Value", value)


def check_passport_id(value):
    print("PID Value", value)


def check_country_id(value):
    print("CID Value", value)


def switch_on_passport_key(key, value):
    key_valid = True
    if key == 'byr':
        key_valid = check_birth_year(value)
    elif key == 'iyr':
        key_valid = check_issue_year(value)
    elif key == 'eyr':
        key_valid = check_expiration_year(value)
    elif key == 'hgt':
        key_valid = check_height(value)
    # elif key == 'hcl':
    #     check_hair_color(value)
    # elif key == 'ecl':
    #     check_eye_color(value)
    # elif key == 'pid':
    #     check_passport_id(value)
    # elif key == 'cid':
    #     check_country_id(value)

    return key_valid


# Main line
# Start reading the map
all_passports = read_passport_file("Day 04-02 - Passport Processing - Example input - Invalid.txt")
# all_passports = read_passport_file("Day 04-02 - Passport Processing - Example input - Valid.txt")
# all_passports = read_passport_file("Day 04 - Passport Processing.txt")

# Put together Passport data: Combine several Passport line to one line.
all_processed_passports = put_passports_together(all_passports)

# Check every passport to see if it's valid
number_of_valid_passports = 0
for passport_to_check in all_processed_passports:
    passport_is_valid = check_validity_of_passport(passport_to_check)
    if passport_is_valid:
        number_of_valid_passports += 1

print("Number of valid passports:", number_of_valid_passports, "out of", len(all_processed_passports))
