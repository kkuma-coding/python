arr = [1, 2, 4, 7, 8]
presum = [0]
for i in range(len(arr)):
    presum.append(presum[i]+arr[i])

print (*presum)