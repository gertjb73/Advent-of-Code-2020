# Advent of Code
# Day 03-02 - Toboggan Trajectory
#
# https://adventofcode.com/2020/day/3#part2
#
# --- Day 3: Toboggan Trajectory ---
# With the toboggan login problems resolved, you set off toward the airport.
# While travel by toboggan might be easy, it's certainly not safe: there's
# very minimal steering and the area is covered in trees. You'll need to see
# which angles will take you near the fewest trees.
#
# Due to the local geology, trees in this area only grow on exact integer
# coordinates in a grid. You make a map (your puzzle input) of the open
# squares (.) and trees (#) you can see. For example:
#
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
#
# These aren't the only trees, though; due to something you read about once
# involving arboreal genetics and biome stability, the same pattern repeats
# to the right many times:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........#.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...##....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# You start on the open square (.) in the top-left corner and need to reach
# the bottom (below the bottom-most row on your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper
# model that prefers rational numbers); start by counting all the trees you
# would encounter for the slope right 3, down 1:
#
# From your starting position at the top-left, check the position that is
# right 3 and down 1. Then, check the position that is right 3 and down 1
# from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with O where
# there was an open square and X where there was a tree:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# In this example, traversing the map using this slope would cause you to
# encounter 7 trees.
#
# Starting at the top-left corner of your map and following a slope of right
# 3 and down 1, how many trees would you encounter?
#
# Your puzzle answer was 216.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability
# of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the
# following slopes, you start at the top-left corner and traverse the map all
# the way to the bottom:
#
# - Right 1, down 1.
# - Right 3, down 1. (This is the slope you already checked.)
# - Right 5, down 1.
# - Right 7, down 1.
# - Right 1, down 2.
#
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
# respectively; multiplied together, these produce the answer 336.
#
# What do you get if you multiply together the number of trees encountered on
# each of the listed slopes?
#

def read_map_file(file_name_of_map):
    map_file = open(file_name_of_map, "r")
    map_data = map_file.read().splitlines()
    map_file.close()
    return map_data


def determine_next_coordinates(coord_x, coord_y, go_right, go_down, size_of_map):
    # Keep in mind map-sizes are based on maps starting at (1,1)
    # This map (Python rules) starts at (0,0)
    # So size_of_map should be reduced by one
    steps_right = go_right
    steps_down = go_down
    coord_x += steps_right
    coord_y += steps_down
    on_map = True if coord_y <= size_of_map - 1 else False
    return coord_x, coord_y, on_map


def check_coordinates_for_tree(coord_x, coord_y):
    map_line = full_map[coord_y]
    tree_on_location = True if map_line[coord_x % map_size_x] == "#" else False
    return tree_on_location


def check_for_different_step(steps_right, steps_down):
    # Starting point on the map is (0,0)
    x, y = 0, 0
    # Determine next step
    still_on_map = True
    number_of_trees = 0
    while still_on_map:
        x, y, still_on_map = determine_next_coordinates(x, y, right, down, map_size_y)
        # Check new location for tree
        if still_on_map:
            tree_found = check_coordinates_for_tree(x, y)
            if tree_found:
                number_of_trees += 1

    return number_of_trees


# Main line
# Start reading the map
# full_map = read_map_file("Day 03 - Toboggan Trajectory - Example input.txt")
full_map = read_map_file("Day 03 - Toboggan Trajectory.txt")

# Set steps and other map related variables
print(full_map)
map_size_x = len(full_map[0])
map_size_y = len(full_map)
# - Right 1, down 1.
# - Right 3, down 1. (This is the slope you already checked.)
# - Right 5, down 1.
# - Right 7, down 1.
# - Right 1, down 2.
steps_to_check = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

multiply_answer = 1
for steps in steps_to_check:
    right, down = steps
    counted_trees = check_for_different_step(right, down)
    multiply_answer *= counted_trees
    print("Steps Right, Down (", right, ",", down, ")\t\tNumber of trees found:", counted_trees, "\tMultiply:",
          multiply_answer)
