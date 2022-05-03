bitcoins = int(input())
uans = float(input())
comission = float(input())

bitcoin_to_lv = 1168
uan_usd = 0.15
usd_lv = 1.76
eur_lv = 1.95

levs_from_bitcoins = bitcoins * bitcoin_to_lv
usd_from_uan = uans * uan_usd
levs_from_usd = usd_from_uan * usd_lv
total_bgn = levs_from_usd + levs_from_bitcoins
total_euro = total_bgn / eur_lv
total_comission = comission / 100 * total_euro
total_euro_after_comission = total_euro - total_comission
formatted_answer = "{:.2f}".format(total_euro_after_comission)

print (formatted_answer)