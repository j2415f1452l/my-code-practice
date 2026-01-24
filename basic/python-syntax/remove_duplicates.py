def remove_duplicates(original_list: list) -> list:
    """
    列表去重（保留元素首次出现的顺序）
    :param original_list: 可能包含重复元素的列表
    :return: 去重后的新列表
    """
    return list(dict.fromkeys(original_list))

def test_remove_duplicates():
    assert remove_duplicates([1,2,2,3,3,3,4]) == [1,2,3,4], "测试用例1失败"
    assert remove_duplicates([]) == [], "测试用例2失败"
    assert remove_duplicates([5,5,5]) == [5], "测试用例3失败"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_remove_duplicates()