# Advent of Code
# Day 06-01 - Custom Customs
#
# https://adventofcode.com/2020/day/6
#
# --- Day 6: Custom Customs ---
# As your flight approaches the regional airport where you'll switch to a
# much larger plane, customs declaration forms are distributed to the
# passengers.
#
# The form asks a series of 26 yes-or-no questions marked a through z. All
# you need to do is identify the questions for which anyone in your group
# answers "yes". Since your group is just you, this doesn't take very long.
#
# However, the person sitting next to you seems to be experiencing a language
# barrier and asks if you can help. For each of the people in their group,
# you write down the questions for which they answer "yes", one per line. For
# example:
#
# abcx
# abcy
# abcz
#
# In this group, there are 6 questions to which anyone answered "yes": a, b,
# c, x, y, and z. (Duplicate answers to the same question don't count extra;
# each question counts at most once.)
#
# Another group asks for your help, then another, and eventually you've
# collected answers from every group on the plane (your puzzle input). Each
# group's answers are separated by a blank line, and within each group, each
# person's answers are on a single line. For example:
#
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b
#
# This list represents answers from five groups:
#
# - The first group contains one person who answered "yes" to 3 questions:
#   a, b, and c.
# - The second group contains three people; combined, they answered "yes"
#   to 3 questions: a, b, and c.
# - The third group contains two people; combined, they answered "yes" to
#   3 questions: a, b, and c.
# - The fourth group contains four people; combined, they answered "yes"
#   to only 1 question, a.
# - The last group contains one person who answered "yes" to only 1
#   question, b.
#
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
#
# For each group, count the number of questions to which anyone answered
# "yes". What is the sum of those counts?
#


def read_customs_forms_file(customs_declaration_form_file):
    customs_form_file = open(customs_declaration_form_file, "r")
    customs_form_data = customs_form_file.read().splitlines()
    customs_form_file.close()
    return customs_form_data


def split_group_answers(answers):
    answer_split = []
    for answer in answers:
        for char in answer:
            answer_split.append(char)
    return answer_split


def process_customs_forms(customs_declaration_forms):
    group_answers = []
    sum_unique_answers = 0
    for answers in customs_declaration_forms:
        if answers != '':
            group_answers.append(answers)
        else:
            group_answers_split = split_group_answers(group_answers)
            # Now make the list unique with help of a set
            group_answers_unique = set(group_answers_split)
            sum_unique_answers += len(group_answers_unique)
            group_answers = []
    group_answers_split = split_group_answers(group_answers)
    # Now make the list unique with help of a set
    group_answers_unique = set(group_answers_split)
    sum_unique_answers += len(group_answers_unique)
    print("Sum of unique answers:", sum_unique_answers)


# Main line
# Start reading the customs declaration forms
# all_forms = read_customs_forms_file("Day 06 - Custom Customs - Example input.txt")
all_forms = read_customs_forms_file("Day 06 - Custom Customs.txt")

print(all_forms)
process_customs_forms(all_forms)

