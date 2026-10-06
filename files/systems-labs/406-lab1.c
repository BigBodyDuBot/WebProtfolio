#include <stdio.h> //standard input/output library
#include <signal.h> //Access to signal types and function, along with signal structures
#include <sys/time.h> //Access to setitimer, struct itimerval
#include <unistd.h> //Use getpid, along sleep functions like (usleep), and more structures for timers
#include <stdlib.h>


volatile sig_atomic_t ticks = 0;
//volatile -> cannot be changed, and is left out of any optimization done by the compiler
//sig_atomic_t is a data type, that is indivisible meaning it cannot be worked on by muiltiple treads at the same time
//So only one thread can work on the variable at a given time

void timer_isr(){
	ticks++;
	printf("ISR timer tick %d\n", ticks);
}
//This is our interrupt service routine, tracks how many times our process has been interrupted and keeps count using ticks variable
//

int main(){
	//first wet up our signal handler, and we are going to signal SIGALRM
	struct sigaction sigfunc = {0};
	//this is a data structure that specifies how to handle a specific OS signal
	sigfunc.sa_handler = timer_isr;
	//call timer_isr (interrupt service routine) everytime a signal arrives
	sigemptyset(&sigfunc.sa_mask);
	//this is going to ensure that when our handler runs, it does not block any other signals
	//we set the signal mask set to empty
	sigfunc.sa_flags = SA_RESTART;
	//this ensure that the OS is notified to restart any interrupted system calls caused by our signal handler/ISR
	if(sigaction(SIGALRM, &sigfunc, NULL) == -1){
		perror("Error occurred\n");
		return 1;
	}
	//sigaction() is a system call that is used to change the action taken by a process of a specific signal
	//In our case, SIGALRM
	//sigaction(signal, function/structure, NULL);
	//

	struct itimerval interval_timer = {0};
	interval_timer.it_interval.tv_sec = 0;
	interval_timer.it_interval.tv_usec = 250000; //250000 microseconds == 250ms
	//it_interval is the period (the period in which the signal repeats)
	interval_timer.it_value.tv_sec = 0;
	interval_timer.it_value.tv_usec = 250000; //250ms
	//it_value is the initial delay
	if(setitimer(ITIMER_REAL, &interval_timer, NULL) == -1){
		perror("setitimer error");
		return 1;
	}
	//ITIMER_REAL counts the wall clock time, and delivers SIGALRM
	
	printf("PID=%d timer interrupts every ~250ms\n", getpid());
	for(int i=0; i<20; i++){
		printf("The Main thread working: i=%d, ticks=%d\n", i, ticks);
		usleep(180000);//180ms
	}
	printf("Total ticks=%d\n", ticks);
	return 0;
}
