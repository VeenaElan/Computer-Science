#include<iostream>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#define fun main
using namespace std;
class book
{

    char title[100],author[100],sub[100];
    int stock,issued,code;
    float price;
    static int totalbooks;

    public:

    book();
    book(int code,char title[],char author[],char sub[],float price,int stock=1000);
    void getdata();
    void searchbook(book b[],int &n,char title[]);
    void searchbook(book b[],char author[],int &n);
    void searchbook(char sub[],book b[],int &n);
    void disp();
    void chkstock(int );
    int cstock();
    static int ret_totalstock()
    {
        return totalbooks;
    }
};
int book::totalbooks=0;
book::book()
{
    code=0;
    strcpy(title,"\0");
    strcpy(author,"\0");
    strcpy(sub,"\0");
    price=0;
    stock=0;
}
book::book(int code,char title[],char author[],char sub[],float price,int stock)
{

    this->code=code;
    strcpy(this->title,title);
    strcpy(this->author,author);
    strcpy(this->sub,sub);
    this->price=price;
     this->stock=stock;
    totalbooks+=stock;
}
int fun()
{
    book a[100]={book(1001,"C++","RVMAM","c++",100.0)};

    int ans,n,i;
    char ch='y',title[100],author[100],sub[100];
    cout<<endl<<"\n Enter the no. of books to be entered:";
    cin>>n;
    for(i=1;i<n;++i)
    {
        a[i].getdata();
    }
    while(ch=='y')
    {
    //clrscr();
    system("cls");
    cout<<"\n\n\n \t\t\t\t SEARCH:";
    cout<<"\n1.TITLE\n2.AUTHOR\n3.SUBJECT\n4.DISPLAY ALL BOOKS\n5.TOTAL BOOK COUNT";
    cout<<"\nEnter your choice:";
    cin>>ans;
    if(ans==1)
    {
        cout<<"\n Enter the title to search for:";
        cin>>title;
        a[0].searchbook(a,n,title);
    }
    else if(ans==2)
    {
        cout<<"\n Enter the author to search for:";
        cin>>author;
        a[0].searchbook(a,author,n);
    }
    else if(ans==3)
    {
        cout<<"\n Enter the sub to search for:";
        cin>>sub;
        a[0].searchbook(sub,a,n);
    }
    else if(ans==4)
    {
    	cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    	cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
        for(i=0;i<n;++i)
            a[i].disp();
    }
    else if(ans==5)
    {
        cout<<"\nThe total book count is:"<<book::ret_totalstock();
    }
    else
        cout<<"\nWRONG ENTRY!!";
    cout<<"\n Do u wanna continue??";
    cin>>ch;
	}
}

void book::getdata()
{
    cout<<"\n Enter the code:";
    cin>>code;
    cout<<"\n Enter TITLE:";
    cin>>title;
    cout<<"\n Enter author:";
    cin>>author;
    cout<<"\n Enter subject:";
    cin>>sub;
    cout<<"\n Enter price:";
    cin>>price;
    cout<<"\n Enter stock:";
    cin>>stock;
    cout<<"\n\n";
    totalbooks+=stock;
}

void book::searchbook(book b[],int &n,char title1[])
{
    int i,no,ans,codeno;char ch='y';
    for(i=0;i<n;++i)
    {
        if((strcmp(b[i].title,title1))==0)
        {
            cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    		cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
			b[i].disp();
        }
    }
    cout<<"\n Enter the code no.";
    cin>>codeno;
    for(i=0;i<n;++i)
    {
        if(codeno==b[i].code)
        {
            cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    		cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
			b[i].disp();
            break;
        }
    }
    while(ch=='y')
    {
        cout<<"\n 1.check stock\n 2.Buy books";
        cin>>ans;
        if(ans==2)
        {
            cout<<"\n Enter the no. of books you want:";
            cin>>no;
            b[i].chkstock(no);
        }
        else
        {
            cout<<"\n Remaining stock:"<<b[i].cstock();
        }
        cout<<"\n continue  ??";
        cin>>ch;
    }
}
void book::disp()
{
    cout<<"\n";
	cout<<code<<"\t";
    cout<<title<<"\t";
    cout<<author<<"\t";
    cout<<sub<<"\t";
    cout<<price<<"\t";
    cout<<stock;
}
void book::chkstock(int no)
{
    if((stock-no)<0)
    {
        cout<<"\n Sorry not available :(";
    }
    else
    {
        stock-=no;
        cout<<"\n You can buy them";
        totalbooks-=no;
    }
}

void book::searchbook(book b[],char author1[],int &n)
{
    int i,no,ans,codeno;char ch='y';
    for(i=0;i<n;++i)
    {
        if((strcmp(b[i].author,author1))==0)
        {
        	cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    		cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
            b[i].disp();
        }
    }
    cout<<"\n Enter the code no.";
    cin>>codeno;
    for(i=0;i<n;++i)
    {
        if(codeno==b[i].code)
        {
        	cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    		cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
            b[i].disp();
            break;
        }
    }
    while(ch=='y')
    {
        cout<<"\n 1.check stock\n 2.Take books";
        cin>>ans;
        if(ans==2)
        {
            cout<<"\n Enter the no. of books you want:";
            cin>>no;
            b[i].chkstock(no);
        }
        else
        {
            cout<<"\n Remaining stock:"<<b[i].cstock();
        }
        cout<<"\n continue??";
        cin>>ch;
    }
}

void book::searchbook(char sub1[],book b[],int &n)
{
    int i,no,ans,codeno;char ch='y';
    for(i=0;i<n;++i)
    {
        if((strcmp(b[i].sub,sub1))==0)
        {
        	cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    		cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
            b[i].disp();
        }
    }
    cout<<"\n Enter the code no.";
    cin>>codeno;
    for(i=0;i<n;++i)
    {
        if(codeno==b[i].code)
        {
        	cout<<"\n\nDETAILS OF THE BOOK"<<endl;
    		cout<<"CODE\tTITLE\tAUTHOR\tSUB\tPRICE\tSTOCK\n";
            b[i].disp();
            break;
        }
    }
    while(ch=='y')
    {
        cout<<"\n 1.chk stock\n 2.Take books";
        cin>>ans;
        if(ans==2)
        {
            cout<<"\n Enter the no. of books u want:";
            cin>>no;
            b[i].chkstock(no);
        }
        else
        {
            cout<<"\n REM stock:"<<b[i].cstock();
        }
        cout<<"\n cont??";
        cin>>ch;
    }
}
inline int book::cstock()
{
    return(stock);
}
