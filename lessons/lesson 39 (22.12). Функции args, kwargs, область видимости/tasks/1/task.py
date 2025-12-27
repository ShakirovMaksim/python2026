def mean_abs_deviation(*scores):
    if not scores:
        raise TypeError("Введите хотя-бы одно значение!")

    avg = sum(scores) / len(scores)
    normalized = []
    for score in scores:
        normalized.append(round(score - avg, 1))
    return tuple(normalized)

print(mean_abs_deviation(3, 5, 7, 9))


existing_scores = [10, 8, 6]
print(mean_abs_deviation(*existing_scores))
