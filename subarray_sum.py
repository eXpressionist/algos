def subSum(nums, k):
    '''
    Функция находит количество подмассивов в массиве nums, которые дают в сумме число k
    '''
    answer = 0
    subarray_sum = 0
    prefix_sum_count = {0: 1} #hashmap, задаем изначально 0-1 для случая, если указанная сумма будет состоять из всего массива
    for i in range(len(nums)):
        subarray_sum += nums[i]  #подсчитываем подряд сумму подмассива
        to_remove = subarray_sum - k  #вычитаем из этой суммы число k на текущем этапе, чтобы понять, какую часто отрезать
        answer += prefix_sum_count.get(to_remove, 0) #обращаемся к hashmap, если не нашли, что можно "отрезать" то получаем 0
        prev_count = prefix_sum_count.get(subarray_sum, 0) #забираем из hashmap предыдущую сумму подмассива
        prefix_sum_count[subarray_sum] = prev_count + 1 #затем в hashmap кладем предыдущее значение +1 (если первый раз, будет 1)

    return answer
