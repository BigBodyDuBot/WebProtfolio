#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>	

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int temp1;
int temp2;
int temp3;
int temp4;

sem_t mutex;
sem_t empty;
sem_t full;

void *producer(void *param){
	int item_produced = 1;
	while (1){
		//while (counter == BUFFER_SIZE);
		sem_wait(&empty);
		sem_wait(&mutex);
		buffer[in] = item_produced;
		in = (in + 1)%BUFFER_SIZE;
		//counter++;

		sem_getvalue(&empty, &temp1);
		sem_getvalue(&full, &temp2);

		printf("producer produced an item, counter is: %d and the value of full is%d\n", temp1, temp2);
		sleep(1);
		sem_post(&mutex);
		sem_post(&full);

	}
}


void *consumer(void * param){
	while (1){
		//while(counter == 0);
		sem_wait(&full);
		sem_wait(&mutex);
		int item = buffer[out];
		out = (out+1)%BUFFER_SIZE;
		//counter--;
		sleep(2);
		sem_getvalue(&empty, &temp3);
		sem_getvalue(&full, &temp4);
		printf("Consumer consumed %d items, full: %d, empty: %d\n" , item, temp4, temp3);
		sem_post(&mutex);
		sem_post(&empty);
	}
}

int main(){
	sem_init(&mutex,0 ,1);
	sem_init(&empty, 0, BUFFER_SIZE);
	sem_init(&full, 0, 0);
	
	pthread_t thread1, thread2;

	pthread_create(&thread1, NULL, producer, NULL);
	pthread_create(&thread2, NULL, consumer, NULL);

	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);

	sem_destroy(&mutex);
	sem_destroy(&empty);
	sem_destroy(&full);
	return 0;

}


