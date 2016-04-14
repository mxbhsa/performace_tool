#include <stdlib.h>
#include <stdio.h>


#define SLEEPTIME 2

int main(int argc, char* argv[])
{


        int i;
        int nevents = 10;
        double events[10];
        double time;
        int count, test = 0;
        // Init Marker API in serial region once in the beginning
        int j = 0;


        printf("Thread starts to calculate twice\n");
        // Start measurements inside a parallel region

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


        // Insert your code here.
        // Often contains an OpenMP for pragma. Regions can be nested.
        for (i = 0; i < 10000000; ++i)
        {
            for (j = 0; j < 200; ++j)
            {
                test = test +1;
            }
        }
        // Stop measurements inside a parallel region


        // Insert your code here.
        // Often contains an OpenMP for pragma. Regions can be nested.
        for (i = 0; i < 10000000; ++i)
        {
            for (j = 0; j < 200; ++j)
            {
                test = test +1;
            }
        }
        // Stop measurements inside a parallel region



        printf("Event finished\n");


    // Close Marker API and write results to file for further evaluation done
    // by likwid-perfctr
        /* code */

    return 0;
}