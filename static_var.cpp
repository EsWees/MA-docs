#include <iostream>

int test_function (void) {
	static int counter = 0 ;
	counter++;
	return counter;
}

int main() {
	int (&counter1)() = test_function;
	int (&counter2)() = test_function;

	for (int i = 0; i < 10; i++)
		std::cout << counter1() << std::endl;

	for (int i = 0; i < 10; i++)
		std::cout << counter2() << std::endl;

	return 0;
}
