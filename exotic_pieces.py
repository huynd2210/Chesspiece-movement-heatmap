from heatmap import generate_heatmap, print_heatmap
from typing import List, Tuple, Dict

def get_piece_movements() -> Dict[str, List[Tuple[int, int]]]:
    """
    Returns movement patterns for various pieces from different chess variants.
    """
    pieces = {
        # Standard Chess
        "knight": [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)],
        "king": [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
        
        # Fairy Chess Pieces
        "camel": [(-3, -1), (-3, 1), (-1, -3), (-1, 3), (1, -3), (1, 3), (3, -1), (3, 1)],  # 3-1 jumper
        "zebra": [(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)],  # 3-2 jumper
        "giraffe": [(-4, -1), (-4, 1), (-1, -4), (-1, 4), (1, -4), (1, 4), (4, -1), (4, 1)],  # 4-1 jumper
        "nightrider": [(i*2, i*1) for i in range(-7, 8) if i != 0] + 
                      [(i*2, -i*1) for i in range(-7, 8) if i != 0] +
                      [(i*1, i*2) for i in range(-7, 8) if i != 0] +
                      [(i*1, -i*2) for i in range(-7, 8) if i != 0],  # Knight rider
        "dabbaba": [(0, 2), (0, -2), (2, 0), (-2, 0)],  # 2-square orthogonal jumper
        "alfil": [(2, 2), (2, -2), (-2, 2), (-2, -2)],  # 2-square diagonal jumper
        "wazir": [(0, 1), (0, -1), (1, 0), (-1, 0)],  # 1-square orthogonal
        "ferz": [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # 1-square diagonal
        "amazon": [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] +  # Knight
                  [(i, 0) for i in range(-7, 8) if i != 0] +  # Rook horizontal
                  [(0, i) for i in range(-7, 8) if i != 0] +  # Rook vertical
                  [(i, i) for i in range(-7, 8) if i != 0] +  # Bishop diagonal
                  [(i, -i) for i in range(-7, 8) if i != 0],  # Bishop anti-diagonal
        
        # Xiangqi (Chinese Chess) Pieces
        "xiangqi_horse": [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)],  # Same as knight
        "xiangqi_elephant": [(2, 2), (2, -2), (-2, 2), (-2, -2)],  # 2-point diagonal
        "xiangqi_cannon": [(i, 0) for i in range(-9, 10) if i != 0] + 
                          [(0, i) for i in range(-9, 10) if i != 0],  # Orthogonal slider
        "xiangqi_soldier": [(1, 0)],  # Forward only (before crossing river)
        "xiangqi_soldier_promoted": [(1, 0), (0, 1), (0, -1)],  # After crossing river
        "xiangqi_general": [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Orthogonal one step
        "xiangqi_advisor": [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Diagonal one step
        
        # Shogi (Japanese Chess) Pieces
        "shogi_gold": [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1)],  # Gold general
        "shogi_silver": [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0)],  # Silver general
        "shogi_lance": [(i, 0) for i in range(1, 9)],  # Forward only slider
        "shogi_knight": [(2, 1), (2, -1)],  # Forward L-shape only
        "shogi_dragon": [(0, 1), (0, -1), (1, 0), (-1, 0)] +  # King moves
                        [(i, i) for i in range(-8, 9) if i != 0] +  # Bishop diagonal
                        [(i, -i) for i in range(-8, 9) if i != 0],  # Bishop anti-diagonal
        "shogi_horse": [(1, 1), (1, -1), (-1, 1), (-1, -1)] +  # King moves
                       [(i, 0) for i in range(-8, 9) if i != 0] +  # Rook horizontal
                       [(0, i) for i in range(-8, 9) if i != 0],  # Rook vertical
        
        # Other Interesting Pieces
        "grasshopper": [(i, 0) for i in range(-7, 8) if abs(i) > 1] +  # Must jump over a piece
                       [(0, i) for i in range(-7, 8) if abs(i) > 1] +
                       [(i, i) for i in range(-7, 8) if abs(i) > 1] +
                       [(i, -i) for i in range(-7, 8) if abs(i) > 1],
        "archbishop": [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] +  # Knight
                      [(i, i) for i in range(-7, 8) if i != 0] +  # Bishop diagonal
                      [(i, -i) for i in range(-7, 8) if i != 0],  # Bishop anti-diagonal
        "chancellor": [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] +  # Knight
                      [(i, 0) for i in range(-7, 8) if i != 0] +  # Rook horizontal
                      [(0, i) for i in range(-7, 8) if i != 0],  # Rook vertical
    }
    
    return pieces


