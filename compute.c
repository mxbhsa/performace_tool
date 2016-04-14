#include <stdlib.h>
#include <stdio.h>

#include <likwid.h>

#define SLEEPTIME 2

int main(int argc, char* argv[])
{
    likwid_markerInit();  


        LIKWID_MARKER_START("init");
        int i;
        int nevents = 10;
        double events[10];
        double time;
        int count, test = 0;
        // Init Marker API in serial region once in the beginning
        int j = 0;
        LIKWID_MARKER_STOP("init");


        printf("Thread starts to calculate twice\n");
        // Start measurements inside a parallel region

        // Insert your code here.
        // Often contains an OpenMP for pragma. Regions can be nested.
        LIKWID_MARKER_START("example");
        for (i = 0; i < 10000; ++i)
        {
            for (j = 0; j < 200; ++j)
            {
                test = test +1;
            }
        }
        LIKWID_MARKER_STOP("example");
        // Stop measurements inside a parallel region


        LIKWID_MARKER_START("example2");
        // Insert your code here.
        // Often contains an OpenMP for pragma. Regions can be nested.
        for (i = 0; i < 10000; ++i)
        {
            for (j = 0; j < 200; ++j)
            {
                test = test +1;
            }
        }
        // Stop measurements inside a parallel region
        LIKWID_MARKER_STOP("example2");

        LIKWID_MARKER_START("example3");
        // Insert your code here.
        // Often contains an OpenMP for pragma. Regions can be nested.
        for (i = 0; i < 1000; ++i)
        {
            for (j = 0; j < 200; ++j)
            {
                test = test +1;
            }
        }
        // Stop measurements inside a parallel region
        LIKWID_MARKER_STOP("example3");


        LIKWID_MARKER_GET("example", &nevents, events, &time, &count);

        LIKWID_MARKER_START("output");
        printf("Thread end\n");

        // If you need the performance data inside your application, use
        // where events is an array of doubles with nevents entries,
        // time is a double* and count an int*.
        printf("Region example measures %d events, total measurement time is %f\n", nevents, time);
        printf("The region was called %d times\n", count);
        printf("The answer is %d \n", test);
        for (i = 0; i < nevents; i++)
        {
            printf("Event %d: %f\n", i, events[i]);
        }

        printf("Event finished\n");

        LIKWID_MARKER_STOP("output");

    // Close Marker API and write results to file for further evaluation done
    // by likwid-perfctr
    likwid_markerClose();
        /* code */

    return 0;
}