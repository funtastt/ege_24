lines = open('24.txt').readlines()
addresses = set()

for line in lines:
    nums = line.strip().split('.')
    if nums[0] == '195' and nums[3] == '14':
        if len(nums[1]) == 2 and len(nums[2]) >= 2:
            if nums[1].endswith('2') and nums[2].startswith('1') and nums[2].endswith('5'):
                addresses.add(line)

print(len(addresses))