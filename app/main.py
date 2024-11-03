class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = []

    # First, create all Person instances and add them to Person.people
    for person in people:
        name = person["name"]
        age = person["age"]

        # Create a Person instance and add it to the list
        person_instance = Person(name, age)
        instances.append(person_instance)

    # Now set the wife/husband attributes if they are not None
    for person in people:
        name = person["name"]
        spouse_key = "wife" if "wife" in person else "husband"

        if person[spouse_key] is not None:
            # Retrieve the person instance and their spouse instance
            person_instance = Person.people[name]
            spouse_instance = Person.people[person[spouse_key]]

            # Set the attribute (either wife or husband)
            setattr(person_instance, spouse_key, spouse_instance)

    return instances
