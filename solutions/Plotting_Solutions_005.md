## Plotting Solutions (005)

1. Generate random data of 25000 points called "temperature

        tmp = np.linspace(0,100,25000)
        tmp
   
2. Divide temperature by 2 and call it "half temperature"

        halftmp = tmp/2

4. Make a line plot of the two data variables

        plt.figure
        plt.plot (tmp,'purple')
        plt.plot (halftmp, 'blue')
        plt.title ("Random Temperature Plot",fontsize =18)
        plt.xlabel ("Amount", fontsize =15)
        plt.ylabel ("Temperature and Half Temperature", fontsize =15)
        plt.tight_layout

6. Make a histogram of "half temperature"
    
        plt.figure
        hh= plt.hist (halftmp, bins = 250)
        plt.title ("Random Half Temperature", fontsize = 15)
        plt.xlabel ("Half temperature", fontsize =15)
        plt.ylabel ("Amount", fontsize = 15)
        plt.tight_layout

8. Create three additional variables called "lat", "long", and "salinity" (30-35)
- need to be same points
- make a scatter plot using above variables
              
        lat = np.random.rand(35)
        long = np.random.rand (35)
        sal = np.arange (35)
                            
        x = long
        y = lat
        z = sal
  
        plt.figure
        plt.scatter(x,y,s=5,c=sal,cmap= "jet")
        plt.xlabel("Long", fontsize = 15)
        plt.ylabel("Lat", fontsize = 15)
        plt.title("Lat v.s. Long")
        plt.tight_layout