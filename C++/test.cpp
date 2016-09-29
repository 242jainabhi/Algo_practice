#include<iostream>
#include<climits>
using namespace std;
//Swap two elements
void swap (int *x, int *y);

//Class representing a heap
class heap
{
    int heap_size;
    int heap_capacity;
    int *heap_arr;
    public:
    heap(int capacity)
    {
        heap_capacity = capacity;
        heap_size = 0;
        heap_arr = new int[capacity];
    }

    void print()
    {
        for(int i=0;i<heap_size;i++)
        cout<<heap_arr[i]<<"\t";
    }
    void add_Elem(int);
    void decrease(int,int);
    void del_Elem(int);
    int extract_Max();
    void heapify(int);
    int parent(int i)
    {
        return (i-1)/2;
    }
    int left(int i)
    {
        return 2*i+1;
    }
    int right(int i)
    {
        return 2*i+2;
    }
};
void heap::add_Elem(int x)
{
    if(heap_size == heap_capacity)
    {
        cout<<"Overflow: Can not add new element!\n";
        return;
    }
    int index = heap_size;
    heap_size++;
    heap_arr[index] = x;
    while(index != 0 && heap_arr[parent(index)] < heap_arr[index])
    {
        swap(&heap_arr[parent(index)], &heap_arr[index]);
        index = parent(index);
    }
}
void heap::decrease(int i,int val)
{
    heap_arr[i] = val;
    while (i != 0 && heap_arr[parent(i)] < heap_arr[i])
    {
       swap(&heap_arr[i], &heap_arr[parent(i)]);
       i = parent(i);
    }
}
void heap::del_Elem(int i)
{
    decrease(i,INT_MIN);
    extract_Max();
}

int heap::extract_Max()
{
    if(heap_size <= 0)
    {
        cout<<"Underflow: Can not extract!\n";
        return INT_MIN;
    }
    if(heap_size == 1)
    {
        //heap_size--;
        return heap_arr[--heap_size];
    }
    int root = heap_arr[0];
    heap_arr[0] = heap_arr[--heap_size];
    heapify(0);
    return root;
}
void heap::heapify(int root)
{
    int l = left(root);
    int r = right(root);
    int smallest = root;
    if(l<heap_size && heap_arr[root] < heap_arr[l])
    smallest = l;
    if(r<heap_size && heap_arr[smallest] < heap_arr[r])
    smallest = r;

    if(root != smallest)
    {
        swap(&heap_arr[root], &heap_arr[smallest]);
        heapify(smallest);
    }
}

void swap (int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int n;
    cin>>n;
    int arr[n];

    for(int i=0;i<n;i++)
    cin>>arr[i];
    cout<<-1<<endl<<-1<<endl;
    int mul = 1;
    for(int i=2;i<n;i++)
    {
        heap hp(i+1);
        for(int j=0;j<i+1;j++)
        {
            hp.add_Elem(arr[j]);
        }
        mul *= hp.extract_Max() * hp.extract_Max() * hp.extract_Max();
        cout<<mul<<endl;
        mul = 1;
    }
    return 0;
}
