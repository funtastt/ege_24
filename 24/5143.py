result = []
with open('../24.txt') as file:
    for s in file:
        s = s.strip()
        nums = s.split('.')
        if nums[0] == '195' and nums[1].startswith('2') and len(nums[2]) > 0 and nums[3] == '14':
            if s not in result:
                result.append(s)
print(len(result))
