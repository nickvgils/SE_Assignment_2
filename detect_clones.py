import os


if __name__ == "__main__":
    # loop through types:
    for x in range(1, 4):
        # loop through variations:
        for y in range(1, 5):
            """ Jsinspect:
            Type 1: Use no parameters
            Type 2: Use -I -L to match identifiers and literals for 'type 2'
            Type 3: Use a lower threshold as the default (30) to register 'type 3' clones """

            command = f"jsinspect -I -L -t 25 in/base_snippet.js in/clone_type{x}_{y}.js"
            print(f"Executing {command}")
            os.system(command)
