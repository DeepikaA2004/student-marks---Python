if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr=student_marks[query_name]
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    print(f"{sum/len(arr):.2f}")