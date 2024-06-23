# Problem 2884: Modify Columns
# https://leetcode.com/problems/modify-columns/

import pandas as pd


def modify_salary_column(employees: pd.DataFrame) -> pd.DataFrame:
    # 直接使用 df[column_name] 來修改一整條 column 資料
    employees['salary'] *= 2
    return employees
