# Verilen listeyi minimum takas ile sıralama
# n = len(arr) arr = [4 3 1 2]
def minimumSwaps(arr):
    swaps=0
    ref_list = sorted(arr)
    sozluk = {v:i for i,v in enumerate(arr)}

    for i,v in enumerate(arr):
        correct_value= ref_list[i]
        correct_value_index= sozluk[correct_value]

        if v!=correct_value:
            arr[i],arr[correct_value_index]= arr[correct_value_index],arr[i]
            sozluk[correct_value]=i
            sozluk[v]=correct_value_index
            swaps+=1
    return swaps
