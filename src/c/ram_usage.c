#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double get_ram_usage()
{
    char line[256];
    unsigned long total = 0;
    unsigned long free = 0;
    unsigned long used = 0;
    int valueFound = 0;

    FILE* fp = fopen("/proc/meminfo", "r");

    if (!fp)
    {
        return -1.0;
    }

    while(fgets(line, sizeof(line), fp))
    {
        if (strncmp(line, "MemTotal:", strlen("MemTotal:")) == 0)
        {
            sscanf(line, "MemTotal: %lu", &total);
            valueFound++;
        }

        else if (strncmp(line, "MemAvailable:", strlen("MemAvailable:")) == 0)
        {
            sscanf(line, "MemAvailable: %lu", &free);
            valueFound++;
        }

        if (valueFound == 2)
        {
            break;
        }
    }
    
    if (valueFound < 2 || total == 0)
    {
        return -1.0;
    }

    used = total - free;

    return ((double)used / (double)total) * 100;
}
