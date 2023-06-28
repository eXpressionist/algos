def subSum(nums, k):
    answer = 0
    subarray_sum = 0
    prefix_sum_count = {0: 1}
    for i in range(len(nums)):
        subarray_sum += nums[i]
        to_remove = subarray_sum - k
        answer += prefix_sum_count.get(to_remove, 0)
        prev_count = prefix_sum_count.get(subarray_sum, 0)
        prefix_sum_count[subarray_sum] = prev_count + 1

    return answer
