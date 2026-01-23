def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    两数之和（哈希表优化版）
    :param numbers: 整数数组（无重复元素）
    :param target: 目标和
    :return: 满足条件的两个数的索引列表，无则返回空列表
    """
    # 哈希表存储「数值: 索引」，空间换时间，时间复杂度 O(n)
    num_index_map = {}
    for index, num in enumerate(numbers):
        complement = target - num
        # 检查补数是否已在哈希表中
        if complement in num_index_map:
            return [num_index_map[complement], index]
        # 未找到则将当前数存入哈希表
        num_index_map[num] = index
    return []

# 清晰的测试用例 + 断言验证（确保代码正确性）
def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0, 1], "测试用例1失败"
    assert two_sum([3,2,4], 6) == [1, 2], "测试用例2失败"
    assert two_sum([3,3], 6) == [0, 1], "测试用例3失败"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_two_sum()