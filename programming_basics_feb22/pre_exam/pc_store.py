price_processor = float(input())
price_gfx = float(input())
price_ram = float(input())
number_of_ram = int(input())
discount = float(input())

processor_lv = price_processor * 1.57
processor_lv -= processor_lv * discount
gfx_lv = price_gfx * 1.57
gfx_lv -= gfx_lv * discount
ram_lv = price_ram * 1.57
totla_ram = ram_lv * number_of_ram
total_leva = processor_lv + gfx_lv + totla_ram

print(f'Money needed - {total_leva:.2f} leva.')