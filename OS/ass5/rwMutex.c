/*Assignment 5B - Reader - Writer Problem Using Mutex
Name - Hasnain Merchant		Div - B		Roll No -30
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>
#include <pthread.h>

//Mutex's
pthread_mutex_t wrt;
pthread_mutex_t mutex;

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
	pthread_mutex_lock(&wrt);
	set_clock();
	printf("\nWriter : Modified Time %02d:%02d:%02d\n\n", hh, mm, ss);
	pthread_mutex_unlock(&wrt);
}

void *reader(void *readerNo)
{
	pthread_mutex_lock(&mutex);
	readerCount++;
	if (readerCount == 1)
	{
		pthread_mutex_lock(&wrt);
	}
	pthread_mutex_unlock(&mutex);
	printf("\nReader %d : Reads Time %02d:%02d:%02d\n\n", (*((int *)readerNo)), hh, mm, ss);
	pthread_mutex_lock(&mutex);
	readerCount--;
	if (readerCount == 0)
	{
		pthread_mutex_unlock(&wrt);
	}
	pthread_mutex_unlock(&mutex);
}

int main()
{
	pthread_t r[3], w;
	pthread_mutex_init(&wrt, NULL);
	pthread_mutex_init(&mutex, NULL);

	int a[4] = {1, 2, 3, 4};

	while (1)
	{
		pthread_create(&r[0], NULL, reader, (void *)&a[0]);
		pthread_join(r[0], 0);
		sleep(2);

		pthread_create(&w, NULL, writer, NULL);
		pthread_join(w, 0);
		sleep(2);

		pthread_create(&r[1], NULL, reader, (void *)&a[1]);
		pthread_join(r[1], 0);
		sleep(2);

		pthread_create(&r[2], NULL, reader, (void *)&a[2]);
		pthread_join(r[2], 0);
		sleep(2);

		pthread_create(&w, NULL, writer, NULL);
		pthread_join(w, 0);
		sleep(2);

		pthread_create(&r[3], NULL, reader, (void *)&a[3]);
		pthread_join(r[3], 0);
		sleep(2);
	}
	pthread_mutex_destroy(&wrt);
	pthread_mutex_destroy(&mutex);
	return 0;
}
