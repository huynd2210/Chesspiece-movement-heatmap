from fairy_chess_pieces import fairy_chess_pieces

# List of all 154 pieces from the original description
all_pieces = [
    "Angry-Boar",
    "Angry-Boar-Taikyoku",
    "Bat",
    "Bears-Eyes",
    "Bishop",
    "Blind-Bear",
    "Blind-Monkey",
    "Blind-Tiger",
    "Blue-Dragon",
    "Buddhist-Devil",
    "Cavalryman",
    "Capricorn",
    "Captive-Officer",
    "Cat-Sword",
    "Ceramic-Dove",
    "Chinese-Cock",
    "Cloud-Dragon",
    "Cloud-Eagle",
    "Cloud-Eagle-Taikyoku",
    "Coiled-Serpent",
    "Copper-General",
    "Crown-Prince",
    "Dark-Spirit",
    "Deva",
    "Donkey",
    "Dove",
    "Dragon-Horse",
    "Dragon-King",
    "Drunk-Elephant",
    "Eagle",
    "Earth-General",
    "East-Barbarian",
    "Enchanted-Badger",
    "Enchanted-Fox",
    "Evil-Wolf",
    "Ferocious-Leopard",
    "Fierce-Eagle",
    "Fire-Dragon",
    "Fire-General",
    "Flying-Cat",
    "Flying-Cock",
    "Flying-Dragon",
    "Flying-Dragon-Taikyoku",
    "Flying-Horse",
    "Flying-Ox",
    "Flying-Stag",
    "Flying-Swallow",
    "Forest-Demon",
    "Fragrant-Elephant",
    "Free-Boar",
    "Free-Copper",
    "Free-Demon",
    "Free-Dream-Eater",
    "Free-Earth",
    "Free-Gold",
    "Free-Iron",
    "Free-King",
    "Free-Silver",
    "Free-Stone",
    "Free-Tile",
    "Furious-Fiend",
    "Go-Between",
    "Gold-Chariot",
    "Golden-Bird",
    "Golden-Deer",
    "Gold-General",
    "Goose",
    "Great-Dove",
    "Great-Dragon",
    "Great-Dragon-Tai",
    "Great-Dream-Eater",
    "Great-Elephant",
    "Guardian-of-the-Gods",
    "Guardian-of-the-Gods-Taikyoku",
    "Heavenly-Knight",
    "Heavenly-Tetrarch-Taikyoku",
    "Hook-Mover",
    "Horned-Falcon",
    "Howling-Dog",
    "Iron-General",
    "Keima",
    "King",
    "Kirin-Master",
    "Kylin",
    "Lance",
    "Left-Chariot",
    "Left-General",
    "Leopard-King",
    "Lion",
    "Lion-Dog",
    "Long-Nosed-Goblin",
    "Mountain-Dove",
    "Mountain-General",
    "Mountain-Witch",
    "Multi-General",
    "Neighbouring-King",
    "North-Barbarian",
    "Old-Kite",
    "Old-Kite-Hawk",
    "Old-Monkey",
    "Old-Rat",
    "Pawn",
    "Phoenix",
    "Phoenix-Master",
    "Poison-Snake",
    "Prancing-Stag",
    "Racing-Chariot",
    "Rain-Dragon",
    "Ramshead-Soldier",
    "Ramshead-Soldier-Taikyoku",
    "Reclining-Dragon",
    "Reverse-Chariot",
    "Right-Chariot",
    "Right-General",
    "Rook",
    "Running-Wolf",
    "Rushing-Bird",
    "Savage-Tiger",
    "She-Devil",
    "Side-Dragon",
    "Side-Dragon-Taikyoku",
    "Side-Mover",
    "Side-Mover-Heian-dai",
    "Side-Serpent",
    "Side-Soldier",
    "Silver-Chariot",
    "Silver-General",
    "Silver-Hare",
    "Soaring-Eagle",
    "South-Barbarian",
    "Square-Mover",
    "Standard-Bearer",
    "Stone-General",
    "Strutting-Crow",
    "Tile-General",
    "Tokin",
    "Treacherous-Fox",
    "Vertical-Mover",
    "Vertical-Soldier",
    "Violent-Bear",
    "Violent-Ox",
    "Water-Buffalo",
    "Water-Dragon",
    "Water-General",
    "West-Barbarian",
    "Whale",
    "White-Elephant",
    "White-Elephant-Taikyoku",
    "White-Horse",
    "White-Tiger",
    "Wind-Dragon",
    "Wizard-Stork",
    "Wood-General",
    "Wrestler",
    "Wrestler-Taikyoku",
    "Yaksha"
]

# Convert piece names to match the format in fairy_chess_pieces (replace hyphens with spaces)
def normalize_name(name):
    return name.replace("-", " ")

# Check implementation status
print("FAIRY CHESS PIECES VERIFICATION")
print("===============================\n")

implemented_count = 0
missing_pieces = []
implemented_pieces = list(fairy_chess_pieces.keys())

for piece in all_pieces:
    normalized_piece = normalize_name(piece)
    if normalized_piece in fairy_chess_pieces:
        implemented_count += 1
    else:
        missing_pieces.append(piece)

print(f"Total pieces in original list: {len(all_pieces)}")
print(f"Total pieces implemented: {len(implemented_pieces)}")
print(f"Pieces matched from original list: {implemented_count}")

if missing_pieces:
    print(f"\nMissing pieces ({len(missing_pieces)}):")
    for piece in missing_pieces:
        print(f"  - {piece}")
else:
    print("\n✓ All pieces from the original list are implemented!")

# Check for extra pieces (implemented but not in original list)
extra_pieces = []
for implemented in implemented_pieces:
    denormalized = implemented.replace(" ", "-")
    if denormalized not in all_pieces:
        extra_pieces.append(implemented)

if extra_pieces:
    print(f"\nExtra pieces not in original list ({len(extra_pieces)}):")
    for piece in extra_pieces:
        print(f"  + {piece}")

# Display some statistics
print("\n\nIMPLEMENTATION STATISTICS")
print("=========================")
print(f"Total unique movements: {sum(len(moves) for moves in fairy_chess_pieces.values())}")
print(f"Average moves per piece: {sum(len(moves) for moves in fairy_chess_pieces.values()) / len(fairy_chess_pieces):.1f}")

# Find pieces with most and least moves
max_moves_piece = max(fairy_chess_pieces.items(), key=lambda x: len(x[1]))
min_moves_piece = min(fairy_chess_pieces.items(), key=lambda x: len(x[1]))

print(f"\nPiece with most moves: {max_moves_piece[0]} ({len(max_moves_piece[1])} moves)")
print(f"Piece with least moves: {min_moves_piece[0]} ({len(min_moves_piece[1])} moves)")

# Verify specific complex pieces
print("\n\nCOMPLEX PIECES STATUS")
print("=====================")
complex_pieces = ["Lion", "Hook-Mover", "Capricorn", "Long-Nosed-Goblin", "Horned-Falcon", "Soaring-Eagle", "Furious-Fiend"]
for piece in complex_pieces:
    normalized = normalize_name(piece)
    if normalized in fairy_chess_pieces:
        print(f"✓ {piece}: Implemented (basic movement)")
    else:
        print(f"✗ {piece}: Missing")
