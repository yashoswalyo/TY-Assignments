#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include<math.h>
#define Iterations 15
#define Size 5
int in = 0;
int out = 0;
int buffer[Size] = {0};
pthread_mutex_t mutex;
void show()
{
  for (int i=0;i<Size;i++)
  printf("%d ",buffer[i]);
  printf("\n");
}
void* prod(void*_args)
{
  int item;
  for(int i=0;i<Iterations;i++)
  {
    printf("\nConsumer blocked\n");
    sleep(rand() % 3);
    item = 1 + rand() % 10;
    pthread_mutex_lock(&mutex);
    buffer[in] = item;
    printf("\nProduced : %d",buffer[in]);
    printf("\nBuffer Status : ");
    show();
    in = (in+1)%Size;
    pthread_mutex_unlock(&mutex);
  }
}
void* cons(void*_args)
{
  for(int i=0;i<Iterations;i++)
  {
   sleep(rand() % 5);
   printf("\nproducer blocked\n");
   int item = buffer[out];
   pthread_mutex_lock(&mutex);
   buffer[out] = 0;
   printf("\nConsumed : %d",item);
   printf("\nBuffer Status : ");
   show();
   out = (out+1)%Size;
   pthread_mutex_unlock(&mutex);
  }
}
int main()
{
  pthread_t pro,con;
  pthread_mutex_init(&mutex,NULL);
  pthread_create(&pro,NULL,prod,NULL);
  pthread_create(&con,NULL,cons,NULL);
  sleep(10);
  pthread_join(pro,NULL);
  pthread_join(con,NULL);
  pthread_mutex_destroy(&mutex);
  return 0;
}
