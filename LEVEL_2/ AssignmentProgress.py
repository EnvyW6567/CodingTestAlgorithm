def solution(plans):
    assignment_stack = []
    plan_minute = []
    answer = []
    for plan in plans:
        assignment, start, end = convert_plan_to_minute(plan)
        plan_minute.append([assignment, start, end])
    sorted_plans = sorted(plan_minute, key=lambda x: x[1])

    for plan in sorted_plans:
        assignment, start, end = plan
        while len(assignment_stack) > 0:
            prevAssignment, prevEnd = assignment_stack[-1]
            if prevEnd <= start:
                answer.append(prevAssignment)
                assignment_stack.pop()
            else:
                break

        for index, prevPlan in enumerate(assignment_stack):
            prevAssignment, prevEnd = prevPlan
            assignment_stack[index] = [prevAssignment, prevEnd + end - start]
        assignment_stack.append([assignment, end])

    while len(assignment_stack) > 0:
        answer.append(assignment_stack.pop()[0])

    return answer


def convert_plan_to_minute(plan):
    assignment, start, takeTime = plan
    hour, minute = start.split(':')
    startMinute = int(hour) * 60 + int(minute)
    endMinute = startMinute + int(takeTime)
    return assignment, startMinute, endMinute


plans_input = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"],
               ["computer", "12:30", "100"]]
solution(plans_input)
