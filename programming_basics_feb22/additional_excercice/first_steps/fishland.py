skumria_cenakg = float(input())
caca_cenakg = float(input())
palamud_weight = float(input())
safrid_weight = float(input())
midi_weight = int(input())

price_palamud = skumria_cenakg * 0.6  + skumria_cenakg
total_price_palamud = price_palamud * palamud_weight

price_safrid = caca_cenakg * 0.8 + caca_cenakg
total_price_safrid = price_safrid * safrid_weight

price_midi = midi_weight * 7.5

total = price_midi + total_price_safrid + total_price_palamud


formatted_total = "{:.2f}".format(total)

print(formatted_total)
