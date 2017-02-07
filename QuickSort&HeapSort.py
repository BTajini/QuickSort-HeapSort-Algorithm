def partition_of_quickSort(List, begin, end):
    temp = begin #pivot
    for i in xrange(begin+1, end+1):
        if List[i] <= List[begin]:
            temp += 1
            List[i], List[temp] = List[temp], List[i]
    List[temp], List[begin] = List[begin], List[temp]
    return temp

def quicksort(List, begin=0, end=None):
    if end is None:
        end = len(List) - 1
    if begin >= end:
        return
    temp = partition_of_quickSort(List, begin, end)
    quicksort(List, begin, temp-1)
    quicksort(List, temp+1, end)

def heapsort(List):

  length = len( List ) - 1
  leastemp = length / 2
  for i in range ( leastemp, -1, -1 ):
    moveD( List, i, length )


  for i in range ( length, 0, -1 ):
    if List[0] > List[i]:
      temp( List, 0, i )
      moveD( List, 0, i - 1 )


def moveD( List, first, last ):
  larger = 2 * first + 1
  while larger <= last:

    if ( larger < last ) and ( List[larger] < List[larger + 1] ):
      larger += 1

    if List[larger] > List[first]:
      temp( List, larger, first )

      first = larger;
      larger = 2 * first + 1
    else:
      return


def temp( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp


List = [97, 91220635, 703, 21, 3090, 547]


heapsort(List)
quicksort(List)

print"HeapSort :",  List
print"QuickSort Sort :",  List
