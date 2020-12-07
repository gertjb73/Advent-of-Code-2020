# NOT FINISHED #####
# Advent of Code
# Day 07-02 - Handy Haversacks
#
# https://adventofcode.com/2020/day/7#part2
#
# --- Day 7: Handy Haversacks ---
# You land at the regional airport in time for your next flight. In fact,
# it looks like you'll even have time to grab some food: all flights are
# currently delayed due to issues in luggage processing.
#
# Due to recent aviation regulations, many rules (your puzzle input) are
# being enforced about bags and their contents; bags must be color-coded and
# must contain specific quantities of other color-coded bags. Apparently,
# nobody responsible for these regulations considered how long they would
# take to enforce!
#
# For example, consider the following rules:
#
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
#
# These rules specify the required contents for 9 bag types. In this example,
# every faded blue bag is empty, every vibrant plum bag contains 11 bags (5
# faded blue and 6 dotted black), and so on.
#
# You have a shiny gold bag. If you wanted to carry it in at least one other
# bag, how many different bag colors would be valid for the outermost bag?
# (In other words: how many colors can, eventually, contain at least one
# shiny gold bag?)
#
# In the above rules, the following options would be available to you:
#
# - A bright white bag, which can hold your shiny gold bag directly.
# - A muted yellow bag, which can hold your shiny gold bag directly, plus
#   some other bags.
# - A dark orange bag, which can hold bright white and muted yellow bags,
#   either of which could then hold your shiny gold bag.
# - A light red bag, which can hold bright white and muted yellow bags,
#   either of which could then hold your shiny gold bag.
#
# So, in this example, the number of bag colors that can eventually contain
# at least one shiny gold bag is 4.
#
# How many bag colors can eventually contain at least one shiny gold bag?
# (The list of rules is quite long; make sure you get all of it.)
#
# Your puzzle answer was 101.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
#
# It's getting pretty expensive to fly these days - not because of ticket
# prices, but because of the ridiculous number of bags you need to buy!
#
# Consider again your shiny gold bag and the rules from the above example:
#
# - faded blue bags contain 0 other bags.
# - dotted black bags contain 0 other bags.
# - vibrant plum bags contain 11 other bags: 5 faded blue bags and 6
#   dotted black bags.
# - dark olive bags contain 7 other bags: 3 faded blue bags and 4
#   dotted black bags.
#
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags
# within it) plus 2 vibrant plum bags (and the 11 bags within each of those):
# 1 + 1*7 + 2 + 2*11 = 32 bags!
#
# Of course, the actual rules have a small chance of going several levels
# deeper than this example; be sure to count all of the bags, even if the
# nesting becomes topologically impractical!
#
# Here's another example:
#
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
#
# In this example, a single shiny gold bag must contain 126 other bags.
#
# How many individual bags are required inside your single shiny gold bag?

def read_luggage_rules_file(luggage_rules_file):
    luggage_file = open(luggage_rules_file, "r")
    luggage_data = luggage_file.read().splitlines()
    luggage_file.close()
    return luggage_data


def put_rules_in_dict(luggage_rules):
    rule_dict = {}
    for rule in luggage_rules:
        string_bag_removed = rule.replace(' bags', '').replace(' bag', '')
        luggage_split = string_bag_removed[:-1].split(" contain ")
        rule_dict[luggage_split[0]] = luggage_split[1].split(', ')
    return rule_dict


def check_luggage(all_bags_to_check, bag_to_check, number_of_bags):
    print("Number of Bags Param", number_of_bags)
    total_found = 0
    stop_here = "no other"
    if bag_to_check != stop_here:
        for next_bags in all_bags_to_check[bag_to_check]:
            # Remove digits and leading space from 'more_bags'
            next_bag = (''.join([i for i in next_bags if not i.isdigit()])).lstrip()
            if next_bag != stop_here:
                number_of_next_bags = int((''.join([i for i in next_bags if not i.isalpha()])).rstrip())
                print("Multiplying by", int((''.join([i for i in next_bags if not i.isalpha()])).rstrip()))
                # print(next_bag, "(", number_of_bags, ")", "->", all_bags_to_check[next_bag])
                number_of_bags_temp = check_luggage(all_bags_to_check, next_bag, number_of_next_bags)
                number_of_bags *= number_of_bags_temp
                print("Adding", number_of_bags_temp)
                # print(next_bag, "(", number_of_bags, ")", "->", all_bags_to_check[next_bag])
            else:
                return number_of_bags
    else:
        return number_of_bags
    return number_of_bags


# Main line
# Start reading the luggage rules
# all_luggage_rules = read_luggage_rules_file("Day 07 - Handy Haversacks.txt")
all_luggage_rules = read_luggage_rules_file("Day 07-01 - Handy Haversacks - Example input.txt")
all_luggage_rules = read_luggage_rules_file("Day 07-02 - Handy Haversacks - Example input.txt")
print(all_luggage_rules)

luggage_dict = put_rules_in_dict(all_luggage_rules)
print(luggage_dict)

bag = "shiny gold"

print("shiny gold ->", luggage_dict[bag])
number_of_bags_total = check_luggage(luggage_dict, bag, 1)
print("End total", number_of_bags_total)
# luggage_found = 0
# for luggage_rule in luggage_dict:
#     found = False
#     luggage_to_find = "shiny gold"
#     print(luggage_rule, '->', luggage_dict[luggage_rule], end="")
#     found = check_luggage(luggage_dict, luggage_rule, luggage_to_find, found)
#     if found:
#         print("->", luggage_to_find, "was FOUND")
#         luggage_found += 1
#     else:
#         print("")
#
# print("\nNumber of colored bags found: ", luggage_found)
