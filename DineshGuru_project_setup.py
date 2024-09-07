''' This module provides functions for creating a series of project folders. '''


# Import moduldes from standand library
import pathlib
import time
import utils_dinesh
#####################################
# Declare global variables

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    for year in range(start_year,end_year +1):
        year_folder = data_path / str(year)
        year_folder.mkdir(exist_ok=True)
        print(f"Created folder for {year}")
        time.sleep(1)

     
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase=False, remove_spaces=False) -> None:
        for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", " _")
        folder_path = data_path / folder_name
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder for {folder_name}")
        time.sleep(1)

  
#####################################
## Create prefixed folders
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
      for folder in folder_list:
        folder_path = data_path / f"{prefix}-{folder}"
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder for {folder}")
        time.sleep(1) 
    
################
#####################################
## Create prefixed periodically
#####################################
def create_folders_periodically(folder_count: int, duration_seconds: int) -> None:
        for i in range(folder_count):
            folder_path = data_path / f"folder_{i}"
            folder_path.mkdir(exist_ok=True)
            print(f"Created folder {i}")
            time.sleep(duration_seconds)  


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_dinesh.get_byline()}")
   
    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(folder_count=3, duration_seconds=5)

    
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    # create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

