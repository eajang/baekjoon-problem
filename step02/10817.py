#세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)

if A >= B and A >= C:	# max number: A
	if B >= C: print(B)
	else: print(C)
elif B >= A and B >= C:	# max number: B
	if A >= C: print(A)
	else: print(C)
elif C >= A and C >= B: # max number: C
	if A >= B: print(A)
	else: print(B)

