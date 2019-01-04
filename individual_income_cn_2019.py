from dataclasses import dataclass
from typing import Optional, List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


@dataclass
class TaxRate:
    start: Optional[float]
    end: Optional[float]
    rate: float
    deduction: float


def count_social_insurance(monthly_salary):
    return 0


def check_tax_rate(tax_rates):
    pass


def find_tax_rate(tax_rates: List[TaxRate], salary: float) -> Optional[TaxRate]:
    for r in tax_rates:
        if ((r.start is None or r.start < salary)
                and (r.end is None or r.end >= salary)):
            return r
    return None


def count_tax(
        start_point: float,  # 月薪起征点
        tax_rates: List[TaxRate],  # 税率表
        monthly_salary: float,  # 月薪
        bonus: float,  # 年终奖
        deduction: float,  # 专项扣除
) -> float:
    monthly_need_tax = monthly_salary - count_social_insurance(monthly_salary) - start_point - deduction
    monthly_tax_rate = find_tax_rate(tax_rates, monthly_need_tax)
    monthly_tax = monthly_need_tax * monthly_tax_rate.rate - monthly_tax_rate.deduction
    bonus_tax_rate = find_tax_rate(tax_rates, bonus / 12.0)
    # The bonus tax result is not the accumulated tax, it is what the law says, not a bug
    bonus_tax = bonus * bonus_tax_rate.rate - bonus_tax_rate.deduction
    return monthly_tax + bonus_tax


# 中华人民共和国个人所得税法: http://www.chinatax.gov.cn/n810341/n810755/c3967308/content.html
# 关于个人所得税法修改后有关优惠政策衔接问题的通知:
# http://www.chinatax.gov.cn/n810341/n810755/c3978994/content.html
tax_rates_2019 = [
    TaxRate(None, 3000, 0.03, 0),
    TaxRate(3000, 12000, 0.1, 210),
    TaxRate(12000, 25000, 0.2, 1410),
    TaxRate(25000, 35000, 0.25, 2660),
    TaxRate(35000, 55000, 0.3, 4410),
    TaxRate(55000, 80000, 0.35, 7160),
    TaxRate(80000, None, 0.45, 15160),
]

monthly_start_point_2019 = 60000 / 12.0


def count_tax_2019(monthly_salary, bonus, deduction):
    return count_tax(monthly_start_point_2019, tax_rates_2019, monthly_salary,
                     bonus, deduction)


def draw_tax_2019():
    x = []
    y = []
    z = []
    for monthly_salary in range(0, 200000, 2000):
        for bonus in range(0, 2000000, 20000):
            salary = 12 * monthly_salary + bonus
            tax = count_tax_2019(monthly_salary, bonus, 0)
            after_tax = salary - tax
            x.append(monthly_salary)
            y.append(bonus)
            z.append(after_tax)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(np.array(x), np.array(y), np.array(z))
    plt.show()


draw_tax_2019()
