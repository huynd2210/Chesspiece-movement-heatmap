#!/usr/bin/env python3
"""
Chess Movement Heatmap Generator CLI

A command-line tool to generate movement heatmaps for various chess pieces,
including standard chess, fairy chess, xiangqi, and shogi variants.
"""

import argparse
import sys
from typing import List, Tuple, Optional
from heatmap import generate_heatmap, print_heatmap
from heatmap_with_obstacles import generate_heatmap_with_obstacles, print_heatmap_with_obstacles
from exotic_pieces import get_piece_movements
from fairy_chess_pieces import fairy_chess_pieces

# Combine all piece dictionaries
ALL_PIECES = {}
ALL_PIECES.update(get_piece_movements())
ALL_PIECES.update(fairy_chess_pieces)

# Normalize piece names for case-insensitive lookup
NORMALIZED_PIECES = {name.lower().replace(" ", "-"): name for name in ALL_PIECES.keys()}


def list_pieces(category: Optional[str] = None):
    """List all available pieces, optionally filtered by category."""
    categories = {
        "standard": ["king", "queen", "rook", "bishop", "knight", "pawn"],
        "fairy": ["camel", "zebra", "grasshopper", "amazon", "archbishop", "chancellor"],
        "xiangqi": ["xiangqi_horse", "xiangqi_elephant", "xiangqi_cannon", "xiangqi_general"],
        "shogi": ["shogi_gold", "shogi_silver", "shogi_lance", "shogi_knight"],
    }
    
    if category:
        category = category.lower()
        if category in categories:
            print(f"\n{category.upper()} PIECES:")
            print("=" * 40)
            for piece in sorted(ALL_PIECES.keys()):
                if any(keyword in piece.lower() for keyword in categories[category]):
                    print(f"  {piece}")
        else:
            print(f"Unknown category: {category}")
            print("Available categories: standard, fairy, xiangqi, shogi")
    else:
        print("\nALL AVAILABLE PIECES:")
        print("=" * 50)
        sorted_pieces = sorted(ALL_PIECES.keys())
        for i in range(0, len(sorted_pieces), 3):
            row = sorted_pieces[i:i+3]
            print("  " + "".join(f"{p:<25}" for p in row))
        print(f"\nTotal: {len(ALL_PIECES)} pieces")


def parse_position(pos_str: str) -> Tuple[int, int]:
    """Parse position string like 'e4' or '4,4' into (row, col) tuple."""
    pos_str = pos_str.strip().lower()
    
    # Try numeric format first (row,col)
    if ',' in pos_str:
        try:
            row, col = map(int, pos_str.split(','))
            return (row, col)
        except ValueError:
            raise ValueError(f"Invalid position format: {pos_str}")
    
    # Try chess notation (e.g., 'e4')
    if len(pos_str) == 2 and pos_str[0].isalpha() and pos_str[1].isdigit():
        col = ord(pos_str[0]) - ord('a')
        row = int(pos_str[1]) - 1
        return (row, col)
    
    raise ValueError(f"Invalid position format: {pos_str}. Use 'e4' or '4,4' format.")


def parse_obstacles(obstacle_str: str) -> List[Tuple[int, int]]:
    """Parse obstacle string into list of positions."""
    obstacles = []
    for pos in obstacle_str.split(';'):
        pos = pos.strip()
        if pos:
            obstacles.append(parse_position(pos))
    return obstacles


