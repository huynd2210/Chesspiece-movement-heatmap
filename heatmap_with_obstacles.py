from collections import deque
from typing import List, Tuple, Optional

def generate_heatmap_with_obstacles(
    grid: List[List[int]], 
    piece_movements: List[Tuple[int, int]], 
    start_coord: Tuple[int, int],
    obstacles: Optional[List[Tuple[int, int]]] = None
) -> List[List[int]]:
    """
    Generate a heatmap showing the minimum number of moves required to reach each cell
    from the starting coordinate using the given piece's movement set, with obstacles.
    
    Args:
        grid: NxM grid (list of lists)
        piece_movements: List of (row_offset, col_offset) tuples representing valid moves
        start_coord: Starting position as (row, col) tuple
        obstacles: Optional list of (row, col) tuples representing blocked cells
        
    Returns:
        Heatmap where each cell contains the minimum moves to reach it 
        (-1 if unreachable, -2 if obstacle)
    """
    rows, cols = len(grid), len(grid[0])
    heatmap = [[-1 for _ in range(cols)] for _ in range(rows)]
    
    # Mark obstacles
    if obstacles:
        for obs_row, obs_col in obstacles:
            if 0 <= obs_row < rows and 0 <= obs_col < cols:
                heatmap[obs_row][obs_col] = -2
    
    # Check if start position is valid
    if heatmap[start_coord[0]][start_coord[1]] == -2:
        raise ValueError("Starting position is on an obstacle!")
    
    queue = deque([(start_coord[0], start_coord[1], 0)])
    heatmap[start_coord[0]][start_coord[1]] = 0
    
    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in piece_movements:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and 
                heatmap[nx][ny] == -1):  # Not visited and not obstacle
                heatmap[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    
    return heatmap


def print_heatmap_with_obstacles(heatmap: List[List[int]], width: int = 3) -> None:
    """Pretty print the heatmap with obstacles marked as 'X'."""
    for row in heatmap:
        cells = []
        for cell in row:
            if cell == -2:
                cells.append(f"{'X':>{width}}")
            elif cell == -1:
                cells.append(f"{'-':>{width}}")
            else:
                cells.append(f"{cell:>{width}}")
        print(" ".join(cells))


def visualize_path(
    grid: List[List[int]], 
    piece_movements: List[Tuple[int, int]], 
    start: Tuple[int, int],
    target: Tuple[int, int],
    obstacles: Optional[List[Tuple[int, int]]] = None
) -> Optional[List[Tuple[int, int]]]:
    """
    Find and return the shortest path from start to target.
    
    Returns:
        List of coordinates representing the path, or None if no path exists
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    
    # Mark obstacles
    if obstacles:
        for obs_row, obs_col in obstacles:
            if 0 <= obs_row < rows and 0 <= obs_col < cols:
                visited[obs_row][obs_col] = True
    
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == target:
            # Reconstruct path
            path = []
            current = target
            while current is not None:
                path.append(current)
                if parent[current[0]][current[1]]:
                    current = parent[current[0]][current[1]]
                else:
                    break
            return path[::-1]
        
        for dx, dy in piece_movements:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and 
                not visited[nx][ny]):
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))
    
    return None


# Example usage
if __name__ == "__main__":
    # Create a 10x10 grid
    grid = [[0] * 10 for _ in range(10)]
    
    # Knight movements
    knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
                    (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    # Define some obstacles (walls)
    obstacles = [
        (2, 3), (2, 4), (2, 5), (2, 6),  # Horizontal wall
        (3, 6), (4, 6), (5, 6),          # Vertical wall
        (7, 2), (7, 3), (7, 4)           # Another wall
    ]
    
    start_pos = (0, 0)
    target_pos = (9, 9)
    
    print("Knight movement with obstacles:")
    print("Start: (0,0), Target: (9,9)")
    print("Obstacles marked with 'X'\\n")
    
    # Generate heatmap
    heatmap = generate_heatmap_with_obstacles(grid, knight_moves, start_pos, obstacles)
    print_heatmap_with_obstacles(heatmap)
    
    # Find path
    path = visualize_path(grid, knight_moves, start_pos, target_pos, obstacles)
    if path:
        print(f"\\nShortest path found! Length: {len(path) - 1} moves")
        print("Path:", " -> ".join(f"({r},{c})" for r, c in path))
    else:
        print("\\nNo path found!")
    
    # Test with a different piece - Bishop
    print("\\n" + "="*50 + "\\n")
    print("Bishop movement with same obstacles:")
    
    bishop_moves = [(i, i) for i in range(1, 10)] + \
                   [(i, -i) for i in range(1, 10)] + \
                   [(-i, i) for i in range(1, 10)] + \
                   [(-i, -i) for i in range(1, 10)]
    
    heatmap_bishop = generate_heatmap_with_obstacles(grid, bishop_moves, start_pos, obstacles)
    print_heatmap_with_obstacles(heatmap_bishop)
