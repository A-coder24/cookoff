def merge_sort(arr,l,n):
    if l>=n :
        return
    if l<n:
        mid=(l+n)//2
        
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,n)
        i=l
        j=mid+1
        c=0
        temp=[]
        while i<=mid and j<=n:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
                c+=mid-i+1

        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j <= n:
            temp.append(arr[j])
            j+=1
        k=0
        for i in range(l,n+1):
            arr[i]=temp[k]
            k+=1

                
                
            
