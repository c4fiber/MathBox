def flip(some_list):
    if len(some_list) <= 1:
        return some_list


some_list = [1, 2, 3, 4, 5]
temp_list = some_list[-1:] + some_list[1:-1] + some_list[:1]
print(temp_list)


start_peg = 1
end_peg = 3

mid_peg = [1, 2, 3]
mid_peg.remove(start_peg)
mid_peg.remove(end_peg)
print(mid_peg)
