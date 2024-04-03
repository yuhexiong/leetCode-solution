# Problem 2879: Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows/

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # 使用 head 決定顯示前幾行
    return employees.head(3)