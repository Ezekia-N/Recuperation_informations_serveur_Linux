#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h>

double get_cpu_usage()
{
    long double user, nice, system, idle, iowait, irq, softirq;
    long double total_a, total_b, idle_a, idle_b;
    long double total_delta, idle_delta;

    FILE *fp;

    fp = fopen("/proc/stat", "r");
    if (!fp) return -1.0;
    
    if (fscanf(fp, "%*s %Lf %Lf %Lf %Lf %Lf %Lf %Lf", 
               &user, &nice, &system, &idle, &iowait, &irq, &softirq) != 7) {
        fclose(fp);
        return -1.0;
    }
    fclose(fp);

    total_a = user + nice + system + idle + iowait + irq + softirq;
    idle_a = idle + iowait;

    usleep(200000);

    fp = fopen("/proc/stat", "r");
    if (!fp) return -1.0;

    if (fscanf(fp, "%*s %Lf %Lf %Lf %Lf %Lf %Lf %Lf", 
               &user, &nice, &system, &idle, &iowait, &irq, &softirq) != 7) 
    {
        fclose(fp);
        return -1.0;
    }

    fclose(fp);

    total_b = user + nice + system + idle + iowait + irq + softirq;
    idle_b = idle + iowait; 

    total_delta = total_b - total_a;
    idle_delta  = idle_b - idle_a;

    if (total_delta <= 0.0) return 0.0;

    return ((total_delta - idle_delta) / total_delta) * 100.0;
}
