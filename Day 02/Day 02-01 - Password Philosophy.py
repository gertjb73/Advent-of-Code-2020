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

def read_password_file():
    password_file = open("Day 02 - Password Philosophy.txt", "r")
    password_lines = password_file.readlines()
    return password_lines


def process_password(password_line_to_process):
    # Strip newline from password line
    password_line = password_line_to_process.rstrip()

    # Split in Policy and Password
    (password_policy, password) = password_line.split(":")

    # Split Policy in MinMax and Character
    (policy_min_max, policy_character) = password_policy.split()

    # Split PolicyMinMax in Minimum and Maximum
    (policy_min, policy_max) = policy_min_max.split("-")

    # Count Policy Character in Password
    count = password.count(policy_character)

    # Check if password meets policy
    return_value = True if int(policy_min) <= count <= int(policy_max) else False

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
