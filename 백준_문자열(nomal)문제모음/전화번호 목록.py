import sys
import collections
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.children:
            return True
        else:
            return False


t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    nums_Trie = Trie()
    nums_list = []
    check = True # 접두어인 경우가 없음
    for j in range(n):
        num = sys.stdin.readline().rstrip()
        nums_Trie.insert(num)
        nums_list.append(num)

    nums_list.sort(key=len)
    for num in nums_list:
        if nums_Trie.startsWith(num):
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")



# 1차 시도 시간초과
# import sys

# t = int(sys.stdin.readline())
# for i in range(t):
#     n = int(sys.stdin.readline())
#     phone_nums = []
#     check = True
#     for j in range(n):
#         phone_nums.append(sys.stdin.readline().rstrip())
#     #phone_nums.sort(key=len)

#     for k in range(len(phone_nums)):
#         start_num = phone_nums[k]
#         for num in phone_nums[k+1:]:
#             # print(start_num)
#             # print(num)
#             if len(start_num) < len(num):
#                 if num.startswith(start_num):
#                     check = False
#                     break
#         if check == False:
#             break
#     if check:
#         print("YES")
#     else:
#         print("NO")
        
    
