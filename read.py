data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('file read finish, total for', len(data))

# for average len of message
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('The average lenth of message is:', sum_len/len(data))

