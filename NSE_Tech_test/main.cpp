#include <iostream>
#include <stdlib.h>
//#include <climits>
#define FLOAT_MAX 9999999
using namespace std;

float customAbs (float x) {
    if (x < 0)
        return x*-1;
    return x;
}

int binarySearch(int s[],int l,int r,float x,float res)
{
   //float y = 0;
   static int index = 0;
   if (r >= l)
   {
        int mid = l + (r - l)/2;
        if(customAbs(x-s[mid]) < res)
        {
            res = customAbs(x-s[mid]);
            index = mid;
        }
        else if (customAbs(x-s[mid]) == res)
        {
        	if (mid < index)
    		index = mid;
        }
        if (s[mid] > x)
        {
           binarySearch(s, l, mid-1, x,res);
        }
        else
        {
            binarySearch(s, mid+1, r, x,res);
        }
        return index;
   }
   return index;
}
int main()
{
    int N,Q,B,C;
    cin>>N;
    int a[N],s[N];
    int SN = 0;
    for(int i=0;i<N;i++)
    {
    	cin>>a[i];
    	SN += a[i];
    	s[i] = SN;
    }
    cin>>Q;
    //cout<<"total sum = "<<s[1];
    for(int i=0;i<Q;i++)
    {
    	cin>>B>>C;
    	float ratio = ((float) B)/C;
    	float x = SN * ratio;
    	//int SI = 0,index;
    	float res = FLOAT_MAX;
    	cout<<a[binarySearch(s,0,N-1,x,res)]<<endl;

    }
    return 0;
}
