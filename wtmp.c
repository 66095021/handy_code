#include<stdio.h>
#include<fcntl.h>
#include<utmp.h>

int main()
{
	int fd;
	struct utmp cr;
	int reclen = sizeof(struct utmp);

	fd = open(WTMP_FILE, O_RDONLY);
	if (fd == -1){
		perror("oops");
		exit(1);
	}
	while (read(fd, &cr, reclen) == reclen)
	{
		//if(cr.ut_type == USER_PROCESS)
		{
		printf("-- user:%sdevice:%s login %d host %s ip %d\n", cr.ut_user,  cr.ut_line, cr.ut_time, cr.ut_host, cr.ut_addr);
	//	printf(" %d bobo\n", cr.ut_user[0]);
	}
	}
	close (fd);
	return 0;
}
