result = set()
lines = open('24.txt').readlines()

for s in lines:
    s = s.strip()
    nums = s.split('.')
    if nums[0] == '195' and nums[3] == '14':
        if len(nums[1]) == 2 and len(nums[2]) == 3:
            if nums[1].startswith('2') and nums[2].startswith('1') and nums[2].endswith('5'):
                result.add(s)

print(len(result))
