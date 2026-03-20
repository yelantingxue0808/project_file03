from concurrent.futures import as_completed
import pandas


def save_data(tasks):
    excel_lis = []
    for val in as_completed(tasks):
        excel_lis.extend(val.result())
    # 将数据存储到excel表格中
    pd = pandas.DataFrame(excel_lis)
    pd.to_excel('./中药材天地网市场价格数据1.xlsx')
    print("全部爬取完成！总数据量：", len(excel_lis))
