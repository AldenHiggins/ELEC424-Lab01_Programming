CC=gcc
ORDER = "ASC"
CFLAGS=-g -D $(ORDER)
DEPS = sort.h
OBJ = sort.o read_data.a 

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

sort: $(OBJ)
	gcc -o $@ $^ $(CFLAGS)

clean:
	rm sort
