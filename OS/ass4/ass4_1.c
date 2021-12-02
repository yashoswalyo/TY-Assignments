#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>
#define buffersize 3
sem_t empty;
sem_t full;
int in = 0, out = 0, buffer[buffersize];
void show()
{
for(int i=0;i<buffersize;i++)
{
printf("%d",buffer[i]);
printf(" ");
}
printf("\n");
}
void *producer()
{
int data, temp;
sleep(rand() % 3);
temp = rand() % 3;
while (1)
{
data = rand() % 5;
sem_wait(&empty);
buffer[in] = data;
printf("\n\nProducer Inserted Data %d at %d", data, in);
printf("\nBuffer Status : ");
show();
in = (in + 1) % buffersize;
sem_post(&full);
}
}

void *consumer()
{
int temp, data;
temp = rand() % 5;
while (1)
{
sem_wait(&full);
data = buffer[out];
printf("\n\nConsumer Consumed Data %d from %d", data, out);
printf("\n\nProducer Inserted Data %d at %d", data, in);
printf("\nBuffer Status : ");
show();
out = (out + 1) % buffersize;
sem_post(&empty);
}
}
int main()
{
pthread_t prod, cons;
sem_init(&empty, 0, buffersize);
sem_init(&full, 0, 0);
pthread_create(&prod, NULL, &producer, NULL);
pthread_create(&cons, NULL, &consumer, NULL);
sleep(10);
pthread_join(prod, NULL);
pthread_join(cons, NULL);
return 0;
}
