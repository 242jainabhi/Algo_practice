#include<iostream>
#include<climits>
using namespace std;
#define N 4
struct heapNode
{
    int element;
    int i;
    int j;
};

void swap(heapNode *x, heapNode *y)
{
    heapNode temp = *x;
    *x = *y;
    *y = *x;
}
class heap
{
    private:
    heapNode *heapArr;
    int heapSize;

    public:
    void heapify(int);
    heap(heapNode arr[], int size);
    heapNode getMin()
    {
        return heapArr[0];
    }
    void replaceMin(heapNode x)
    {
        heapArr[0] = x;  heapify(0);
    }
    int left(int i){return (2*i+1);}
    int right(int i){return (2*i+2);}
};

heap::heap(heapNode arr[], int size)
{
    heapSize = size;
    heapArr = arr;
    int i = (heapSize-1)/2;
    if(i>=0)
    {
        heapify(i);
        i--;
    }
}
void heap::heapify(int root)
{
    int l = left(root);
    int r = right(root);
    int smallest = root;
    if(l<heapSize && heapArr[l].element < heapArr[root].element)
    smallest = l;
    if(r<heapSize && heapArr[r].element < heapArr[smallest].element)
    smallest = l;
    if(smallest != root)
    {
        swap(&heapArr[root], &heapArr[smallest]);
        heapify(smallest);
    }
}

void printSorted(int mat[][N])
{
    heapNode *hArr = new heapNode[N];
    for(int i=0;i<N;i++)
    {
        hArr[i].element = mat[i][0];
        hArr[i].i = i;
        hArr[i].j = 1;
    }
    heap hp(hArr,N);
    for(int count=0;count<N*N;count++)
    {
        heapNode n = hp.getMin();
        cout<<n.element<<' ';

        if(n.j < N)
        {
            n.element = mat[n.i][n.j];
            n.j += 1;
        }
        else{n.element = INT_MAX;}

        hp.replaceMin(n);
    }
}

int main()
{
    int mat[N][N] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}, };
    printSorted(mat);
    return 0;
}
