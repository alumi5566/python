# Best for input array which we know the range of number
# Best for the element is balance distributed
# https://rust-algo.club/sorting/bucket_sort/index.html

# Assume we know the range of the input element is [0:100]
# Set 10 bucket, each cover 10 integers
def bucketSort(input):
    ret = []
    bins = [[] for i in range(10)]
    # bins[0].append(55)
    for i in input:
        bins[int(i/10)].append(i)
    print(bins)
    for b in bins:
        ret.extend(sorted(b))
    return ret

input = [6, 28, 96, 14, 74, 37, 9, 71, 91, 36]
print(bucketSort(input))