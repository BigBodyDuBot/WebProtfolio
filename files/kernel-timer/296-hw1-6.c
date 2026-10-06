#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/timer.h>
#include <linux/uaccess.h> 
#include <linux/jiffies.h>
#include <linux/proc_fs.h>
#include <linux/string.h>

static int global_counter = 0;
static struct timer_list my_timer;
void timer(struct timer_list *t);


void timer(struct timer_list *t) {
 global_counter ++; 

//this prints the current counter and jiffie value to the kernal
 printk(KERN_INFO "Counter value: %d | Current jiffies: %ld\n", global_counter, jiffies);
 mod_timer(&my_timer, jiffies + msecs_to_jiffies(1000));

  
}



static ssize_t proc_read(struct file *file, char __user *buf, size_t len, loff_t *offset) {
    static int completed = 0;
	//this is the message that displays when the proc file is read
    const char *message = "Hello! My name is Duy"; 
    size_t message_len = strlen(message);

    if (completed) {
        completed = 0; 
        return 0; 
    }

    if (copy_to_user(buf, message, message_len)) {
        return -EFAULT;
    }

    completed = 1; 
    return message_len;
}


static const struct proc_ops proc_ops = {
    .proc_read = proc_read,
};



int counter_module_init(void) {
	
	printk(KERN_INFO "counter module has been loaded\n");

    	timer_setup(&my_timer, timer, 0);
    	mod_timer(&my_timer, jiffies + msecs_to_jiffies(1000));
	//This creates the proc filesystem entry with read functions for all and only write for users
	proc_create("hw1", 0644, NULL, &proc_ops); 

    return 0;
}



void counter_module_exit(void) {
	
	del_timer(&my_timer);
    	//this removes the proc  filesystem entry so /proc/hw1 is deleted 
	remove_proc_entry("hw1", NULL);
	//this creates a message telling us the kernel log confirming the module has been removed
	printk(KERN_INFO "counter module has been removed\n");
}

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Duy Hoang");
MODULE_DESCRIPTION("CSIT 345 HW1");

module_init(counter_module_init); //tells the kernel to call counter_module_init()
module_exit(counter_module_exit); //tells the kernel to call counter_module_exit()
