loads = int(input())

bus = 0
truck = 0
train = 0
bus_tonnes = 0
truck_tonnes = 0
train_tonnes = 0


for i in range(loads):
    tonnes = int(input())
    if tonnes <= 3:
        bus += 1
        bus_tonnes += tonnes
    elif 4 <= tonnes <= 11:
        truck += 1
        truck_tonnes += tonnes
    else:
        train += 1
        train_tonnes += tonnes

total_tonnes = bus_tonnes + train_tonnes + truck_tonnes
print(f'{(bus_tonnes * 200 + truck_tonnes * 175 + train_tonnes * 120) / total_tonnes:.2f}')
print(f'{bus_tonnes/total_tonnes * 100:.2f}%')
print(f'{truck_tonnes/total_tonnes * 100:.2f}%')
print(f'{train_tonnes/total_tonnes * 100:.2f}%')