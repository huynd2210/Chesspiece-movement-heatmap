#!/usr/bin/env python3
"""
Demo script for Chess Movement Heatmap Generator CLI
Shows various features and capabilities
"""

import subprocess
import time
import sys

def run_command(cmd):
    """Run a command and print output"""
    print(f"\n{'='*60}")
    print(f"$ {cmd}")
    print('='*60)
    subprocess.run(cmd, shell=True)
    time.sleep(1)  # Pause for readability

def main():
    print("CHESS MOVEMENT HEATMAP GENERATOR - DEMO")
    print("======================================\n")
    print("This demo will showcase various features of the CLI tool.")
    input("Press Enter to start...")

    # 1. Basic usage - Standard chess piece
    print("\n\n1. BASIC USAGE - Standard Chess Piece")
    print("-------------------------------------")
    run_command("python chess_heatmap_cli.py knight")
    
    # 2. Custom board size and position
    print("\n\n2. CUSTOM BOARD SIZE AND POSITION")
    print("---------------------------------")
    run_command("python chess_heatmap_cli.py queen --size 10 --position 2,7")
    
    # 3. Using chess notation
    print("\n\n3. CHESS NOTATION FOR POSITION")
    print("------------------------------")
    run_command("python chess_heatmap_cli.py bishop --position d4")
    
    # 4. Obstacles demonstration
    print("\n\n4. OBSTACLES DEMONSTRATION")
    print("-------------------------")
    run_command('python chess_heatmap_cli.py rook --obstacles "3,4;4,3;4,5;5,4"')
    
    # 5. Fairy chess piece
    print("\n\n5. FAIRY CHESS PIECE - Nightrider")
    print("---------------------------------")
    run_command("python chess_heatmap_cli.py nightrider --size 10")
    
    # 6. Shogi piece with asymmetric movement
    print("\n\n6. SHOGI PIECE - Gold General")
    print("-----------------------------")
    run_command("python chess_heatmap_cli.py \"gold general\"")
    
    # 7. Complex fairy piece
    print("\n\n7. COMPLEX FAIRY PIECE - Flying Ox")
    print("----------------------------------")
    run_command("python chess_heatmap_cli.py \"flying ox\" --size 12 --position 6,6")
    
    # 8. Search functionality
    print("\n\n8. SEARCH FUNCTIONALITY")
    print("----------------------")
    run_command("python chess_heatmap_cli.py --search dragon")
    
    # 9. Piece information
    print("\n\n9. DETAILED PIECE INFORMATION")
    print("-----------------------------")
    run_command("python chess_heatmap_cli.py \"drunk elephant\" --info")
    
    # 10. List pieces by category
    print("\n\n10. LIST PIECES BY CATEGORY")
    print("---------------------------")
    run_command("python chess_heatmap_cli.py --list shogi")
    
    # 11. Unique piece - Goose
    print("\n\n11. UNIQUE PIECE - Goose (from Tori Shogi)")
    print("------------------------------------------")
    run_command("python chess_heatmap_cli.py goose")
    
    # 12. Limited movement piece
    print("\n\n12. LIMITED MOVEMENT - Pawn")
    print("---------------------------")
    run_command("python chess_heatmap_cli.py pawn --position 1,4")
    
    # 13. Complex scenario with obstacles
    print("\n\n13. COMPLEX SCENARIO - Knight with maze")
    print("---------------------------------------")
    run_command('python chess_heatmap_cli.py knight --size 10 --position 0,0 --obstacles "2,1;1,2;3,3;4,4;5,5;6,6;7,7"')
    
    # 14. Asymmetric piece
    print("\n\n14. ASYMMETRIC MOVEMENT - Howling Dog")
    print("-------------------------------------")
    run_command("python chess_heatmap_cli.py \"howling dog\" --position 7,4")
    
    print("\n\nDEMO COMPLETE!")
    print("=============")
    print("\nThe Chess Movement Heatmap Generator supports:")
    print("- 180+ pieces from various chess variants")
    print("- Obstacle handling")
    print("- Custom board sizes")
    print("- Chess notation")
    print("- Search and information commands")
    print("\nExplore more pieces with: python chess_heatmap_cli.py --list")

if __name__ == "__main__":
    main()
