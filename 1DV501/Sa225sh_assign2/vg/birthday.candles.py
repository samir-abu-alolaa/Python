def birthday_candles():
    boxes_tot = 0
    candles_per_box = 24
    candles_left = 0

    for year in range(1, 101):
        boxes_needed = 0
        if year < candles_per_box:
            if candles_left == 0:
                boxes_needed += 1
                boxes_tot += boxes_needed
                candles_left = 24
            candles_left -= year

        else:
            cand_needed = year
            cand_needed -= candles_left
            boxes_needed = (cand_needed // 24) + 1
            boxes_tot += boxes_needed
            candles_left = 24
            candles_left -= (cand_needed % 24)

        print(f"befor birthday {year}, need to buy{boxes_needed}, candles\
remening {candles_left}")
    print(f"{boxes_tot}, {candles_left}")


birthday_candles()
