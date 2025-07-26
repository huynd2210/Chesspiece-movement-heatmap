import unittest
from heatmap import generate_heatmap, print_heatmap

class TestHeatmapGenerator(unittest.TestCase):
    
    def test_knight_corner(self):
        """Test knight movement from corner position"""
        grid = [[0] * 8 for _ in range(8)]
        knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        heatmap = generate_heatmap(grid, knight_moves, (0, 0))
        
        # Check specific distances
        self.assertEqual(heatmap[0][0], 0)  # Starting position
        self.assertEqual(heatmap[1][2], 1)  # One knight move away
        self.assertEqual(heatmap[2][1], 1)  # One knight move away
        self.assertEqual(heatmap[0][1], 3)  # Takes 3 moves
        
    def test_king_center(self):
        """Test king movement from center position"""
        grid = [[0] * 5 for _ in range(5)]
        king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        heatmap = generate_heatmap(grid, king_moves, (2, 2))
        
        # Check Manhattan distance pattern
        self.assertEqual(heatmap[2][2], 0)  # Center
        self.assertEqual(heatmap[1][1], 1)  # Adjacent diagonal
        self.assertEqual(heatmap[0][0], 2)  # Corner
        self.assertEqual(heatmap[4][4], 2)  # Opposite corner
        
    def test_custom_piece(self):
        """Test custom piece with specific movement pattern"""
        grid = [[0] * 6 for _ in range(6)]
        # Custom piece that moves like a "plus sign" - 2 squares orthogonally
        custom_moves = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        heatmap = generate_heatmap(grid, custom_moves, (3, 3))
        
        self.assertEqual(heatmap[3][3], 0)  # Start
        self.assertEqual(heatmap[3][1], 1)  # 2 left
        self.assertEqual(heatmap[1][3], 1)  # 2 up
        self.assertEqual(heatmap[3][5], 1)  # 2 right
        self.assertEqual(heatmap[5][3], 1)  # 2 down
        self.assertEqual(heatmap[1][1], 2)  # Diagonal requires 2 moves
        
    def test_unreachable_cells(self):
        """Test piece that cannot reach certain cells"""
        grid = [[0] * 4 for _ in range(4)]
        # Piece that only moves diagonally by 2
        diagonal_moves = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
        heatmap = generate_heatmap(grid, diagonal_moves, (0, 0))
        
        # Check unreachable cells
        self.assertEqual(heatmap[0][1], -1)  # Cannot reach
        self.assertEqual(heatmap[1][0], -1)  # Cannot reach
        self.assertEqual(heatmap[2][2], 1)   # Can reach in 1 move
        
    def test_small_grid(self):
        """Test on very small grid"""
        grid = [[0] * 3 for _ in range(3)]
        # Simple orthogonal movement
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heatmap = generate_heatmap(grid, moves, (1, 1))
        
        expected = [
            [2, 1, 2],
            [1, 0, 1],
            [2, 1, 2]
        ]
        self.assertEqual(heatmap, expected)
        
    def test_rook_movement(self):
        """Test rook-like movement"""
        grid = [[0] * 5 for _ in range(5)]
        # Simplified rook (moves 1-2 squares orthogonally)
        rook_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                      (0, 2), (0, -2), (2, 0), (-2, 0)]
        heatmap = generate_heatmap(grid, rook_moves, (2, 2))
        
        # All cells should be reachable
        for row in heatmap:
            for cell in row:
                self.assertNotEqual(cell, -1)
                
        # Check specific distances
        self.assertEqual(heatmap[2][0], 1)  # 2 left
        self.assertEqual(heatmap[0][2], 1)  # 2 up
        self.assertEqual(heatmap[1][1], 2)  # Diagonal


def run_visual_tests():
    """Run visual tests to see the heatmaps"""
    print("=== Visual Test Results ===\n")
    
    # Test 1: L-shaped piece (similar to knight but different)
    print("1. L-shaped piece (3-1 movement):")
    grid = [[0] * 8 for _ in range(8)]
    l_piece = [(3, 1), (3, -1), (-3, 1), (-3, -1), (1, 3), (-1, 3), (1, -3), (-1, -3)]
    heatmap = generate_heatmap(grid, l_piece, (4, 4))
    print_heatmap(heatmap)
    
    # Test 2: Asymmetric piece
    print("\n2. Asymmetric piece (only moves forward/right):")
    grid = [[0] * 6 for _ in range(6)]
    asymmetric = [(0, 1), (1, 0), (1, 1)]  # Right, down, diagonal down-right
    heatmap = generate_heatmap(grid, asymmetric, (0, 0))
    print_heatmap(heatmap)
    
    # Test 3: Teleporting piece
    print("\n3. 'Teleporting' piece (jumps to corners):")
    grid = [[0] * 5 for _ in range(5)]
    teleport = [(4, 4), (4, -4), (-4, 4), (-4, -4)]  # Jump to corners from center
    heatmap = generate_heatmap(grid, teleport, (2, 2))
    print_heatmap(heatmap)


if __name__ == "__main__":
    # Run unit tests
    print("Running unit tests...")
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "="*50 + "\n")
    
    # Run visual tests
    run_visual_tests()
