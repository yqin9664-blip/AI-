
import pandas as pd
import matplotlib.pyplot as plt

def generate_report(df, output_path):
    df.to_excel(output_path, index=False)

    # 生成简单图表
    if len(df.columns) >= 2:
        df.plot(x=df.columns[0], y=df.columns[1], kind='bar')
        plt.title("Auto Generated Chart")
        plt.savefig(output_path.replace(".xlsx", ".png"))
