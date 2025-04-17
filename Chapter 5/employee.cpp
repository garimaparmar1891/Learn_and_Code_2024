class Employee
{
    string name;
    int age;
    float salary;

public:
    string getName();
    void setName(string name);
    int getAge();
    void setAge(int age);
    float getSalary();
    void setSalary(float salary);
};
Employee employee;

// This Employee class holds data (name, age, salary) and provides getters and setters and no business logic is there
// so this class is a data structure.
// employee is an object — because it is an instance of the Employee class.
