import json

start_date = "01-01"

with open(f'load_shed/load_shed_{start_date}.json', 'r') as file:
    load_shed = json.load(file)

day = 0
average_load_shed = {} # stores average hourly load shed on each day
total_load_shed = {}   # stores total load shed on each day
while day < 7:
    one_day = {}
    for i in range(24*day + 1, 24*day + 25):
        one_day[i] = sum(load_shed[l] for l in load_shed.keys() if f'commitmentPeriod[{i}]' in l) # summing load shed from all buses
    total_load_shed[day] = sum(one_day.values())
    average_load_shed[day] = total_load_shed[day]*(1/24)
    day += 1

print(f"highest_ave_load_shed day is {max(average_load_shed, key=average_load_shed.get)}:", max(average_load_shed.values()))
print(f"highest_total_load_shed day is {max(total_load_shed, key=total_load_shed.get)}:", max(total_load_shed.values()))

'''
    I think we want to use average hourly load shed as our metric here?? or do we want to use average per-bus load shed???
    - how many extreme days to select? 
    - fork of gtep?

    % of day w/ load shed; choose day with largest % hours of load shed

    file that stores load shed for each day; retain raw info so that we can decide things later and not rerun everything
'''
