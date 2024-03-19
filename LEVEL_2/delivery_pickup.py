def solution(cap, n, deliveries, pickups):
    answer, todo_d, todo_p = 0, 0, 0
    d_address, p_address = [], []
    for address in range(n):
        todo_d += deliveries[address]
        todo_p += pickups[address]
        if deliveries[address] > 0:
            d_address.append([address, deliveries[address]])
        if pickups[address] > 0:
            p_address.append([address, pickups[address]])
    while todo_d + todo_p > 0:
        answer += (max(peek_stack(d_address)[0], peek_stack(p_address)[0]) + 1) * 2
        todo_d, d_address = do_cycle(todo_d, d_address, cap)
        todo_p, p_address = do_cycle(todo_p, p_address, cap)

    return answer


def do_cycle(todo, todo_stack, cap):
    while todo > 0 and cap > 0:
        address, package = peek_stack(todo_stack)
        if address == 0 and package == 0:
            return
        if package > cap:
            package -= cap
            todo_stack[len(todo_stack) - 1] = [address, package]
            todo -= cap
            cap = 0
        else:
            cap = cap - package
            todo -= package
            todo_stack.pop()
    return todo, todo_stack


def peek_stack(stack):
    if len(stack) > 0:
        return stack[len(stack) - 1]
    return [0, 0]


solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
