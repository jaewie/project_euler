n = int(raw_input())
ppl = [raw_input().split() for _ in range(n)]

most_pairs = male_guests = female_guests = 0

events = [dict(begin_male=0, begin_female=0, end_male=0, end_female=0) for _ in range(367)]

for gender, begin, end in ppl:
    begin, end = int(begin), int(end)

    if gender == 'M':
        events[begin]['begin_male'] += 1
        events[end]['end_male'] += 1
    else:
        events[begin]['begin_female'] += 1
        events[end]['end_female'] += 1


for event in events:
    male_guests += event['begin_male']
    female_guests += event['begin_female']
    most_pairs = max(most_pairs, min(male_guests, female_guests))

    male_guests -= event['end_male']
    female_guests -= event['end_female']


print most_pairs * 2
