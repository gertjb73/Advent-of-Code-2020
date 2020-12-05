# Advent of Code
# Day 05-01 - Binary Boarding
#
# https://adventofcode.com/2020/day/5
#
# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your
# boarding pass! You aren't sure which seat is yours, and all of the flight
# attendants are busy with the flood of people that suddenly made it through
# passport control.
#
# You write a quick program to use your phone's camera to scan all of the
# nearby boarding passes (your puzzle input); perhaps you can find your seat
# through process of elimination.
#
# Instead of zones or groups, this airline uses binary space partitioning to
# seat people. A seat might be specified like FBFBBFFRLR, where F means
# "front", B means "back", L means "left", and R means "right".
#
# The first 7 characters will either be F or B; these specify exactly one of
# the 128 rows on the plane (numbered 0 through 127). Each letter tells you
# which half of a region the given seat is in. Start with the whole list of
# rows; the first letter indicates whether the seat is in the front (0
# through 63) or the back (64 through 127). The next letter indicates which
# half of that region the seat is in, and so on until you're left with
# exactly one row.
#
# For example, consider just the first seven characters of FBFBBFFRLR:
#
# - Start by considering the whole range, rows 0 through 127.
# - F means to take the lower half, keeping rows 0 through 63.
# - B means to take the upper half, keeping rows 32 through 63.
# - F means to take the lower half, keeping rows 32 through 47.
# - B means to take the upper half, keeping rows 40 through 47.
# - B keeps rows 44 through 47.
# - F keeps rows 44 through 45.
# - The final F keeps the lower of the two, row 44.
#
# The last three characters will be either L or R; these specify exactly one
# of the 8 columns of seats on the plane (numbered 0 through 7). The same
# process as above proceeds again, this time with only three steps. L means
# to keep the lower half, while R means to keep the upper half.
#
# For example, consider just the last 3 characters of FBFBBFFRLR:
#
# - Start by considering the whole range, columns 0 through 7.
# - R means to take the upper half, keeping columns 4 through 7.
# - L means to take the lower half, keeping columns 4 through 5.
# - The final R keeps the upper of the two, column 5.
#
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
#
# Every seat also has a unique seat ID: multiply the row by 8, then add the
# column. In this example, the seat has ID 44 * 8 + 5 = 357.
#
# Here are some other boarding passes:
#
# - BFFFBBFRRR: row 70, column 7, seat ID 567.
# - FFFBBBFRRR: row 14, column 7, seat ID 119.
# - BBFFBBFRLL: row 102, column 4, seat ID 820.
#
# As a sanity check, look through your list of boarding passes. What is the
# highest seat ID on a boarding pass?


def read_boarding_pass_file(name_of_boarding_pass_file):
    boarding_pass_file = open(name_of_boarding_pass_file, "r")
    boarding_pass_data = boarding_pass_file.read().splitlines()
    boarding_pass_file.close()
    return boarding_pass_data


def determine_new_range(fbrl, range_begin, range_end):
    count_range = len(range(range_begin, range_end + 1))
    if fbrl == 'F' or fbrl == 'L':
        range_end = range_end - int(count_range / 2)
    if fbrl == 'B' or fbrl == 'R':
        range_begin = range_begin + int(count_range / 2)
    return range_begin, range_end


def determine_row(location_params, first_row, last_row):
    for f_or_b in location_params:
        first_row, last_row = determine_new_range(f_or_b, first_row, last_row)
    return first_row


# Main line
# Start reading the boarding pass file
# all_boarding_passes = read_boarding_pass_file("Day 05 - Binary Boarding - Example input.txt")
all_boarding_passes = read_boarding_pass_file("Day 05 - Binary Boarding.txt")

highest_seat_ID = 0
for boarding_pass in all_boarding_passes:
    row_range_first = 0
    row_range_last = 127
    column_range_first = 0
    column_range_last = 7
    print("Boarding Pass:", boarding_pass, end="")
    row_number = determine_row(boarding_pass[:7], row_range_first, row_range_last)
    column_number = determine_row(boarding_pass[7:], column_range_first, column_range_last)
    seat_ID = row_number * 8 + column_number
    print(" - Row:", row_number, " - Column:", column_number, " - Seat ID:", seat_ID)
    if seat_ID > highest_seat_ID:
        highest_seat_ID = seat_ID
print("Highest Seat ID: ", highest_seat_ID)
