# Problem 2276: Count Integers in Intervals
# https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals:

    def __init__(self):
        self.intervalList = []
        self.countNum = 0

    def add(self, left: int, right: int) -> None:
        # 如果目前陣列是空的 或 要加入的區間大於現在最後的, 就直接加在後面
        if self.intervalList == [] or self.intervalList[-1][1] < left - 1:
            self.intervalList.append([left, right])
            self.countNum += right - left + 1
        # 加入的區間緊接在現在最後的, 就更新最後一個區間的右端點
        elif self.intervalList[-1][1] == left - 1:
            self.intervalList[-1][1] = right
            self.countNum += right - left + 1
        else:
            # 其餘的照順序檢查加入, i 代表第幾個區間組
            i = 0

            # 跑迴圈直到 i 超過目前有的區間組數, 先只檢查區間組頭
            while i < len(self.intervalList):
                # 如果目前要加入的區間大於或緊接在這個區間的頭, 就 i + 1 去檢查下一個
                if left >= self.intervalList[i][0]:
                    i += 1
                # 小於則 insert區間
                else:
                    self.intervalList.insert(i, [left, right])
                    self.countNum += right - left + 1
                    break
            # 如果 i 跑到最後, 就加在最後一個
            if i == len(self.intervalList):
                self.intervalList.append([left, right])
                self.countNum += right - left + 1
                i -= 1
            
            # i - 1 才會是加入的前一個區間組位置, 避免 i 跑到頭以前所以至少要是 0
            i -= 1
            i = max(i, 0)
            # 跑迴圈直到 i 超過目前有的區間組數 - 1, 檢查區間尾, 如果在最後就已在前面的 if 和 elif 修正, 所以不用檢查最後一個
            while i < len(self.intervalList) - 1:
                # 如果這個區間尾大於等於下一個區間頭 - 1, 就合併兩個區間
                if self.intervalList[i][1] >= self.intervalList[i+1][0] - 1:
                    self.countNum -= (self.intervalList[i+1][1] - self.intervalList[i+1][0] + 1)
                    self.countNum -= (self.intervalList[i][1] - self.intervalList[i][0]+1)
                    self.intervalList[i][1] = max(self.intervalList[i][1], self.intervalList[i+1][1])
                    self.countNum += self.intervalList[i][1] - self.intervalList[i][0] + 1
                    del (self.intervalList[i+1])
                # 沒有問題就持續 - 1 檢查到最後
                else:
                    i += 1
        
    def count(self) -> int:
        return self.countNum

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()