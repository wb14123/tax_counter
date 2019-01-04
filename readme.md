
# 2019 年个人所得税计算器

## 使用

```
python -i individual_income_cn_2019.py
```

其中有两个函数可以直接使用：

### 计算需要缴纳的个人所得税

```
def count_tax_2019(monthly_salary, bonus, deduction):
    """
    计算个人所得税
    :param monthly_salary: 月薪
    :param bonus: 年终奖
    :param deduction: 每月专项扣除
    :return: 全年需要缴纳的个人所得税
    """
```

### 根据年薪计算最优的年终奖方案使得缴纳的个人所得税最少

```
def min_tax_2019(year_salary, monthly_deduction):
    """
    计算最优的年终奖方案
    :param year_salary: 年薪
    :param monthly_deduction: 每月专项扣除
    :return: (全年需要缴纳的个人所得税, 月薪, 年终奖)
    """
```

## 图表

根据年薪的年终奖优化方案：



## TODO

* 扣除五险一金
