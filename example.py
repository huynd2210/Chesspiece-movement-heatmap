from heatmap import generate_heatmap, print_heatmap

# Create a 6x6 chess board
grid = [[0] * 6 for _ in range(6)]

# Define knight movement pattern (L-shaped moves)
knight_moves = [
    (-2, -1), (-1, -2),  # Up-left moves
    (1, -2), (2, -1),    # Down-left moves
    (2, 1), (1, 2),      # Down-right moves
    (-1, 2), (-2, 1)     # Up-right moves
]

# Starting position: row 2, column 2 (center of board)
start_position = (2, 2)

# Generate the heatmap
heatmap = generate_heatmap(grid, knight_moves, start_position)

# Display the result
print("Knight Movement Heatmap")
print("======================")
print(f"Starting from position ({start_position[0]}, {start_position[1]})")
print("\nMinimum moves to reach each square:")
print_heatmap(heatmap)

print("\nHow to read:")
print("- '0' = Starting position")
print("- '1' = Can reach in 1 move")
print("- '2' = Can reach in 2 moves")
print("- '3' = Can reach in 3 moves")
print("- '-' = Cannot reach from starting position")
