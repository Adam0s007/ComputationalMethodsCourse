# Definicja kompilatora
CC = gcc

# Opcje kompilatora
CFLAGS = -Wall -O2

# Biblioteki
LIBS = -lgsl -lgslcblas -lm

# Nazwa programu
PROG = monte_carlo

# Obiekty
OBJS = $(PROG).o

all: $(PROG)

$(PROG): $(OBJS)
	$(CC) $(CFLAGS) -o $(PROG) $(OBJS) $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f $(PROG) $(OBJS)
