## Glob Solutions (008)

1. Access and print the oldest file
    
        import glob
        oldest_file = min(glob.glob("*.*"), key = os.path.getmtime)
        print('The oldest file is:', oldest_file)
        The oldest file is: 001_basic_maths.ipynb
   
3. Access 5th file in folder

        files = sorted(glob('*'))
        print(files[4])
        005_plotting.ipynb