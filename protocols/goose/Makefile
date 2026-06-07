CC      = gcc
CFLAGS  = -I/usr/local/include/libiec61850
LDFLAGS = -L/usr/local/lib -liec61850 -lpthread

all: goose_publisher goose_subscriber goose_observer

goose_publisher: goose_publisher.c
	$(CC) $(CFLAGS) -o goose_publisher goose_publisher.c $(LDFLAGS)

goose_subscriber: goose_subscriber.c
	$(CC) $(CFLAGS) -o goose_subscriber goose_subscriber.c $(LDFLAGS)

goose_observer: goose_observer.c
	$(CC) $(CFLAGS) -o goose_observer goose_observer.c $(LDFLAGS)

clean:
	rm -f goose_publisher goose_subscriber goose_observer