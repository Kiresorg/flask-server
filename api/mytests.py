import unittest

from controllers import avgDailySales, sumWeeklySalesFigures

class TestWeeklySum(unittest.TestCase):
    def test_returns_sum_with_sales_data(self):
        """
            arrange
        """
        mock_sales_figures = [
            [100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100]
        ]
        mock_weeks = 3

        """
            act
        """
        actual = sumWeeklySalesFigures(mock_weeks, mock_sales_figures)
        
        """
            assert
        """
        expected = 2100
        self.assertEqual(actual, expected)
    
    def test_returns_zero_with_no_data(self):
        """
            arrange
        """
        mock_sales_figures = []
        mock_weeks = 3

        """
            act
        """
        actual = sumWeeklySalesFigures(mock_weeks, mock_sales_figures)
        
        """
            assert
        """
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_returns_zero_with_negative_weeks(self):
        """
            arrange
        """
        mock_sales_figures = [
            [100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100]
        ]
        mock_weeks = -1

        """
            act
        """
        actual = sumWeeklySalesFigures(mock_weeks, mock_sales_figures)
        
        """
            assert
        """
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_returns_zero_with_excess_weeks(self):
        """
            arrange
        """
        mock_sales_figures = [
            [100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100, 100, 100]
        ]
        mock_weeks = 4

        """
            act
        """
        actual = sumWeeklySalesFigures(mock_weeks, mock_sales_figures)
        
        """
            assert
        """
        expected = 0
        self.assertEqual(actual, expected)

class TestAverageDailySales(unittest.TestCase):
    def test_gets_avg_with_good_data(self):
        """
            arrange
        """
        mock_total = 1200
        mock_weeks = 3

        """
            act
        """
        actual = avgDailySales(mock_total, mock_weeks)

        """
            assert
        """
        expected = 57.14
        self.assertEqual(actual, expected)

    def test_returns_zero_with_no_weeks(self):
        """
            arrange
        """
        mock_total = 1200
        mock_weeks = 0

        """
            act
        """
        actual = avgDailySales(mock_total, mock_weeks)

        """
            assert
        """
        expected = 0
        self.assertEqual(actual, expected)
