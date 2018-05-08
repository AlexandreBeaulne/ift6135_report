import glob
import matplotlib.pyplot as plt
import numpy as np
import os
import csv
import math



def plot_graph(save=False):
    data = np.loadtxt('results.csv', delimiter=',', skiprows=1, dtype = 'str')

    algos = data[:, 0]
    games = data[:, 1]
    rollout = np.array(data[:, 2], dtype ='float')
    avg_score = np.array(data[:, 3], dtype ='float')

    games_un = np.unique(games)
    algos_un = np.unique(algos)
    rollout_un = np.unique(rollout)
    
    
    # n = len(rollout_un)
    num_games = len(games_un)
    xarray = rollout[:len(rollout_un)]
    index = 0
    plt.figure()
    for i in range(len(games_un)):
        plt.subplot(1, num_games, i + 1)
        game = games_un[i]
        print(game)
        for j in range(len(algos_un)):
            alg = algos_un[j]
            print(alg)
            scores = []
            for k in range(len(rollout_un)):
                scores.append(avg_score[index])
                index += 1
            yarray = scores
            plt.plot(xarray, yarray, label=alg)
            plt.xlabel('rollout length')
            plt.ylabel('avg score')
            print(scores)
        plt.legend(loc='best')
        plt.title('{}'.format(game))
    plt.tight_layout()
    if save:
        plt.savefig('results.png')
    plt.show()
    plt.close()



if __name__ == '__main__':
    plot_graph(True)