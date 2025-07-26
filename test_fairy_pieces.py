from heatmap import generate_heatmap, print_heatmap
from fairy_chess_pieces import fairy_chess_pieces

def test_fairy_piece(piece_name, board_size=10, start_pos=None):
    """Test a fairy chess piece and display its movement heatmap."""
    if start_pos is None:
        start_pos = (board_size // 2, board_size // 2)
    
    if piece_name not in fairy_chess_pieces:
        print(f"Piece '{piece_name}' not found!")
        return
    
    # Create board
    grid = [[0] * board_size for _ in range(board_size)]
    
    # Get piece movements
    movements = fairy_chess_pieces[piece_name]
    
    # Generate heatmap
    heatmap = generate_heatmap(grid, movements, start_pos)
    
    print(f"\n{piece_name.upper()} - Starting from position {start_pos}")
    print("=" * (len(piece_name) + 30))
    print_heatmap(heatmap)
    print(f"Movement pattern has {len(movements)} possible moves")

# Test some interesting fairy chess pieces
if __name__ == "__main__":
    print("FAIRY CHESS PIECES DEMONSTRATION")
    print("================================\n")
    
    # Test some unique pieces
    test_pieces = [
        ("Drunk Elephant", 8),      # Moves in all directions except backward
        ("Flying Cat", 10),         # Leaps 3 squares in certain directions
        ("Hook Mover", 10),        # Double rook move
        ("Mountain Witch", 10),     # Steps forward, slides backward/diagonally
        ("Lion Dog", 8),           # Steps 1-3 squares in any direction
        ("Goose", 8),              # Forward alfil, backward dabbaba
        ("Gold General", 8),       # Classic shogi piece
        ("Phoenix", 8),            # Jumps diagonally
        ("Wizard Stork", 10),      # Steps backward, slides forward/diagonally
    ]
    
    for piece_name, board_size in test_pieces:
        test_fairy_piece(piece_name, board_size)
    
    # Test some special movement patterns
    print("\n\nSPECIAL MOVEMENT PATTERNS")
    print("=========================")
    
    # Asymmetric pieces
    print("\nAsymmetric Movement Examples:")
    test_fairy_piece("Howling Dog", 8, (7, 4))  # Moves differently forward vs backward
    test_fairy_piece("Left General", 8)         # Cannot move left
    test_fairy_piece("Right General", 8)        # Cannot move right
    
    # Limited range pieces
    print("\nLimited Range Examples:")
    test_fairy_piece("Leopard King", 12)        # Moves up to 5 squares
    test_fairy_piece("Guardian of the Gods", 10) # Moves 1-3 squares orthogonally
    
    # Jumping pieces
    print("\nJumping Pieces:")
    test_fairy_piece("Kylin", 8)               # Jumps to 2nd square orthogonally
    test_fairy_piece("Heavenly Knight", 8)      # Limited knight moves
