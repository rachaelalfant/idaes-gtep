import json

start_date = "01-01"

with open(f"power_flows/power_flows_{start_date}.json", "r") as power_flows_file:
    power_flows = json.load(power_flows_file)
with open(f"max_flows/max_flows_{start_date}.json", "r") as max_flows_file:
    max_flows = json.load(max_flows_file)

branch_names = [
    "branch_2_3",
    "branch_1_2",
    "branch_1_4",
    "branch_4_10",
    "branch_1_10",
    "branch_3_4_0",
    "branch_3_4_1",
]

day = 0
average_congestion = {}  # stores (per-line) average hourly congestion on each day
# total_congestion = {}   # stores total load shed on each day
while day < 7:
    one_day = {}
    for i in range(24 * day + 1, 24 * day + 25):  # AVERAGE PER-LINE CONGESTION:
        one_day[i] = (
            sum(
                abs(
                    power_flows[
                        f"investmentStage[1].representativePeriod[1].commitmentPeriod[{i}].dispatchPeriod[1].powerFlow.{branch_name}"
                    ]
                )
                / max_flows[
                    f"investmentStage[1].representativePeriod[1].commitmentPeriod[{i}].dispatchPeriod[1].powerFlow.{branch_name}"
                ]
                for branch_name in branch_names
            )
        ) / len(branch_names)
    # total_congestion[day] = sum(one_day.values())
    average_congestion[day] = sum(one_day.values()) * (1 / 24)
    day += 1

print(
    f"highest_ave_congestion day is {max(average_congestion, key=average_congestion.get)}:",
    max(average_congestion.values()),
)
# print(f"highest_total_congestion day is {max(total_congestion, key=total_congestion.get)}", max(total_congestion.values()))

'''
    retain raw info here too

    what's happening w/ distribution of vals
    visualize patters: are there lines that are constantly under-utilized/congested? 
'''
