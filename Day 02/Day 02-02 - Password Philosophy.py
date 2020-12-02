# Advent of Code
# Day 02-01 - Password Philosophy
#
# https://adventofcode.com/2020/day/2
#
# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport;
# the easiest way down to the coast from here is via toboggan.
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
# "Something's wrong with our computers; we can't log in!"
# You ask if you can take a look.
#
# Their password database seems to be a little corrupted:
# some of the passwords wouldn't have been allowed by
# the Official Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input)
# of passwords (according to the corrupted database) and the corporate policy
# when that password was set.
#
# For example, suppose you have the following list:
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
#
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number
# of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain
# a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password,
# cdefg, is not; it contains no instances of b, but needs at least 1.
# The first and third passwords are valid: they contain one a or
# nine c, both within the limits of their respective policies.
#
# How many passwords are valid according to their policies?
#
# Your puzzle answer was 603.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem
# to be what the Official Toboggan Corporate Authentication System is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained
# the password policy rules from his old job at the sled rental place down the street!
# The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two positions in the password,
# where 1 means the first character, 2 means the second character, and so on.
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter.
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

def read_password_file():
    password_file = open("Day 02 - Password Philosophy.txt", "r")
    password_lines = password_file.readlines()
    return password_lines


def process_password(password_line_to_process):
    # Strip newline from password line
    password_line = password_line_to_process.rstrip()

    # Split in Policy and Password
    (password_policy, password) = password_line.split(": ")

    # Split Policy in Positions and Character
    (policy_positions, policy_character) = password_policy.split()

    # Split PolicyPositions in First and Second
    (policy_position_1, policy_position_2) = policy_positions.split("-")
    password_char_1 = password[int(policy_position_1)-1]
    password_char_2 = password[int(policy_position_2)-1]

    # Check Policy Character in Password
    # Check if password meets policy
    #
    # 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    # 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    # 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    position_1_correct = True if password_char_1 == policy_character else False
    position_2_correct = True if password_char_2 == policy_character else False

    if position_1_correct or position_2_correct:
        return_value = True
    if not position_1_correct and not position_2_correct:
        return_value = False
    if position_1_correct and position_2_correct:
        return_value = False

    return return_value


# Main line

# Initializing
correct_count = 0
incorrect_count = 0

# Start reading
password_database = read_password_file()

# Process password
database_length = len(password_database)
for counter in range(database_length):
    password_correct = process_password(password_database[counter])
    if password_correct:
        correct_count += 1
    else:
        incorrect_count += 1

print("Correct:", correct_count, "Incorrect:", incorrect_count)
