#include <mqueue.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    const char *mailbox = "/mailboxA";

    struct mq_attr mailbox_queue = {
	.mq_flags = 0,
	.mq_maxmsg = 5,
	.mq_msgsize = 256,
	.mq_curmsgs = 0 
	     /*
	      *fill int the four appropriate attributes needed for a mail queue structure
	      */
    };
    mqd_t mailq = mq_open(mailbox, O_CREAT | O_WRONLY, 0644, &mailbox_queue); //fill in the appropriate attributes for the mq_open command 

    if (mailq == (mqd_t)-1) { //can also cast as a mqd_t data type 
	    perror("mq_open error"); 
	    return 1; 
    }

    for (int i = 1; i <= 5; i++) {
        char msg[64];

	//use snprintf to print the message along with the PID of this process
	snprintf(msg, sizeof(msg), "Message %d from PID %d", i, getpid());

        if (mq_send(mailq, msg, strlen(msg), 0) == -1) { 
		perror("mq_send"); 
		break; 
	}
    }
    mq_send(mailq, "term", 4, 0);
    mq_close(mailq);
    return 0;
}

