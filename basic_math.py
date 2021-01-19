def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list) / len(number_list)
    return mean


def get_median(number_list):
    median = 0
    number_list.sort()
    # 짝수면 가운데 두 자리수를 더한 후 나눠줘야해서 조건문으로 분류
    if len(number_list) % 2 == 0:
        # 중간 인덱스 값 구하기
        idx = len(number_list) // 2
        # 가운데 두개 원소 더하기
        median = number_list[idx - 1] + number_list[idx]
        # 중앙값 구하기
        median /= 2
    else:
        # 홀수면 /2한 만큼의 몫이 인덱스가 됨
        median = number_list[len(number_list) // 2]
    return median