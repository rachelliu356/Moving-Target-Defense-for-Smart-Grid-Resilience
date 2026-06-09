/*
 * goose_publisher_example.c with changes to run indefinitely every 3 seconds instead of 4 times
 */

#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <signal.h>

#include "mms_value.h"
#include "goose_publisher.h"
#include "hal_thread.h"

static int running = 1;

void sigint_handler(int signalId)
{
    running = 0;
}

/* has to be executed as root! */
int
main(int argc, char **argv)
{
    char *interface;

    if (argc > 1)
        interface = argv[1];
    else
        interface = "eth0";

    printf("Using interface %s\n", interface);

    signal(SIGINT, sigint_handler);

    LinkedList dataSetValues = LinkedList_create();

    LinkedList_add(dataSetValues, MmsValue_newIntegerFromInt32(1234));
    LinkedList_add(dataSetValues, MmsValue_newBinaryTime(false));
    LinkedList_add(dataSetValues, MmsValue_newIntegerFromInt32(5678));

    CommParameters gooseCommParameters;

    gooseCommParameters.appId = 1000;
    gooseCommParameters.dstAddress[0] = 0x01;
    gooseCommParameters.dstAddress[1] = 0x0c;
    gooseCommParameters.dstAddress[2] = 0xcd;
    gooseCommParameters.dstAddress[3] = 0x01;
    gooseCommParameters.dstAddress[4] = 0x00;
    gooseCommParameters.dstAddress[5] = 0x01;
    gooseCommParameters.vlanId = 0;
    gooseCommParameters.vlanPriority = 4;

    /*
     * Create a new GOOSE publisher instance. As the second parameter the interface
     * name can be provided (e.g. "eth0" on a Linux system). If the second parameter
     * is NULL the interface name as defined with CONFIG_ETHERNET_INTERFACE_ID in
     * stack_config.h is used.
     */
    GoosePublisher publisher = GoosePublisher_create(&gooseCommParameters, interface);

    if (publisher) {
        GoosePublisher_setGoCbRef(publisher, "simpleIOGenericIO/LLN0$GO$gcbAnalogValues");
        GoosePublisher_setConfRev(publisher, 1);
        GoosePublisher_setDataSetRef(publisher, "simpleIOGenericIO/LLN0$AnalogValues");
        GoosePublisher_setTimeAllowedToLive(publisher, 500);

        int frameCount = 0;

        while (running) {
            Thread_sleep(3000);

            if (GoosePublisher_publish(publisher, dataSetValues) == -1) {
                printf("Error sending message!\n");
            }
            else {
                frameCount++;
                printf("Published frame %d\n", frameCount);
            }
        }


        GoosePublisher_destroy(publisher);
    }
    else {
        printf("Failed to create GOOSE publisher. Reason can be that the Ethernet interface doesn't exist or root permission are required.\n");
    }

    LinkedList_destroyDeep(dataSetValues, (LinkedListValueDeleteFunction) MmsValue_delete);

    return 0;
}