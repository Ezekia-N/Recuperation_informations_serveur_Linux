#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h>

double get_cpu_usage()
{
    long double a[7], b[7], loadavg;
    long double total_a, total_b, idle_a, idle_b, total_delta, idle_delta;

    FILE *fp;

    fp = fopen("/proc/stat", "r");

    if (!fp)
    {
        return -1.0;
    }

    fscanf(fp, "%*s %Lf %Lf %Lf %Lf %Lf %Lf %Lf", &a[0], &a[1], &a[2], &a[3], &a[4], &a[5], &a[6]);
    fclose(fp);


    usleep(200000);

    fp = fopen("/proc/stat", "r");

    if (!fp)
    {
        return -1.0;
    }

    fscanf(fp, "%*s %Lf %Lf %Lf %Lf %Lf %Lf %Lf", &b[0], &b[1], &b[2], &b[3], &b[4], &b[5], &b[6]);
    fclose(fp);

    total_a = 0;
    total_b = 0;

    for(int i = 0; i < 7; i++)
    {
        total_a += a[i];
        total_b += b[i];
    }

    idle_a = a[3];
    idle_b = b[3];

    total_delta = total_b - total_a;
    idle_delta  = idle_b - idle_a;

    if (total_delta == 0)
    {
        return 0.0;
    }

    return ((total_delta - idle_delta) / total_delta) * 100.0;
}
