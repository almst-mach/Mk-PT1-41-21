def friendly_debt(check: int, **friends: int):
    all_friends_money = sum(friends.values())
    if check > all_friends_money:
        print(f'Account must be closed, please pay {check - all_friends_money}$')
        return
    elif check <= all_friends_money:
        print(f'Tips for the waiter: {all_friends_money - check}$')
        average_check = check // len(friends)
        print(f'Average check: {average_check}$')
        creditors = {}
        deptors = {}
        for name, cash in friends.items():
            account_diff = average_check - cash
            if account_diff < 0:
                creditors[name] = account_diff
            elif account_diff > 0:
                deptors[name] = account_diff
            elif account_diff == 0:
                print(f'{name} owes nothing to anyone')

        for k_creditors, v_creditors in creditors.items():
            for k_deptors, v_deptors in deptors.items():
                while v_deptors != 0 and v_creditors != 0:
                    v_creditors += 1
                    v_deptors -= 1
                if deptors[k_deptors] - v_deptors != 0:
                    print(f'{k_deptors} gave his {deptors[k_deptors] - v_deptors}$ to {k_creditors}')
                    deptors[k_deptors] = v_deptors


friendly_debt(300, friend1=60, friend2=25, friend3=65, friend4=60, friend5=90)
