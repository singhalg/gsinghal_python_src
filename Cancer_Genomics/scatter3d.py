#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     21/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

def plot3dData():


    fig = plt.figure()
    ax = fig.add_subplot(111)
#    n = 100


    Z = [1,0,0,1,0,0,1,0,0,0,0,0,1] # home owner

#    Y = [1,1,1,1,1,1,1,1,1,1,1,1,1]
#    Z = [1]*13 # home owner
#    Y = [0,2,0,2,0.5,2,0.5,0,2,0,0,2,0]  # marital status
#    Y = [0]*13  # marital status
#    X = [12.5,10,7,12,9.5,6,22,8.5,7.5,9,9.8,13,8]  #annual income
    X = [12.5,20,7,24,11.4,12,26.4,8.5,15,9,9.8,26,8]  #annual income

    clr = ['g','g','g','g','r','g','g','r','g','r','m','m','m']
#    clr = ['o','o','o','o','d','o','o','d','o','d','x','x','x']

    A = [-6, -1, 1, 2, 3, 6, 11, 15, 19,]

    Aclr = ['g', 'g', 'r', 'r', 'r', 'g', 'g', 'r', 'r']
#    B =    [1, 1, 0, 0, 0, 1, 1, 0, 0]
    B = [1,1,1,1,1,1,1,1,1]
    ax.scatter(A, B, s=5, c=Aclr )


    ax.set_ybound(lower=0.05, upper=1.0)
    ax.set_xbound(lower=0.05, upper=1.0)
    ax.set_xlabel('Primary')
    ax.set_ylabel('Metastasis')


    plt.show()



def main():
    plot3dData()

if __name__ == '__main__':
    main()
