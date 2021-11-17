import statistics

# Number of words per title for old vs. new
old_list = [4, 7, 4, 5, 7, 4, 5, 4, 6, 7, 6, 6, 6, 3, 7, 3, 3, 5]
new_list = [4, 3, 3, 3, 3, 4, 3, 5, 4, 4, 3, 5, 4, 4, 4, 3, 3, 5, 4, 3, 6]

# sort lists from least to greatest
old_list.sort()
new_list.sort()

# print sorted lists
print("Old List Lengths: " + str(old_list))
print("New List Lengths: " + str(new_list))

# calculate totals for both lists
old_total = 0
new_total = 0
for x in old_list:
    old_total += x
for y in new_list:
    new_total += y
print("Old Total: " + str(old_total))
print("New Total: " + str(new_total))

# calculate averages for old list
old_mean = statistics.mean(old_list)
print("Old Mean: \n" + str(old_mean))
old_median = statistics.median(old_list)
print("Old Median: \n" + str(old_median))
old_mode = statistics.mode(old_list)
print("Old Mode: \n" + str(old_mode))

# calculate averages for new list
new_mean = statistics.mean(new_list)
print("New Mean: \n" + str(new_mean))
new_median = statistics.median(new_list)
print("New Median: \n" + str(new_median))
new_mode = statistics.mode(new_list)
print("New Mode: \n" + str(new_mode))