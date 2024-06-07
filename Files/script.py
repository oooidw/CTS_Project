#!/usr/bin/python

import sys
import os
import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():    

    # Check if the argument is passed
    if len(sys.argv) < 2:
        print()
        print("Error -> ","Usage: python script.py <string>")
        return
    string_argument = sys.argv[1]

    print("Genereting plots...")

    # Get the data
    df = pd.read_csv(string_argument, delimiter=" ",usecols=[0,1,4,8,12],names=["MsuH","m_ini","M_ass","b-y","age_parent"],skiprows=1)
    df = df.sort_values(by=["age_parent"])



    ######################
    # First plot
    ######################
    fig = plt.figure("Plot1")
    # Preparing the data
    ap_min, ap_max = df["age_parent"].min(),df["age_parent"].max()
    n_col = 10
    l = len(df)
    step = int(l/n_col)
    ap_step = (ap_max-ap_min)/n_col
    x,y,c = df[["b-y"]], df[["M_ass"]], df[["age_parent"]].to_numpy()

    # Get the colormap
    viridis = plt.get_cmap('viridis', n_col,)

    # Loop on all the age bins
    for i in range(n_col):

        # Text of the label
        label = "{:.2f} Gyr - {:.2f} Gyr".format(ap_step*i, ap_step*(i+1))

        #Plot the data
        _=plt.scatter(x[i*step:(i+1)*step],y[i*step:(i+1)*step],c=viridis.colors[i],marker=".",label=label,s=7)
        
    # Plot options    
    plt.xlim(-0.2,1.2)
    _=plt.legend(fontsize=8)
    plt.ylabel(r"M_ass")
    plt.xlabel(r"b-y")
    plt.gca().invert_yaxis()
    plt.title("Scatter plot of M_ass vs b-y")

    # Save the plot
    plt.savefig('/opt/my_application/Images/Plot1.png')




    ######################
    # First plot opt
    ###################### 
    fig = plt.figure("Plot1_opt")
    plt.gca().invert_yaxis()

    # Plot the data
    plt.scatter(x,y,c=c,s=4)
    cbar = plt.colorbar()    
    cbar.set_label("Gyr")

    # Plot options
    plt.ylabel(r"M_ass")
    plt.xlabel(r"b-y")
    plt.title("Optional scatter plot of M_ass vs b-y")

    # Save the plot
    plt.savefig('/opt/my_application/Images/Plot1_opt.png')



    ######################
    # Second plot
    ######################
    fig = plt.figure("Plot2")
    # Initializing variables
    n = [1,5]
    h = []
    n_bins = 17

    # Preparing the data
    h.append(df[df["age_parent"]<n[0]]["MsuH"])
    for i in range(len(n)-1):
        h.append(df[(df["age_parent"]>n[i]) & (df["age_parent"]<n[i+1])]["MsuH"])
    h.append(df[df["age_parent"]>n[-1]]["MsuH"])

    # Keywards for the plots
    kwargs = dict(histtype='stepfilled', alpha=0.3, bins=n_bins, ec="k", density=False)

    # Plot the data from the first bin
    plt.hist(h[0], **kwargs, label="age_parent < {:.1f} Gyr".format(n[0]))

    # Plot the average and median lines with text
    average_value = np.mean (h[0])
    median_value = np.median(h[0])
    plt.axvline(average_value, color='blue', linestyle='--')
    plt.axvline(median_value, color='blue', linestyle='dotted')
    plt.text(average_value-0.09, 150, 'Average', rotation='vertical', color='blue')
    plt.text(median_value+0.01, 150, 'Median', rotation='vertical', color='blue')

    for i in range(1, len(n)):                
        # Plot the data from the middle bins
        plt.hist(h[i], **kwargs, label="{:.1f} Gyr < age_parent < {:.1f} Gyr".format(n[i-1], n[i]))

        # Plot the average and median lines with text
        average_value = np.mean(h[i])
        median_value = np.median(h[i])
        plt.axvline(average_value, color='orange', linestyle='--')
        plt.axvline(median_value, color='orange', linestyle='dotted')
        plt.text(average_value-0.09, 400, 'Average', rotation='vertical', color='orange')
        plt.text(median_value+0.02, 400, 'Median', rotation='vertical', color='orange')

    # Plot the data from the last bin
    plt.hist(h[-1], **kwargs, label="age_parant > {:.1f} Gyr".format(n[-1]))

    # Plot the average and median lines with text
    average_value = np.mean(h[-1])
    median_value = np.median(h[-1])
    plt.axvline(average_value, color='green', linestyle='--')
    plt.axvline(median_value, color='green', linestyle='dotted')
    plt.text(average_value-0.09, 100, 'Average', rotation='vertical', color='green')
    plt.text(median_value+0.01, 100, 'Median', rotation='vertical', color='green')

    # Plot options
    plt.xlabel(r"MsuH")
    plt.ylabel(r"Number of stars")
    plt.legend()
    plt.title("Histogram of MsuH")

    # Save the plot
    plt.savefig('/opt/my_application/Images/Plot2.png')




    ######################
    # Third plot
    ######################
    fig = plt.figure("Plot3")
    # Set initial variables
    n = [1,5]
    x = []
    y = []
    n_bins = 17

    # Prepare the data for the scatter plot
    x.append(df[df["age_parent"]<n[0]]["m_ini"])
    y.append(df[df["age_parent"]<n[0]]["MsuH"])
    for i in range(len(n)-1):
        x.append(df[(df["age_parent"]>n[i]) & (df["age_parent"]<n[i+1])]["m_ini"])
        y.append(df[(df["age_parent"]>n[i]) & (df["age_parent"]<n[i+1])]["MsuH"])
    x.append(df[df["age_parent"]>n[-1]]["m_ini"])
    y.append(df[df["age_parent"]>n[-1]]["MsuH"])

    # Set the options for the scatter plot
    kwargs = dict(alpha=0.4, s=8)

    # Plot the data form the first bin
    plt.scatter(x[0],y[0],**kwargs,label="age_parent < {:.1f} Gyr".format(n[0]))

    for i in range(1, len(n)):
        # Plot the data from the middle bins
        plt.scatter(x[i],y[i],**kwargs, label="{:.1f} Gyr < age_parent < {:.1f} Gyr".format(n[i-1], n[i]))

    # Plot the data from the last bin
    plt.scatter(x[-1],y[-1],**kwargs, label="age_parant > {:.1f} Gyr".format(n[-1]))

    # Plot options
    plt.xlabel(r"m_ini")
    plt.ylabel(r"MsuH")
    plt.legend()
    plt.title("Scatter plot of MsuH vs m_ini for different age_parent bins")

    # Save the plot
    plt.savefig('/opt/my_application/Images/Plot3.png')




    ######################
    # Third plot opt
    ######################

    # Create the figures and axes
    fig, axes = plt.subplots(1, 3, figsize=(15, 5) , sharey=True, sharex=True)

    # Set options for the 2D histograms
    r = [[df['m_ini'].min(),df['m_ini'].max()],[df['MsuH'].min()+0.5,df['MsuH'].max()]]
    bins = 32
    kwargs = dict(bins=bins, cmap='viridis', range=r)

    # Plot the first figure
    axes[0].hist2d(x[0],y[0], **kwargs)
    axes[0].legend([],title="age_parent < {:.1f} Gyr".format(n[0]))
    axes[0].set_xlabel(r"m_ini")

    # Plot the middle figures
    for i in range(1, len(n)):
        axes[i].set_xlim(0,6)
        axes[i].hist2d(x[i],y[i], **kwargs)
        axes[i].legend([],title="{:.1f} Gyr < age_parent < {:.1f} Gyr".format(n[i-1], n[i]))
        axes[i].set_xlabel(r"m_ini")

    # Plot the last figure
    axes[-1].hist2d(x[-1],y[-1], **kwargs)
    axes[-1].legend([],title="age_parent > {:.1f} Gyr".format(n[-1]))
    axes[-1].set_xlabel(r"m_ini")


    # Extra options for the plot
    plt.tight_layout()
    axes[0].set_ylabel(r"MsuH")
    plt.suptitle("2d Histograms of m_ini and MsuH for different age_parent ranges",y=1.05)

    # Save the plot
    plt.savefig('/opt/my_application/Images/Plot3_opt.png',bbox_inches='tight')



    # Last message
    print("Plots saved in /opt/my_application/Images")


if __name__ == "__main__":
    main()