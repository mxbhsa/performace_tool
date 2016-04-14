#include <stdlib.h>
#include <stdio.h>

#include <likwid.h>

#define SLEEPTIME 2

int main(int argc, char* argv[])
{
    int i;
    int nevents = 10;
    double events[10];
    double time;
    int count;
    // Init Marker API in serial region once in the beginning
    int j = 0;
    likwid_markerInit();  


        printf("Thread sleeps now for %d seconds\n", SLEEPTIME);
        // Start measurements inside a parallel region
        LIKWID_MARKER_START("example");
        // Insert your code here.
        // Often contains an OpenMP for pragma. Regions can be nested.
        sleep(SLEEPTIME);
        // Stop measurements inside a parallel region
        LIKWID_MARKER_STOP("example");
        printf("Thread wakes up again\n");

        // If you need the performance data inside your application, use
        LIKWID_MARKER_GET("example", &nevents, events, &time, &count);
        // where events is an array of doubles with nevents entries,
        // time is a double* and count an int*.
        printf("Region example measures %d events, total measurement time is %f\n", nevents, time);
        printf("The region was called %d times\n", count);
        for (i = 0; i < nevents; i++)
        {
            printf("Event %d: %f\n", i, events[i]);
        }

    // Close Marker API and write results to file for further evaluation done
    // by likwid-perfctr
    likwid_markerClose();
    printf("Event finished\n");
        /* code */

    return 0;
}