def demonstrate_piece(grid_size: int, piece_name: str, movements: List[Tuple[int, int]], 
                     start_pos: Tuple[int, int] = None):
    """Demonstrate a single piece's movement heatmap."""
    if start_pos is None:
        start_pos = (grid_size // 2, grid_size // 2)
    
    grid = [[0] * grid_size for _ in range(grid_size)]
    heatmap = generate_heatmap(grid, movements, start_pos)
    
    print(f"\n{piece_name.upper()} - Starting from ({start_pos[0]}, {start_pos[1]}):")
    print("=" * (len(piece_name) + 30))
    print_heatmap(heatmap)


def main():
    pieces = get_piece_movements()
    
    # Demonstrate fairy chess pieces
    print("FAIRY CHESS PIECES")
    print("==================")
    
    demonstrate_piece(8, "Camel (3-1 jumper)", pieces["camel"])
    demonstrate_piece(8, "Zebra (3-2 jumper)", pieces["zebra"])
    demonstrate_piece(8, "Dabbaba (2-square orthogonal jumper)", pieces["dabbaba"])
    demonstrate_piece(8, "Alfil (2-square diagonal jumper)", pieces["alfil"])
    
    # Demonstrate Xiangqi pieces
    print("\n\nXIANGQI (CHINESE CHESS) PIECES")
    print("================================")
    
    demonstrate_piece(9, "Xiangqi Elephant", pieces["xiangqi_elephant"], (4, 4))
    demonstrate_piece(9, "Xiangqi General", pieces["xiangqi_general"], (4, 4))
    demonstrate_piece(9, "Xiangqi Advisor", pieces["xiangqi_advisor"], (4, 4))
    demonstrate_piece(9, "Xiangqi Soldier (promoted)", pieces["xiangqi_soldier_promoted"], (4, 4))
    
    # Demonstrate Shogi pieces
    print("\n\nSHOGI (JAPANESE CHESS) PIECES")
    print("==============================")
    
    demonstrate_piece(9, "Shogi Gold General", pieces["shogi_gold"], (4, 4))
    demonstrate_piece(9, "Shogi Silver General", pieces["shogi_silver"], (4, 4))
    demonstrate_piece(9, "Shogi Knight", pieces["shogi_knight"], (7, 4))  # Start near bottom
    demonstrate_piece(9, "Shogi Lance", pieces["shogi_lance"], (8, 4))  # Start at bottom
    
    # Demonstrate powerful compound pieces
    print("\n\nCOMPOUND PIECES")
    print("===============")
    
    demonstrate_piece(8, "Archbishop (Knight + Bishop)", pieces["archbishop"], (3, 3))
    demonstrate_piece(8, "Chancellor (Knight + Rook)", pieces["chancellor"], (3, 3))
    
    # Special demonstration: Compare similar pieces
    print("\n\nCOMPARISON: Different Jump Patterns")
    print("====================================")
    
    for name, piece_type in [("Knight (2-1)", "knight"), 
                             ("Camel (3-1)", "camel"), 
                             ("Zebra (3-2)", "zebra"),
                             ("Giraffe (4-1)", "giraffe")]:
        demonstrate_piece(10, name, pieces[piece_type], (5, 5))


if __name__ == "__main__":
    main()
