// Implement cyclic redundancy check using polynomial division
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node n;
struct node
{
	int power;
	struct node *next;
};

n *head1 = NULL;
n *head2 = NULL;
n *head = NULL;

char * xor (char data[], char key[])
{
	int n = strlen(key);
	char *res = (char *)malloc(sizeof(char) * n);
	int i;

	for (i = 0; i < n; i++)
		res[i] = (data[i] == key[i]) ? '0' : '1';

	res[i] = '\0';
	return res;
}

		char *divpoly(char divident[], char divisor[])
{
	int i, s;
	// divisor_len is the offset from which
	// we have to start xoring
	int divisor_len = strlen(divisor);
	s = divisor_len;

	char *temp1 = (char *)malloc(sizeof(char) * s);
	char *temp2 = (char *)malloc(sizeof(char) * s);
	int n = strlen(divident);

	// copy divident into temp1
	strncpy(temp1, divident, divisor_len);

	while (divisor_len < n)
	{
		// We can only xor if leading digit of divident is 1
		if (temp1[0] == '1')
			strcpy(temp1, xor(divisor, temp1));

		// shift temp1 towards right by 1 unit
		for (i = 0; i < s - 1; i++)
		{
			temp1[i] = temp1[i + 1];
		}
		temp1[s - 1] = divident[divisor_len];
		divisor_len += 1;
	}

	if (temp1[0] == '1')
		strcpy(temp1, xor(divisor, temp1));

	for (i = 0; i < s - 1; i++)
	{
		temp1[i] = temp1[i + 1];
	}
	temp1[s - 1] = divident[divisor_len];

	free(temp2);
	return temp1;
}

void printList(int listno)
{
	n *temp;
	if (listno == 1)
		temp = head1;
	else if (listno == 2)
		temp = head2;
	else
		temp = head;

	while (temp != NULL)
	{
		printf("x^%d + ", temp->power);

		temp = temp->next;
	}
}

n *getpoly(n **node, int iterations)
{
	for (int i = 0; i < iterations; i++)
	{
		n *newnode = (n *)malloc(sizeof(n));

		printf("Enter the power of term %d :", i + 1);
		scanf("%d", &newnode->power);

		n *temp = *node;
		if (*node == NULL)
		{
			newnode->next = *node;
			*node = newnode;
		}
		else
		{
			while (temp->next != NULL)
				temp = temp->next;

			temp->next = newnode; //last element now points to new node
			newnode->next = NULL;
		}
	}
}

void calculate(int t1, int t2)
{
	int i = 0, j = 0, t = t1 + t2;
	printf("\n------------Message  \n");
	getpoly(&head1, t1);

	printf("\n  Key  \n");
	getpoly(&head2, t2);

	printf("\nMessage :");
	printList(1);
	printf("\nKey :");
	printList(2);

	n *temp1 = head1;

	while (temp1 != NULL)
	{
		n *temp2 = head2;
		n *temp3 = head2->next;
		while (temp2 != temp3)
		{
			n *Poly = (n *)malloc(sizeof(n));
			Poly->power = temp1->power + temp2->power;
			if (head == NULL)
			{
				Poly->next = head;
				head = Poly;
			}
			else
			{
				n *temp = head;
				while (temp->next != NULL)
					temp = temp->next;
				temp->next = Poly; //last element now points to new node
				Poly->next = NULL;
			}
			temp2 = temp2->next;
		}
		temp1 = temp1->next;
	}
	printf("\nEncoded Message : ");
	printList(3);

	char data[100], key[100];
	n *dataptr = head;
	int power;
	int maxpow = head->power;
	int len = head->power;
	i = 0;
	while (i <= len)
	{
		power = dataptr->power;
		if (power == maxpow)
		{
			data[i] = '1';
			if (dataptr->next != NULL)
				dataptr = dataptr->next;
		}
		else
			data[i] = '0';
		maxpow--;
		i++;
	}
	data[i] = '\0';

	dataptr = head2;
	maxpow = head2->power;
	len = head2->power;
	i = 0;
	while (i <= len)
	{
		power = dataptr->power;

		if (power == maxpow)
		{
			key[i] = '1';
			if (dataptr->next != NULL)
				dataptr = dataptr->next;
		}
		else
			key[i] = '0';
		maxpow--;
		i++;
	}
	key[i] = '\0';

	int keylen = strlen(key);
	int datalen = strlen(data);
	len = keylen + datalen - 1;
	char rem[keylen - 1];
	char code[datalen];

	strcpy(rem, divpoly(data, key));
	printf("\n\n  Sender's Side  ");
	printf("\nData : %s", data);
	printf("\nKey : %s", key);
	printf("\nRemainder : %s", rem);

	strcpy(code, data);
	for (i = datalen - keylen + 1, j = 0; j < keylen - 1; i++, j++)
		code[i] = rem[j];
	code[i] = '\0';
	strcpy(rem, divpoly(code, key));

	printf("\n\n  Receivers's Side  ");
	printf("\nEncoded Data : %s", code);
	printf("\nKey : %s", key);
	printf("\nRemainder : %s", rem);
}

int main()
{
	int t1 = 0, t2 = 0;
	printf("Enter the number of terms of Divident : ");
	scanf("%d", &t1);
	printf("Enter the number of terms of Divisor : ");
	scanf("%d", &t2);
	calculate(t1, t2);
	return 0;
}
