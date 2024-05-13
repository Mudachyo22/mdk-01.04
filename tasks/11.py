N, M = map(int, input().split())
Anya = set(int(input()) for _ in range(N))
Boris = set(int(input()) for _ in range(M))
both = sorted(Anya & Boris)
only_Anya = sorted(Anya - Boris)
only_Boris = sorted(Boris - Anya)

print(len(both), *both)
print(len(only_Anya), *only_Anya)
print(len(only_Boris), *only_Boris)