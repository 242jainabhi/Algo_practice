#include<iostream>
#include<climits>
#include "Heap.cpp"
using namespace std;

int left(int i)
{
    return i*2+1;
}

int right(int i)
{
    return i*2+2;
}

bool isMaxHeap(int arr[],int root,int n)
{
    if(root > (n-2)/2)
    return true;

    if(arr[root] < arr[left(root)] || arr[root] < arr[right(root)])
    return false;

    isMaxHeap(arr,root+1,n);

}

int main()
{
    int arr[] = {9, 15, 10, 7, 12, 11};
    //int arr[] = {90, 15, 10, 7, 12, 2} ;
    int n = sizeof(arr) / sizeof(int);
    bool flag = true;
    isMaxHeap(arr,0,n) ? cout<<"Yes" : cout<<"No";

    /*Iterative solution
    for(int i=0;i<=(n-2)/2;i++)
    {
        cout<<arr[i]<<' '<<arr[left(i)]<<' '<<arr[right(i)]<<endl;
        if((arr[i] < arr[left(i)]) || (arr[i] < arr[right(i)]))
        {
            flag = false;
            break;
        }
    }
    (flag == true) ?  (cout<<"Not a max heap") : (cout<<"Not a max heap");
    */
    return 0;
}
