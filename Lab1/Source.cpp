#include <iostream>
using namespace std;

void Fillarray(int **arr, int rows, int cols)
{

    for (int i = 0; i < rows; i++)
    {

        arr[i] = new int[cols];
    }

    for (int i = 0; i < rows; i++)
    {

        for (int j = 0; j < cols; j++)
        {
            arr[i][j] = rand() % 20;
        }
    }
}
int Fillarray1(int **arr, int *arr1, int rows, int cols)
{
    int k = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (arr[i][j] % 2 == 0 && i == j)
            {

                arr1[k] = arr[i][j];

                k++;
            }
        }
    }
    return 0;
}

int Showarray1(int **arr, int rows, int cols)
{

    cout << endl
         << endl
         << "Origin array :  " << endl
         << endl;

    for (int i = 0; i < rows; i++)
    {

        for (int j = 0; j < cols; j++)
        {

            cout << arr[i][j] << "\t";
        }

        cout << endl;
    }

    cout << endl
         << endl;

    return 0;
}
int count(int **arr, int rows, int cols)
{
    int size = 0;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (arr[i][j] % 2 == 0 && i == j)
            {
                size += 1;
            }
        }
    }
    return size;
}
int Showarray2(int *arr1, int size)
{

    cout << endl
         << endl
         << "Array:" << endl
         << endl;

    for (int i = 0; i < size; i++)
    {
        cout << arr1[i] << "\t";
    }
    return 0;
}
void result1(int *arr1, int size)
{
    int result = 1;
    for (int i = 0; i < size; i++)
    {
        result = result * arr1[i];
    }
    if (result != 1)
    {
        cout << endl
             << "result =  " << result << endl;
        ;
    }
    else
    {
        cout << "no even on diag";
    }
}
int main()
{
    setlocale(LC_ALL, "ru");
    int rows;
    int cols;
    cout << "enter rows" << endl;
    cin >> rows;
    cout << "enter col" << endl;
    cin >> cols;
    int **arr = new int *[rows];
    Fillarray(arr, rows, cols);
    int size = count(arr, rows, cols);
    int *arr1 = new int[size];
    Fillarray1(arr, arr1, rows, cols);
    Showarray1(arr, rows, cols);
    Showarray2(arr1, size);
    result1(arr1, size);

    delete[] arr1;
    for (int i = 0; i < rows; i++)
    {
        delete[] arr[i];
    }
    delete[] arr;
}