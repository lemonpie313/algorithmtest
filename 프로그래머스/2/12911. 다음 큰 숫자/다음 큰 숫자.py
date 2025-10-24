def solution(n: int) -> int:
    c = n & -n          # n에서 가장 낮은 1비트
    r = n + c           # 그 비트를 한 칸 올림
    return (((r ^ n) >> 2) // c) | r