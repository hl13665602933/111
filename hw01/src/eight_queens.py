def solve_n_queens(n):
    """
    使用回溯法解决N皇后问题
    :param n: 棋盘大小
    :return: 所有合法的棋盘布局
    """

    def backtrack(row, queens, cols, diags1, diags2):
        if row == n:
            # 生成棋盘布局
            board = ['.' * q + 'Q' + '.' * (n - q - 1) for q in queens]
            solutions.append(board)
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            # 检查列和对角线是否冲突
            if col not in cols and d1 not in diags1 and d2 not in diags2:
                cols.add(col)
                diags1.add(d1)
                diags2.add(d2)
                queens.append(col)
                # 递归处理下一行
                backtrack(row + 1, queens, cols, diags1, diags2)
                # 回溯：撤销选择
                queens.pop()
                cols.remove(col)
                diags1.remove(d1)
                diags2.remove(d2)

    solutions = []
    backtrack(0, [], set(), set(), set())
    return solutions


if __name__ == "__main__":
    # 测试8皇后问题
    solutions = solve_n_queens(8)
    print("Found {} solutions for 8-Queens problem.".format(len(solutions)))
    # 可选：打印第一个解的棋盘
    if solutions:
        print("\nFirst solution:")
        for row in solutions[0]:
            print(row)