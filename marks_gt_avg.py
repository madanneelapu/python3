# create a function that takes a list of marks and return marks greater than avg of the marks


def cal_avg(marks):
    total = 0;
    for m in marks:
        total += m

    return total / len(marks)


def marks_gt_avg(marks):
    avg = cal_avg(marks)
    print("Average is", avg)
    return [m for m in marks if m > avg]


print(marks_gt_avg([40, 50, 60, 40, 90, 80, 50]))


#version 2


def marks_gt_avg2(marks):
    return [m for m in marks if m > (sum(marks) / len(marks))]


print(marks_gt_avg2([40, 50, 60, 40, 90, 80, 50]))