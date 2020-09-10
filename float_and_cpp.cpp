#include <iostream>
#include <cmath>

int main() {

	double testing = 45.9;

	std::cout << "Type translation: "
		<< testing
		<< " int(testing) = "
		<< int(testing)
		<< std::endl;

	std::cout << testing
		<< " % 1 * 100 = fmod("
		<< testing
		<< ", 1) * 100 = "
		<< fmod(testing, 1) * 100
		<< std::endl;

/*
Type translation: 45.9 int(testing) = 45
45.9 % 1 * 100 = fmod(45.9, 1) * 100 = 90
*/

	return 0;
}
