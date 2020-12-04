# Advent of Code
# Day 04-01 - Passport Processing
#
# https://adventofcode.com/2020/day/4
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


def check_birth_year(passport):
    passport_dict = dict(passp.split(':') for passp in passport)
    print(passport_dict)
    return True


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
            expected_fields[key] = True
    # Check all field from passport
    # print(expected_fields)
    passport_still_valid = True
    for key, value in expected_fields.items():
        # print("K", key, "V", value)
        if not value and key != 'cid':
            passport_still_valid = False
    return passport_still_valid

    # valid_birth_year = check_birth_year(passport)


# Main line
# Start reading the map
# all_passports = read_passport_file("Day 04-01 - Passport Processing - Example input.txt")
all_passports = read_passport_file("Day 04 - Passport Processing.txt")

# Put together Passport data: Combine several Passport line to one line.
all_processed_passports = put_passports_together(all_passports)

# Check every passport to see if it's valid
number_of_valid_passports = 0
for passport_to_check in all_processed_passports:
    passport_is_valid = check_validity_of_passport(passport_to_check)
    if passport_is_valid:
        number_of_valid_passports += 1

print("Number of valid passports:", number_of_valid_passports, "out of", len(all_processed_passports))
