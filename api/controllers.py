from pyparsing import restOfLine
from sqlalchemy import null


"""
    simulates database call for weekly sales figures
    each row is arranged Sunday to Saturday
"""
mock_database_sales_table = [
    [1,1,1,1,1,1,1],
    [8050.22, 5009.98, 3467.19, 7300.22, 1292.33, 988.45, 12359.87],
    [11030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [4302.37, 5477.48, 4467.19, 5400.82, 1697.73, 888.54, 14759.32],
    [11030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [12030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [14030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [9030.11, 6049.45, 6461.67, 7280.19, 1162.51, 482.95, 17460.78],
    [11030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [21030.11, 6049.45, 6461.67, 7210.19, 1162.51, 481.95, 17460.78],
    [11030.11, 6049.45, 6461.67, 5580.19, 1162.51, 481.95, 17460.78],
    [11030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [19030.11, 6049.45, 6461.67, 9980.19, 1162.51, 481.95, 17460.78],
    [11030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [11630.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [11030.11, 8349.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [11930.11, 6049.45, 6461.67, 7280.19, 1362.51, 481.95, 17460.78]
]

def getSalesData(weeks):
    totalSales = 0
    """
        mock dB call
    """
    weeklySalesFromDB = mock_database_sales_table

    """
        calculate sum of sales figures for given number of weeks
        calculate average daily sales
    """
    if(weeks > 0 and weeks <= len(weeklySalesFromDB)):
        index = 0

        while index < weeks:
            totalSales = totalSales + sum(weeklySalesFromDB[weeks-index-1])
            index += 1
        
        averageDailySales = round(totalSales/(index*7), 2)

        return [round(totalSales, 2), averageDailySales]

    dailyAverage = 0

"""
    Mocks a database call for sales figures
"""
def getSalesFigures(weeks):
    if weeks <= 0:
        raise ValueError("You must request a positive number of weeks")
        
    """ if more weeks are requested than exist, return all weeks avalable """
    if(weeks > len(mock_database_sales_table)):
        weeks = len(mock_database_sales_table)
    
    index = 0
    result = []
    
    while index < weeks:
        result.append(mock_database_sales_table[index])
        index += 1
    return result


"""
    Returns total sales for a given number of weeks
"""
def sumWeeklySalesFigures(numWeeks, salesFiguresFromDB):
    totalSales = 0
    
    if(numWeeks > 0 and numWeeks <= len(salesFiguresFromDB)):
        index = 0

        while index < numWeeks:
            totalSales = totalSales + sum(salesFiguresFromDB[numWeeks-index-1])
            index += 1
    return round(totalSales, 2)

def avgDailySales(total, numWeeks):
    if(numWeeks > 0):
        return round(total/(numWeeks*7),2)
    else:
        return 0

"""
    gets sales totals by week, given a set of weekly sales figures
"""
def weeklySalesTotals(weeklySalesList):
    result = []
    index = 0

    while index < len(weeklySalesList):
        result.append(sum(weeklySalesList[index]))
        index += 1
    return result