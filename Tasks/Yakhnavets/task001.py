start = int(input("Введите сумму депозита\n"))
rate = int(input("Введите процентную ставку\n"))
years = int(input("Введите срок\n"))
alltimedays = years*12
theend=start*(1+(rate/100/12))**alltimedays
print(theend)
#!
