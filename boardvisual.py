def visualize_board():
    for i in range(10, 0, -1):  # Rows
        for j in range(1, 11):   # Columns
            if i % 2 == 1:
                tile_num = (i - 1) * 10 + j
            else:
                tile_num = (i - 1) * 10 + (11 - j)

            if tile_num == player_1_location:
                print("P1", end="\t")
            elif tile_num == player_2_location:
                print("P2", end="\t")
            else:
                print(tile_num, end="\t")
                
    print("\n")