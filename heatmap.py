from collections import deque
from typing import List, Tuple

def generate_heatmap(grid: List[List[int]], piece_movements: List[Tuple[int, int]], start_coord: Tuple[int, int]) -> List[List[int]]:
    """
    Generate a heatmap showing the minimum number of moves required to reach each cell
    from the starting coordinate using the given piece's movement set.
    
    Args:
        grid: NxM grid (list of lists)
        piece_movements: List of (row_offset, col_offset) tuples representing valid moves
        start_coord: Starting position as (row, col) tuple
        
    Returns:
        Heatmap where each cell contains the minimum moves to reach it (-1 if unreachable)
    """
    rows, cols = len(grid), len(grid[0])
    heatmap = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start_coord[0], start_coord[1], 0)])  # (row, col, distance)
    heatmap[start_coord[0]][start_coord[1]] = 0
    
    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in piece_movements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and heatmap[nx][ny] == -1:
                heatmap[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    
    return heatmap


def print_heatmap(heatmap: List[List[int]], width: int = 3) -> None:
    """Pretty print the heatmap with aligned columns."""
    for row in heatmap:
        print(" ".join(f"{cell:>{width}}" if cell != -1 else f"{'-':>{width}}" for cell in row))


# Example usage with different pieces
if __name__ == "__main__":
    # Create an 8x8 grid
    grid = [[0] * 8 for _ in range(8)]
    
    # Define movement patterns for different pieces
    pieces = {
        "knight": [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)],
        "king": [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
        "rook": [(i, 0) for i in range(-7, 8) if i != 0] + [(0, i) for i in range(-7, 8) if i != 0],
        "bishop": [(i, i) for i in range(-7, 8) if i != 0] + [(i, -i) for i in range(-7, 8) if i != 0]
    }
    
    # Generate heatmap for a knight starting at (3, 3)
    print("Knight movement heatmap from position (3, 3):")
    knight_heatmap = generate_heatmap(grid, pieces["knight"], (3, 3))
    print_heatmap(knight_heatmap)
    
    print("\nKing movement heatmap from position (4, 4):")
    king_heatmap = generate_heatmap(grid, pieces["king"], (4, 4))
    print_heatmap(king_heatmap)

