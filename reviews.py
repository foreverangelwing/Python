data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0:
           print(len(data)) 
# print(data[0])
# print('-----------------------------------')
# print(data[1])
# print('檔案讀取完了，共有', len(data), '筆資料')

# sum_len = 0
# for d in data:
#     # print(d)
#     sum_len = sum_len + len(d)
# print('平均留言長度', sum_len/len(data))
# print(sum_len)
# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有', len(new), '筆留言長度小於100')

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print(len(good))
# print(good[0])
# good = [d for d in data if 'good' in d] 
# print(good)
bad =['bad' in d for d in data]
print(bad)
print(bad[1000000])