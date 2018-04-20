# import ipdb
def merge_ranges_print_statements(availability_list):
    availability_list = sorted(availability_list, key=lambda x: x[0])
    merged_ranges = [availability_list[0]]

    for current_start, current_end in availability_list:
        # if end time of previous tuple is the same as the
        # last element in merged list's end time, then skip
        previous = merged_ranges[-1]
        previous_start = previous[0]
        previous_end = previous[1]

        print(f'\ncurrent_start: {current_start}, current_end: {current_end}')
        print(f'previous_start: {previous_start}, previous_end: {previous_end}')

        # if end time of previous tuple is in the range of current tuple
        # merge
        # if (previous_end>=current_start and previous_end<=current_end) or
        if current_start <= previous_end <= current_end:
            merged_tuples = (previous_start, current_end)
            merged_ranges[-1] = merged_tuples
            print('statement 1')
            print(f'merged_tuples: {merged_tuples}, merged_ranges: {merged_ranges}')
        elif previous_start <= current_start <= previous_end:
            merged_tuples = (previous_start, previous_end)
            merged_ranges[-1] = merged_tuples
            print('statement 2')
            print(f'merged_tuples: {merged_tuples}, merged_ranges: {merged_ranges}')

        # elif end time of previous tuple is NOT in range of current tuple
        # continue
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges

def merge_ranges(availability_list):
    availability_list = sorted(availability_list, key=lambda x: x[0])
    merged_ranges = [availability_list[0]]

    for current_start, current_end in availability_list[1:]:
        previous = merged_ranges[-1]
        previous_start = previous[0]
        previous_end = previous[1]

        if current_start <= previous_end:
            merged_tuples = (previous_start, max(current_end, previous_end))
            merged_ranges[-1] = merged_tuples
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges


a = [(0,1),(3,5),(4,8),(10,12),(9,10)] # [(0,1),(3,8),(9,12)]
b = [(0,1),(3,5),(14,16),(4,8),(10,12),(9,10)] # [(0,1),(3,8),(9,12),(14,16)]
c = [(1,5),(2,3),(3,6)] # [(1,6)]
d = [(1,10),(2,6),(3,5),(7,9)] # [(1,10)]
e = [(1,10),(2,6),(3,5),(7,9),(21,25)] # [(1,10),(21,25)]
print(merge_ranges(e))
