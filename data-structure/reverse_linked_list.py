class ListNode:
    """链表节点类（增加文档字符串）"""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"

def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    反转单链表（迭代法）
    :param head: 链表头节点（可能为None）
    :return: 反转后的链表头节点
    """
    if not head or not head.next:
        return head

    prev_node = None
    curr_node = head
    
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    
    return prev_node

def test_reverse_list():
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    reversed_head = reverse_list(node1)
    assert str(reversed_head) == "3 -> 2 -> 1", "测试用例1失败"
    assert reverse_list(None) is None, "测试用例2失败"
    assert str(reverse_list(ListNode(5))) == "5", "测试用例3失败"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_reverse_list()