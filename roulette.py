import random

def roulette():
    n = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
            '31', '32', '33', '34', '35', '36', '0', '00'
        ]
    return random.choice(n)

def play(m):
    inital_money = m
    money = inital_money
    bet = 1

    i = 0
    while True:
        num = roulette()
        # lw = 'Lose'

        if num == '0' or num == '00' or int(num) %2 != 0:
            money -= bet
            bet *= 2
        else:
            money += bet
            # lw = 'Win'

        # print(f"Round: {i+1:<5} Number: {num:<3} Result: {lw:<4} Bet: {bet:<7} Total: {money:<7}")

        if money <= 0:
            # print("You have run out of money.")
            return money
        elif bet > money:
            # print("You have no money for bet.")
            return money
        elif money > inital_money * 1.5:
            return money - inital_money

        i += 1

if __name__ == '__main__':
    total_money = 100
    for i in range(0, 10, 1):
        total_money += play(total_money)
        if total_money <= 0:
            print("You are lose.")
            break
    
        print("i=" + str(i), end="\t")
        print("total_money=" + str(total_money), end="\n")
            
