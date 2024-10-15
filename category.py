class Category:
    def __init__(self, category):
        """
        This class represents a budget category like Food, Entertainment, etc.

        :param category: The name of the category, e.g. Food or Entertainment
        """
        self.name = category
        self.ledger = []

    def __str__(self):
        """
        Returns a string summary of all transactions in the ledger, including the total balance
        """
        final_string = ''
        max_amount_len = "{:.2f}".format(float(max(transaction['amount'] for transaction in self.ledger)))
        max_amount_len = max_amount_len[-7:] if len(max_amount_len) >= 7 else max_amount_len

        final_string = self.name.center(30, '*') + '\n'

        for transaction in self.ledger:
            transaction_str = transaction['description'].ljust(23)[:23] + "{:.2f}".format(
                float(transaction['amount'])).rjust(7)[:7]
            final_string = final_string + transaction_str + '\n'

        total = 'Total: ' + "{:.2f}".format(float(self.get_balance()))
        final_string = final_string + total[:30]

        return final_string

    def deposit(self, amount, description=''):
        """
        Adds a new transaction to the ledger for a deposit of money.

        :param amount: The amount of money deposited
        :param description: A description of the deposit
        """
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        """
        Adds a new transaction to the ledger for a withdrawal of money.

        :param amount: The amount of money withdrawn
        :param description: A description of the withdrawal
        """
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        """
        Returns the balance of the ledger, including all deposits and withdrawals
        """
        amount = [transaction['amount'] for transaction in self.ledger]
        balance = sum(x if x > 0 else -abs(x) for x in amount)
        return balance

    def transfer(self, amount, category):
        """
        Transfers money from this category to another category

        :param amount: The amount of money to transfer
        :param category: The category to transfer money to
        """
        if amount <= self.get_balance():
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        Checks if the category has enough money to withdraw the specified amount

        :param amount: The amount of money to check
        """
        return True if amount <= self.get_balance() else False

    def percentages_spent(self, total):
        """
        Returns the percentage of the total budget that has been spent in this category

        :param total: The total budget
        """
        amount = [transaction['amount'] for transaction in self.ledger]
        if len(amount) > 0:
            return int((sum(abs(x) if x < 0 else 0 for x in amount) * 100) / total)
        else:
            return 0


def get_total_withdraw(categories):
    """
    Returns the total amount of money that has been withdrawn across all categories

    :param categories: A list of Category objects
    """
    total_withdraw = 0  # Initialize total_withdraw to 0
    # Iterate over each category
    for category in categories:
        # Get the list of transaction amounts in the category ledger
        amount = [transaction['amount'] for transaction in category.ledger]
        # Calculate the total amount of money withdrawn in this category
        # by summing up the absolute values of all negative amounts (withdrawals)
        total_withdraw_category = sum(abs(x) if x < 0 else 0 for x in amount)
        # Add the total withdrawn in this category to the total
        total_withdraw += total_withdraw_category
    # Return the total amount of money withdrawn across all categories
    return total_withdraw


def create_spend_chart(categories):
    """
    Creates a chart that shows the percentage of the total budget
    that has been spent in each category
    """
    # Calculate the total amount of money withdrawn across all categories
    total_withdraw = get_total_withdraw(categories)

    # Calculate the percentage of the total budget that has been spent
    # in each category
    percentages = [(category.percentages_spent(total_withdraw) // 10) * 10 if len(category.ledger) > 0 else 0 for
                   category in categories]

    # Get the names of all the categories
    names = [category.name for category in categories]

    # Create a bar chart to display the percentages
    bar_chart = 'Percentage spent by category\n'

    # Iterate over each line of the bar chart
    for index in range(10, -1, -1):
        # Create the line
        new_line = (str(index * 10) + '| ').rjust(5) + ''.join(
            'o  ' if percentage >= (index * 10) else '   ' for percentage in percentages) + '\n'
        # Add the line to the bar chart
        bar_chart += new_line

    # Add a line separating the bar chart from the legend
    bar_chart += ' ' * 4 + '-' * 3 * len(percentages) + '-\n'

    # Iterate over each line of the legend
    for line in range(0, len(max(names, key=len))):
        # Create the line
        bar_chart += ' ' * 5

        # Iterate over each category
        for name in names:
            # If the category name is longer than the current line
            if len(name) - 1 >= line:
                # If this is the last line, add a newline
                if line == len(max(names, key=len)) - 1:
                    bar_chart += name[line] + '   '
                else:
                    # Otherwise, add the character and a space
                    bar_chart += name[line] + '  '
            else:
                # Otherwise, add a space and a newline
                bar_chart += '   '
        # Add a newline
        bar_chart += '\n'

    # Return the bar chart
    return bar_chart[:-2]
