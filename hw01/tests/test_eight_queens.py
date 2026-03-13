# 纯 Python 原生测试代码（无需任何第三方库）
# 导入 N 皇后求解函数（确保路径正确）
import sys
sys.path.append("d:/Users/Huangli/Desktop/hw01/src")  # 手动添加 src 目录到路径
from eight_queens import solve_n_queens

def test_n_queens_4():
    """测试4皇后问题，预期2个解"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2, "Expected 2 solutions for N=4, got {}".format(len(solutions))
    print("✅ 4皇后测试通过！")

def test_n_queens_8():
    """测试8皇后问题，预期92个解"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92, "Expected 92 solutions for N=8, got {}".format(len(solutions))
    print("✅ 8皇后测试通过！")

if __name__ == "__main__":
    try:
        # 执行所有测试
        test_n_queens_4()
        test_n_queens_8()
        print("\n🎉 所有测试都通过了！")
    except AssertionError as e:
        print("\n❌ 测试失败：", e)
    except ImportError as e:
        print("\n❌ 导入失败：", e, "请检查 eight_queens.py 文件路径是否正确")