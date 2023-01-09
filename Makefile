all: libutil.so

libutil.so: util.o
	g++ -shared -o libutil.so util.o

util.o:
	g++ -c -Wall -Werror -fPIC util.cpp 

clean:
	rm libutil.so util.o