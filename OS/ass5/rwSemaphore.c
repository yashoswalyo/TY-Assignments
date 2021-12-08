/*Assignment 5A - Reader - Writer Problem Using Semaphore
Name - Hasnain Merchant		Div - B		Roll No -30
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>
#include <pthread.h>

//Semaphores
sem_t wrt;
sem_t lock;

int hh = 23, mm = 59, ss = 55;
int readerCount = 0;

void set_clock()
{
	ss++;
	if (ss == 60)
	{
		ss = 0;
		mm++;
	}
	if (mm == 60)
	{
		mm = 0;
		hh++;
	}
	if (hh == 24)
	{
		hh = 0;
	}
}

void *writer()
{
	sem_wait(&wrt);
	set_clock();
	printf("\nWriter : Modified Time %02d:%02d:%02d\n\n", hh, mm, ss);
	sem_post(&wrt);
}

void *reader(void *readerNo)
{
	sem_wait(&lock);
	readerCount++;
	if (readerCount == 1)
	{
		sem_wait(&wrt);
	}
	sem_post(&lock);
	printf("\nReader %d : Reads Time %02d:%02d:%02d\n\n", (*((int *)readerNo)), hh, mm, ss);
	sem_wait(&lock);
	readerCount--;
	if (readerCount == 0)
	{
		sem_post(&wrt);
	}
	sem_post(&lock);
}

int main()
{
	pthread_t r[3], w[2];
	sem_init(&wrt, 0, 1);
	sem_init(&lock, 0, 1);

	int a[3] = {1, 2, 3};
	int i = 0;
	while (1)
	{
		pthread_create(&r[0], NULL, reader, (void *)&a[0]);
		pthread_join(r[0], 0);
		sleep(2);

		pthread_create(&w[0], NULL, writer, NULL);
		pthread_join(w[0], 0);
		sleep(2);

		pthread_create(&r[1], NULL, reader, (void *)&a[1]);
		pthread_join(r[1], 0);
		sleep(2);

		pthread_create(&w[1], NULL, writer, NULL);
		pthread_join(w[1], 0);
		sleep(2);

		pthread_create(&r[2], NULL, reader, (void *)&a[2]);
		pthread_join(r[2], 0);
		sleep(2);
	}
	sem_destroy(&wrt);
	sem_destroy(&lock);
	return 0;
}
