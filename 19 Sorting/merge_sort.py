def mergesort(arr):
	if len(arr)>1:

		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergesort(L)
		mergesort(R)

		i=j=k=0

		while(i<len(L) and j<len(R)):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1

		while(i<len(L)):
			arr[k] = L[i]
			i += 1
			k += 2

		while(j<len(R)):
			arr[k] = R[j]
			j+=1
			k+=1
def printList(arr):
	for i in range(len(arr)):
		print(arr[i],end=" ")
	print()

if __name__ == '__main__':
	arr = [12,32,54,75,3,54,87]
	print('The array is ')
	printList(arr)
	
	mergesort(arr)

	print('\nSorted array is ')
	printList(arr)