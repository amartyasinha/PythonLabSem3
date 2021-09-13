"""2.Consider a showroom of electronic products, where there are various salesmen. Each salesman is given a
commission of 5%, depending on the sales made per month. In case the sale done is less than 50000, then the
salesman is not given any commission. Write a function to calculate total sales of a salesman in a month,
commission and remarks for the salesman. Sales done by each sales man per week is to be provided as input.
Use tuples/list to store data of salesmen. Assign remarks according to the following criteria:
Excellent: Sales>=80000
Good: Sales>=60000 and <80000
Average: Sales>=40000 and <60000
Work Hard: Sales<40000"""


def salesman(sales_per_week):
    remarks = ""
    total_sales = (sales_per_week / 7) * 30
    commission = 0.05 * total_sales

    if total_sales >= 80000:
        remarks = "Excellent"
    elif 60000 <= total_sales < 80000:
        remarks = "Good"
    elif 40000 <= total_sales < 60000:
        remarks = "Average"
        if total_sales < 50000:
            commission = 0
    elif total_sales < 40000:
        remarks = "Work Hard"
        commission = 0

    print("Total Sales : %0.0f" % total_sales)
    print("Commission  : %0.2f" % commission)
    print("Remarks     :", remarks)


def usr_input():
    n = int(input("Enter the number of salesman : "))

    for i in range(n):
        weekly_sales = int(
            input("Enter the Sales done by the salesman per week : "))
        salesman(weekly_sales)


if __name__ == "__main__":
    usr_input()
