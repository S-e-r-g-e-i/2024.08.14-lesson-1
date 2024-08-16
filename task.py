# Дополнительное практическое задание по модулю 2
while True:
    n = int(input('Введите число из 1-ой вставки (от 3 до 20):'))
    while n < 3 or n > 20:
        n = int(input('Введено не верное число! Введите число от 3 до 20:'))
    list_sum = []
    for i in range(3, n + 1, 1):
        if n % i == 0:
            list_sum.append(i)
    # print(list_sum)
    list_para =[]
    for j in range(0, len(list_sum), 1):
        for k in range(1, list_sum[j], 1):
            for l in range(1, list_sum[j], 1):
                if k + l == list_sum[j] and k != l:
                    list_para.append(k)
                    list_para.append(l)
    for m in range(0, len(list_para), 2):
        for n in range(m + 2, len(list_para), 2):
            if m > len(list_para) - 3 or n > len(list_para) - 1:
                break
            while list_para[n] + list_para[n + 1] == list_para[m] + list_para[m + 1] and list_para[n] == list_para[
                m + 1]:
                del list_para[n:n + 2]
                # print(list_para)
                if n > len(list_para) - 1:
                    break
    print('=========================================================================================================')
    print('Вам необходимо ввести следующий пароль во вторую вставку:', *list_para)
    print('=========================================================================================================')