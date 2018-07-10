#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pwd.h>
#include <unistd.h>
#include <utmp.h>

int main(int agrc, char* argv[])
{
    struct utmp* entry;
    int i = 0;
    setutent();

    while ((entry = getutent()) != NULL)
    {
        i++;
  	if(entry->ut_type == USER_PROCESS)
        //printf("user: %s, device: %s, remote host: %s, time: %s/n", entry->ut_user,entry->ut_line, entry->ut_host, ctime(&entry->ut_tv));
        printf("user %s, device %s  host %s ip %d time %d\n", entry->ut_user,entry->ut_line, entry->ut_host,  entry->ut_addr, entry->ut_time);
	time_t  t = entry->ut_time;

    }

    printf("number of users %d/n", i);
    printf("%s/n", UTMP_FILE);
    endutent();
    return 0;
}
