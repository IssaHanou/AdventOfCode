def day_1(file):
    total = 0
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open(file) as f:
        for line in f:
            nums = []
            for i in range(len(line)):
                try:
                    x = int(line[i])
                    nums.append(line[i])
                except: pass
                for k, d in enumerate(digits):
                    found = True
                    for j in range(len(d)):
                        if i + j >= len(line) or line[i + j] != d[j]:  
                            found = False
                    if found:
                        nums.append(str(k + 1))
            print(nums)
            total += int(nums[0] + nums[-1])
    print(total)
    
if __name__ == "__main__":
    day_1("day1.txt")