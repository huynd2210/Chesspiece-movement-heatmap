# Chess Movement Heatmap Generator

A Python tool that generates movement heatmaps for various chess pieces from different chess variants including standard chess, fairy chess, Xiangqi (Chinese Chess), and Shogi (Japanese Chess). Currently supports **183 different piece types** from various historical and modern chess variants.

## Overview

This tool uses Breadth-First Search (BFS) to calculate the minimum number of moves required for a piece to reach any square on the board from a given starting position. The result is visualized as a heatmap where each cell shows the distance in moves.

## Usage

### Basic Example
```python
from heatmap import generate_heatmap, print_heatmap

# Create a grid
grid = [[0] * 8 for _ in range(8)]

# Define piece movements (e.g., knight)
knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# Generate heatmap from position (3, 3)
heatmap = generate_heatmap(grid, knight_moves, (3, 3))

# Display the heatmap
print_heatmap(heatmap)
```

**Output:**
```
  2   3   2   3   2   3   2   3
  3   4   1   2   1   4   3   2
  2   1   2   3   2   1   2   3
  3   2   3   0   3   2   3   2
  2   1   2   3   2   1   2   3
  3   4   1   2   1   4   3   2
  2   3   2   3   2   3   2   3
  3   2   3   2   3   2   3   4
```

### With Obstacles
```python
from heatmap_with_obstacles import generate_heatmap_with_obstacles, print_heatmap_with_obstacles

# Define obstacles as list of (row, col) tuples
obstacles = [(2, 3), (2, 4), (2, 5)]

# Generate heatmap with obstacles
heatmap = generate_heatmap_with_obstacles(grid, knight_moves, (0, 0), obstacles)
print_heatmap_with_obstacles(heatmap)
```

**Output:**
```
  0   3   2   5   2   3   4   5
  3   4   1   2   3   4   3   4
  2   1   4   X   X   X   4   5
  3   2   3   2   3   4   5   4
  2   3   2   3   4   3   4   5
  3   4   3   4   3   4   5   4
  4   3   4   3   4   5   4   5
  5   4   5   4   5   4   5   6
```

## Implemented Pieces

This tool supports **183 different chess pieces** from various chess variants including standard chess, fairy chess, Xiangqi, and Shogi. Below are examples such as Camel, Zebra, Nightrider, and Dragon King. For the complete list, see [`fairy_chess_pieces.py`](fairy_chess_pieces.py) and [`exotic_pieces.py`](exotic_pieces.py).

## Movement Notation

Movement patterns are defined as lists of (row_offset, col_offset) tuples:

```python
# Examples:
knight = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
king = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
rook = [(i, 0) for i in range(-7, 8) if i != 0] + [(0, i) for i in range(-7, 8) if i != 0]
```

## Heatmap Interpretation

- `0`: Starting position
- `1, 2, 3...`: Minimum number of moves to reach that square
- `-1`: Unreachable from starting position
- `-2`: Obstacle (when using obstacle-aware version)



## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## CLI Usage

The project includes a command-line interface (`chess_heatmap_cli.py`) for easy interaction:

### Basic Usage

```bash
# Generate heatmap for a knight
python chess_heatmap_cli.py knight

# Specify board size and starting position
python chess_heatmap_cli.py knight --size 10 --position 5,5

# Use chess notation for position
python chess_heatmap_cli.py rook --position e4

# Add obstacles
python chess_heatmap_cli.py queen --obstacles "3,4;5,6;7,2"
```

### Information Commands

```bash
# List all available pieces
python chess_heatmap_cli.py --list

# List pieces by category
python chess_heatmap_cli.py --list fairy
python chess_heatmap_cli.py --list shogi

# Search for pieces
python chess_heatmap_cli.py --search dragon
python chess_heatmap_cli.py --search general

# Get detailed information about a piece
python chess_heatmap_cli.py flying-ox --info
```

### Advanced Options

```bash
# Adjust display width
python chess_heatmap_cli.py knight --width 4

# Hide legend
python chess_heatmap_cli.py pawn --no-legend

# Complex example with multiple options
python chess_heatmap_cli.py drunk-elephant --size 12 --position 6,6 --obstacles "5,6;7,6" --width 2
```

### Available Options

- `piece`: Name of the chess piece (required unless using --list or --search)
- `-s, --size SIZE`: Board size as 'N' or 'NxM' (default: 8)
- `-p, --position POSITION`: Starting position as 'e4' or '4,4' (default: center)
- `-o, --obstacles OBSTACLES`: Obstacle positions separated by semicolons
- `-w, --width WIDTH`: Cell width for display (default: 3)
- `--no-legend`: Don't show movement count legend
- `-l, --list [CATEGORY]`: List available pieces (optionally by category)
- `--search TERM`: Search for pieces containing term
- `-i, --info`: Show detailed information about the piece

## License

This project is open source and available for educational and personal use.
