#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
	private:
		int age;
		int fib_(int);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

int Person::fib(){
	return fib_(age);
	}

int Person::fib_(int n){
    		if (n <= 1){
				return n;
			}else{
				return (fib_(n-1) + fib_(n-2));

			}
		};

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	int Person_fib(Person*person) {return person->fib();}
	}