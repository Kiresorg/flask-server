from pyparsing import restOfLine


"""
    simulates database call for weekly sales figures
    each row is arranged Sunday to Saturday
"""
mock_db_call = [
    [8050.22, 5009.98, 3467.19, 7300.22, 1292.33, 988.45, 12359.87],
    [11030.11, 6049.45, 6461.67, 7280.19, 1162.51, 481.95, 17460.78],
    [4302.37, 5477.48, 4467.19, 5400.82, 1697.73, 888.54, 14759.32]
]

def getSalesData(weeks):
    totalSales = 0
    """
        mock dB call
    """
    weeklySalesFromDB = mock_db_call

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

        return [totalSales, averageDailySales]

    dailyAverage = 0

"""
    Mocks a database call for sales figures
"""
def getSalesFigures(numWeeks):
    index = 0
    result = []

    while index < len(mock_db_call):
        result.append(mock_db_call[index])
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
    return totalSales

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

    while index < len(weeklySalesList)-1:
        result.append(sum(weeklySalesList[index]))
        index += 1
    return result