all: main run

main:
	gcc interpolacja.c -o interpolacja.o -lgsl -lgslcblas -lm

run: main
	./interpolacja.o

clean:
	rm -f *.o interpolacja


