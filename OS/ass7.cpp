#include<iostream>
using namespace std; 
int main()

{

int i, j, k, n, m, y = 0;

cout << "\t\t\t\t\tBANKER'S ALGORITHM";

cout << "\n\nEnter the Number of Processes : "; cin >> n;

cout << "\nEnter the Number of Resources : "; cin >> m;

int alloc[n][m], max[n][m], avail[m];

int f[n], ans[n], ind = 0, need[n][m];

cout << "\n\t\tEnter Process Allocation : "; for (i = 0; i < n; i++)

{

cout << "\n\nP" << i << " : "; for (j = 0; j < m; j++)

{

cout << "\nResource " << j << " : "; cin >> alloc[i][j];

}

}

cout << "\n\t\tEnter Maximum Allocation : "; for (i = 0; i < n; i++)

{

cout << "\n\nP" << i << " : "; for (j = 0; j < m; j++)

{

cout << "\nResource " << j << " : "; cin >> max[i][j];

}

}

cout << "\n\t\tEnter Available Resources : "; for (i = 0; i < m; i++)



cout << "\nResource " << i << " : "; cin >> avail[i];

}

cout << "\n\n\n\t\t\tProcess Allocation : \n\n"; for (i = 0; i < m; i++)

{

cout << "\t\tR" << i;

}

for (i = 0; i < n; i++)

{

cout << "\nP" << i; for (j = 0; j < m; j++)

{

cout << "\t\t" << alloc[i][j];

}

}

cout << "\n\n\t\t\tMaximum Allocation : \n\n"; for (i = 0; i < m; i++)

{

cout << "\t\tR" << i;

}

for (i = 0; i < n; i++)

{

cout << "\nP" << i; for (j = 0; j < m; j++)

{

cout << "\t\t" << max[i][j];

}

}

cout << "\n\n\t\t\tAvailable Resources : \n\n"; for (i = 0; i < m; i++)

{

cout << "\t\tR" << i;

}

cout << "\n";

for (i = 0; i < m; i++)

{

cout << "\t\t" << avail[i];

}

y = 0;

for (k = 0; k < n; k++)

{

f[k] = 0;

}

for (i = 0; i < n; i++)

{

for (j = 0; j < m; j++)

need[i][j] = max[i][j] - alloc[i][j];

}

for (k = 0; k < n; k++)



for (i = 0; i < n; i++)

{

if (f[i] == 0)

{

int flag = 0;

for (j = 0; j < m; j++)

{

if (need[i][j] > avail[j])

{

flag = 1; break;

}

}

if (flag == 0)

{

ans[ind++] = i;

for (y = 0; y < m; y++) avail[y] += alloc[i][y];

f[i] = 1;

}

}

}

}

cout << "\n\nSAFE PROCESS SEQUENCE : \n";

for (i = 0; i < n - 1; i++)

cout << " P" << ans[i] << " ->"; cout << " P" << ans[n - 1] << endl; return (0);

}
