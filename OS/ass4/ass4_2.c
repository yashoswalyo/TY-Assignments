#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<time.h>
#include<semaphore.h>
#define Iterations 12
#define Size 6
sem_t empty;
sem_t full;
int in=0;
int out=0;
int buffer[Size]= {0};
pthread_mutex_t mutex;

void show()
{
for(int i=0;i<Size;i++)
{
printf("%d",buffer[i]);
printf(" ");
}
printf("\n");
}

void* prod(void* _args)
{
int item;
for(int i=0;i<Iterations;i++)
{
sleep(rand() % 3);
item = 1 + rand() % 10;
pthread_mutex_lock(&mutex);
sem_wait(&empty);
buffer[in]=item;
printf("\nProduced : %d", buffer[in]);
printf("\nBuffer Status :");
show();
in= (in+1) % Size;
pthread_mutex_unlock(&mutex);
sem_post(&full);
}
}
void* cons()
{
for(int i=0;i<Iterations;i++)
{
sleep(rand() % 5);
sem_wait(&full);
int item=buffer[out];
pthread_mutex_lock(&mutex);
buffer[out]=0;
printf("\nConsumed : %d",item);
printf("\nBuffer Status : ");
show();
out=(out+1)%Size;
pthread_mutex_unlock(&mutex);
sem_post(&empty);
}
}

int main()
{
pthread_t p,c;
pthread_mutex_init(&mutex,NULL);
sem_init(&empty,0,Size);
sem_init(&full,0,0);
pthread_create(&p,NULL,prod,NULL);
pthread_create(&c,NULL,cons,NULL);
sleep(10);
pthread_join(p,NULL);
pthread_join(c,NULL);
pthread_mutex_destroy(&mutex);
sem_destroy(&empty);
sem_destroy(&full);
return 0;
}