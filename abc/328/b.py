N = int(input())

month_list = list(map(int, input().split()))

total = 0
for each_month, each_day in enumerate(month_list):
    each_month += 1
    # 1月1日, 1月11日
    day = each_month
    if each_month >= 10:
        ichi = int(str(each_month)[0])
        month = 0
        for num in range(len(str(each_month))):
            month += ichi * 10 ** num
        if each_month != month:
            continue
    
        day = ichi
    while day <= each_day:
        total += 1
        # print(f'{each_month}/{day}')
        day = day * 10 + day
        
print(total)