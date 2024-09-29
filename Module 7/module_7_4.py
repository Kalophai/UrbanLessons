def test():
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 18015.2
    tasks_total = 82
    time_avg = 350.4
    challenge_result = "победа команды Мастера кода!"

    print("В команде Мастера кода участников: %s ! " % team1_num)
    print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

    print("Команда Волшебники данных решила задач: {} !".format(score_2))
    print("Волшебники данных решили задачи за {} с !".format(team1_time))

    print(f"Команды решили {score_1} и {score_2} задач")
    print(f"Результат битвы: {challenge_result}!")
    print(f"Сегодня было решено {tasks_total} задач, в среднем по  {time_avg} на задачу!.")


def start():
    test()

if __name__ == '__main__':
    start()