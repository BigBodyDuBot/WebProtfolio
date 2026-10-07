#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main(void) {
    const char *mailbox = "/mailboxA";

    struct mq_attr mailbox_queue = {
	.mq_flags = 0,
	.mq_maxmsg = 5,
	.mq_msgsize = 256,
	.mq_curmsgs = 0
 //mq_attr is type definition from mqueue.h, mailbox_queue is the local variable name
	    /*
	     *
	     * fill in the four attributes needed for a mailbox queue
	     */ 
    };
    
    mqd_t mailq = mq_open(mailbox, O_RDONLY, 0644, &mailbox_queue); //fill in the arguments for the mail queue open functions
			//O_RDONLY makes it that the receiver only reads
    
    if (mailq == (mqd_t)-1) { 
	    perror("mq_open error"); 
	    return 1; 
    }
    char *buf = malloc(mailbox_queue.mq_msgsize + 1);
    //create a buffer using a character pointer that allocates the msgsize of the mailbox queue using malloc

    if (!buf) { 
	    perror("Malloc Failed"); 
	    mq_close(mailq); 
	    return 1; 
    }
  
    printf("recv pid=%d waiting on %s \n", getpid(), mailbox);

    while (1) {
        ssize_t n = mq_receive(mailq, buf, mailbox_queue.mq_msgsize, NULL); //fill in the mq_receive arguments
		//"buf" stores it in the buffer	
        if (n < 0) { 
		perror("mq_receive"); 
		break; 
	}
        buf[n] = '\0';


	printf("recv pid=%d recieved: %s\n", getpid(), buf);
	//print a statement stating that the current process PID and the message that was received.
        
	if (strcmp(buf, "term") == 0){ 
		break;
	}
    }

    free(buf);
    mq_close(mailq);

    if (mq_unlink(mailbox) == -1 && errno != ENOENT){ 
	    perror("mq_unlink");
    }
    return 0;
}

