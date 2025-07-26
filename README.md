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

### With Obstacles
```python
from heatmap_with_obstacles import generate_heatmap_with_obstacles, print_heatmap_with_obstacles

# Define obstacles as list of (row, col) tuples
obstacles = [(2, 3), (2, 4), (2, 5)]

# Generate heatmap with obstacles
heatmap = generate_heatmap_with_obstacles(grid, knight_moves, (0, 0), obstacles)
print_heatmap_with_obstacles(heatmap)
```

## Implemented Pieces

This tool implements **183 different chess pieces** from various chess variants throughout history and from different cultures. Below are some examples from each category. For a complete list of all pieces, see [`fairy_chess_pieces.py`](fairy_chess_pieces.py) and [`exotic_pieces.py`](exotic_pieces.py), or use the CLI with `--list` command.

### Standard Chess Pieces

| Piece | Movement Pattern |
|-------|-----------------|
| **King** | One square in any direction (orthogonal and diagonal) |
| **Queen** | Any distance in any direction (orthogonal and diagonal) |
| **Rook** | Any distance orthogonally (horizontal or vertical) |
| **Bishop** | Any distance diagonally |
| **Knight** | L-shaped: 2 squares in one direction, 1 square perpendicular |
| **Pawn** | One square forward (special rules for capture/initial move not implemented) |

### Fairy Chess Pieces

| Piece | Movement Pattern | Description |
|-------|-----------------|-------------|
| **Camel** | (3,1) jumper | Jumps 3 squares in one direction, 1 perpendicular |
| **Zebra** | (3,2) jumper | Jumps 3 squares in one direction, 2 perpendicular |
| **Giraffe** | (4,1) jumper | Jumps 4 squares in one direction, 1 perpendicular |
| **Nightrider** | Extended knight | Moves like a knight but can continue in same direction |
| **Dabbaba** | (2,0) jumper | Jumps exactly 2 squares orthogonally |
| **Alfil** | (2,2) jumper | Jumps exactly 2 squares diagonally |
| **Wazir** | One square orthogonal | Moves 1 square horizontally or vertically |
| **Ferz** | One square diagonal | Moves 1 square diagonally |
| **Amazon** | Queen + Knight | Combines all queen and knight moves |
| **Archbishop** | Bishop + Knight | Combines bishop and knight moves |
| **Chancellor** | Rook + Knight | Combines rook and knight moves |
| **Grasshopper** | Hopper | Jumps over pieces (simplified as 2+ square jumps) |

...and many more exotic pieces including:
- **Chu Shogi pieces**: Lion, Kirin, Phoenix, Drunk Elephant, Flying Ox, etc.
- **Taikyoku Shogi pieces**: Emperor, Teaching King, Buddhist Spirit, Heavenly Horse, etc.
- **Grant Acedrex pieces**: Unicorno, Rhinoceros, Gryphon, etc.
- **Modern variants**: Rose, Nightrider variants, compound leapers, etc.

For the complete list of 156+ fairy chess pieces, see [`fairy_chess_pieces.py`](fairy_chess_pieces.py).

### Xiangqi (Chinese Chess) Pieces

| Piece | Movement Pattern | Description |
|-------|-----------------|-------------|
| **Horse (馬)** | Same as chess knight | L-shaped movement |
| **Elephant (象)** | (2,2) jumper | Moves exactly 2 points diagonally |
| **Cannon (砲)** | Orthogonal slider | Moves like rook (capture rules not implemented) |
| **Soldier (兵)** | Forward one square | Before river crossing |
| **Soldier (promoted)** | Forward or sideways | After river crossing |
| **General (將)** | One square orthogonal | Moves 1 square horizontally or vertically |
| **Advisor (士)** | One square diagonal | Moves 1 square diagonally |

### Shogi (Japanese Chess) Pieces

| Piece | Movement Pattern | Description |
|-------|-----------------|-------------|
| **Gold General (金)** | 6 directions | One square orthogonally or diagonally forward |
| **Silver General (銀)** | 5 directions | One square diagonally or straight forward |
| **Lance (香)** | Forward only | Any distance straight forward |
| **Knight (桂)** | Forward L-shape | Two forward, one to the side (2 options only) |
| **Dragon King (龍)** | Rook + King | Rook movement plus one square diagonally |
| **Dragon Horse (馬)** | Bishop + King | Bishop movement plus one square orthogonally |

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

## Files

- `heatmap.py`: Core heatmap generation functions
- `heatmap_with_obstacles.py`: Enhanced version with obstacle support and pathfinding
- `exotic_pieces.py`: Collection of 27 pieces from various chess variants
- `fairy_chess_pieces.py`: Comprehensive collection of 156 fairy chess pieces
- `chess_heatmap_cli.py`: Command-line interface for easy interaction
- `test_heatmap.py`: Unit tests and visual demonstrations
- `test_fairy_pieces.py`: Test suite for fairy chess pieces
- `verify_all_pieces.py`: Verification script to check all piece implementations
- `demo.py`: Interactive demonstration of various pieces
- `example.py`: Simple usage example

## Features

- BFS-based shortest path calculation
- Support for arbitrary movement patterns
- Obstacle handling
- Path reconstruction
- Visual heatmap display
- 183 pieces from multiple chess variants worldwide

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