def parse_size(size_str: str) -> Tuple[int, int]:
    """Parse size string like '8' or '10x6' into (rows, cols) tuple."""
    size_str = size_str.strip().lower()
    if 'x' in size_str:
        try:
            rows, cols = map(int, size_str.split('x'))
            return (rows, cols)
        except ValueError:
            raise ValueError(f"Invalid size format: {size_str}")
    else:
        try:
            size = int(size_str)
            return (size, size)
        except ValueError:
            raise ValueError(f"Invalid size format: {size_str}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate movement heatmaps for chess pieces",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s knight --size 8 --position e4
  %(prog)s "flying ox" --size 12 --position 6,6
  %(prog)s rook --size 10 --position 5,5 --obstacles "3,5;7,5"
  %(prog)s --list
  %(prog)s --list fairy
  %(prog)s --search dragon
        """
    )
    
    # Main arguments
    parser.add_argument("piece", nargs="?", help="Name of the chess piece")
    
    # Board configuration
    parser.add_argument("-s", "--size", type=str, default="8",
                        help="Board size (e.g., 8 or 10x6) (default: 8)")
    parser.add_argument("-p", "--position", default=None,
                        help="Starting position (e.g., 'e4' or '4,4'). Default: center")
    parser.add_argument("-o", "--obstacles", default=None,
                        help="Obstacle positions separated by semicolons (e.g., '3,5;7,5')")
    
    # Display options
    parser.add_argument("-w", "--width", type=int, default=3,
                        help="Cell width for display (default: 3)")
    parser.add_argument("--no-legend", action="store_true",
                        help="Don't show movement count legend")
    
    # Information commands
    parser.add_argument("-l", "--list", nargs="?", const="all", metavar="CATEGORY",
                        help="List available pieces (optionally by category)")
    parser.add_argument("--search", metavar="TERM",
                        help="Search for pieces containing term")
    parser.add_argument("-i", "--info", action="store_true",
                        help="Show detailed information about the piece")
    
    args = parser.parse_args()
    
    # Handle list command
    if args.list:
        list_pieces(args.list if args.list != "all" else None)
        return
    
    # Handle search command
    if args.search:
        search_term = args.search.lower()
        matches = [name for name in ALL_PIECES.keys() if search_term in name.lower()]
        if matches:
            print(f"\nPieces matching '{args.search}':")
            print("=" * 40)
            for piece in sorted(matches):
                print(f"  {piece}")
            print(f"\nFound {len(matches)} matches")
        else:
            print(f"No pieces found matching '{args.search}'")
        return
    
    # Require piece name for other operations
    if not args.piece:
        parser.error("piece name is required (use --list to see available pieces)")
    
    # Normalize piece name
    piece_input = args.piece.lower().replace("-", " ").replace("_", " ")
    
    # Try to find exact match first
    piece_name = None
    if piece_input in ALL_PIECES:
        piece_name = piece_input
    else:
        # Try normalized lookup
        normalized_input = piece_input.replace(" ", "-")
        if normalized_input in NORMALIZED_PIECES:
            piece_name = NORMALIZED_PIECES[normalized_input]
        else:
            # Try partial match
            matches = [name for name in ALL_PIECES.keys() if piece_input in name.lower()]
            if len(matches) == 1:
                piece_name = matches[0]
            elif len(matches) > 1:
                print(f"Multiple pieces match '{args.piece}':")
                for match in sorted(matches):
                    print(f"  {match}")
                print("\nPlease be more specific.")
                sys.exit(1)
            else:
                print(f"Unknown piece: '{args.piece}'")
                print("Use --list to see available pieces or --search to find pieces")
                sys.exit(1)
    
    # Get piece movements
    movements = ALL_PIECES[piece_name]
    
    # Show info if requested
    if args.info:
        print(f"\nPIECE: {piece_name}")
        print("=" * (len(piece_name) + 7))
        print(f"Movement patterns: {len(movements)}")
        print(f"Maximum range: {max(max(abs(r), abs(c)) for r, c in movements) if movements else 0}")
        print("\nMovement offsets:")
        for i, (row, col) in enumerate(movements):
            if i % 4 == 0:
                print()
            print(f"  ({row:2},{col:2})", end="")
        print("\n")
        return
    
    # Set up board
    try:
        rows, cols = parse_size(args.size)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    if args.position:
        try:
            start_pos = parse_position(args.position)
            # Validate position
            if not (0 <= start_pos[0] < rows and 0 <= start_pos[1] < cols):
                print(f"Error: Position {start_pos} is outside the {rows}x{cols} board")
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        start_pos = (rows // 2, cols // 2)
    
    # Parse obstacles if provided
    obstacles = None
    if args.obstacles:
        try:
            obstacles = parse_obstacles(args.obstacles)
            # Validate obstacles
            for obs in obstacles:
                if not (0 <= obs[0] < rows and 0 <= obs[1] < cols):
                    print(f"Error: Obstacle at {obs} is outside the board")
                    sys.exit(1)
                if obs == start_pos:
                    print(f"Error: Cannot place obstacle at starting position {obs}")
                    sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    # Generate and display heatmap
    grid = [[0] * cols for _ in range(rows)]
    
    print(f"\n{piece_name.upper()} MOVEMENT HEATMAP")
    print("=" * (len(piece_name) + 17))
    print(f"Board: {rows}x{cols}")
    print(f"Starting position: {start_pos}")
    if obstacles:
        print(f"Obstacles: {obstacles}")
    print()
    
    if obstacles:
        heatmap = generate_heatmap_with_obstacles(grid, movements, start_pos, obstacles)
        print_heatmap_with_obstacles(heatmap, args.width)
    else:
        heatmap = generate_heatmap(grid, movements, start_pos)
        print_heatmap(heatmap, args.width)
    
    if not args.no_legend:
        print(f"\nLegend:")
        print(f"  0 = Starting position")
        print(f"  N = Reachable in N moves")
        print(f"  - = Unreachable")
        if obstacles:
            print(f"  X = Obstacle")
        print(f"\nTotal movement options: {len(movements)}")
        
        # Calculate reachable squares
        reachable = sum(1 for row in heatmap for cell in row if cell >= 0)
        total = rows * cols
        if obstacles:
            total -= len(obstacles)
        print(f"Reachable squares: {reachable}/{total} ({reachable/total*100:.1f}%)")


if __name__ == "__main__":
    main()
