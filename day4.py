import re
from datetime import datetime

"""
i am not happy about this abomination of a solution :(
"""

# test = """
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up
# """
# input = test.strip().split("\n")

# open the input file
filename = "day4_input.txt"
input = open(filename).read().split("\n")

data = []
guard_sleeping = {}
slepping_minutes = [0 for x in range(60)]
print(slepping_minutes)

for line in input:
    temp = re.split(r"^\[(\d*-\d*-\d*\s\d*\:\d*)]\s(.*)", line)
    date_obj = datetime.strptime(temp[1], "%Y-%m-%d %H:%M")
    minute = int(date_obj.strftime("%M"))
    date = date_obj.strftime("%Y-%m-%d")

    guard = None
    guard_pattern = re.compile("Guard.*")
    # if ( (temp[2] != 'falls asleep') or (temp[2] != 'wakes up') ):
    if guard_pattern.match(temp[2]):
        action = None
        result = re.split(r"Guard\s#(\d*).*", temp[2])
        guard = int(result[1])

    else:
        action = temp[2]

    data.append({"timestamp": temp[1], "action": action, "date": date, "minute": minute, "guard": guard})

# sort the list
sorted_data = sorted(data, key=lambda k: k['timestamp'])

guards_total_sleeping = {}
asleep_at = 0
guard = None
for item in sorted_data:
    if item['guard'] != None:
        guard = item['guard']
    if item['action'] == 'falls asleep':
        asleep_at = item['minute']
    if item['action'] == 'wakes up':
        if guard in guards_total_sleeping:
            print('guard in the dict')
            for i in range(asleep_at, (item['minute'] - asleep_at) + asleep_at):
                guards_total_sleeping[guard][i] = guards_total_sleeping[guard][i] + 1

        else:
            slepping_minutes = [0 for x in range(60)]
            for i in range(asleep_at, (item['minute'] - asleep_at) + asleep_at):
                slepping_minutes[i] = slepping_minutes[i] + 1
            guards_total_sleeping[guard] = slepping_minutes
        print("date: {}    guard: {}    asleep_for: {}".format(item['date'], guard, item['minute'] - asleep_at))

max_guard_total = {'guard_id': 0, 'total': 0}
for key, value in guards_total_sleeping.items():
    print(key, end=': ')
    sum_sleeping = sum(i for i in value)
    if sum_sleeping > max_guard_total['total']:
        max_guard_total['guard_id'] = key
        max_guard_total['total'] = sum_sleeping

    print(sum_sleeping , end='  ')
    for i in range(len(value)):
        print(value[i], end = '')
    print()

print(max_guard_total)

max_guard_id = max_guard_total['guard_id']

# find max overlap
max_overlap_min = 0
max_overlap_min_index = 0
for i in range(len(guards_total_sleeping[max_guard_id])):
    # print(guards_total_sleeping[max_guard_id][i])
    if guards_total_sleeping[max_guard_id][i] > max_overlap_min:
        max_overlap_min = guards_total_sleeping[max_guard_id][i]
        max_overlap_min_index = i

print(max_overlap_min_index * max_guard_id)


# part 2
"""
Strategy 2: Of all guards, which guard is most frequently asleep on the same
minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard
or minute - three times in total. (In all other cases, any guard spent any
minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In
the above example, the answer would be 99 * 45 = 4455.)
"""

print("part 2")

max_guard_key = 0
max_overlap_minute_key = 0
max_overlap = 0

for key, value in guards_total_sleeping.items():
    for i in range(len(guards_total_sleeping[key])):
        if guards_total_sleeping[key][i] > max_overlap:
            max_overlap = guards_total_sleeping[key][i]
            max_guard_key = key
            max_overlap_minute_key = i

print("max_overlap: {}  max_guard_key: {}   max_overlap_minute_key: {}".format(max_overlap, max_guard_key, max_overlap_minute_key))

print("max_guard_key * max_overlap_minute_key: {}".format(max_guard_key * max_overlap_minute_key))

