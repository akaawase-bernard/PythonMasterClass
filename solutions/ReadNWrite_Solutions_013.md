## ReadNWrite Solutions (013)

1. Generate any value and amount of data

        data = {"Name":["MLynn","Olivia","Matt"], "Age":[21,21,19], "Year":["Senior","Senior","Junior"],"Major":["Marine_Science","Communications","Music_Ed"]}

2. Save the data

        with open ("./data/task.json", "w") as f:
        json.dump (data,f),

3. Read and write the data

        with open ("./data/task.json", "r") as f:
        loaded_data = json.load(f)
        print("JSON File Content:", loaded_data)

        JSON File Content: {'Name': ['MLynn', 'Olivia', 'Matt'], 'Age': [21, 21, 19], 'Year': ['Senior', 'Senior', 'Junior'], 'Major': ['Marine_Science', 'Communications', 'Music_Ed']}