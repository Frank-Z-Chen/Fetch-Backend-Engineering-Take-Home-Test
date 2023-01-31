import json
import os
import pandas as pd
import sys

with open(os.getcwd() + "/path.json") as json_conf:
    CONF = json.load(json_conf)

file_path = CONF["csv_path"]
df_transactions = pd.read_csv(file_path)

class Points:
    """
    points class
    """
    def spend(self, amount: int) -> dict:
        """
        This function iterates over the CSV file and 
        return a dictionary that sums up the points for each payer
        after a certain amount of points deduction
        :param amount: integer
        :return: dictionary
        """
        df = df_transactions.sort_values("timestamp")
        res = {}
        for index in range(len(df)):
            payer, points = df["payer"].iloc[index], df["points"].iloc[index]
            res[payer] = res.get(payer, 0) + points - amount if points - amount > 0 else 0
            amount -= points
            if amount < 0:
                amount = 0
        return res if amount <= 0 else None

def main():
    pts = Points()
    amount = int(sys.argv[1])
    pts_after_spending = pts.spend(amount)
    if pts_after_spending:
        print(pts_after_spending)
    else:
        print("Points not enough for the last transaction")

if __name__ =="__main__":
    main()