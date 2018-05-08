
import matplotlib.pyplot as plt
import pandas as pd

def plot_graph():

    data = pd.read_csv('results.csv')

    xticks = ['1', '10', '20', '40', '$\infty$']

    a3c_pong = data[(data['algo'] == 'A3C') & (data['game'] == 'pong')]
    nsql_pong = data[(data['algo'] == 'nstepQ') & (data['game'] == 'pong')]
    a3c_seaquest = data[(data['algo'] == 'A3C') & (data['game'] == 'seaquest')]
    nsql_seaquest = data[(data['algo'] == 'nstepQ') & (data['game'] == 'seaquest')]

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(range(5), a3c_pong['avg_score'], label='A3C')
    plt.plot(range(5), nsql_pong['avg_score'], label='n-step Q-learning')
    plt.xticks(range(5), xticks)
    plt.title('Pong')
    plt.xlabel('rollout')
    plt.ylabel('score')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(5), a3c_seaquest['avg_score'], label='A3C')
    plt.plot(range(5), nsql_seaquest['avg_score'], label='n-step Q-learning')
    plt.xticks(range(5), xticks)
    plt.xlabel('rollout')
    plt.ylabel('score')
    plt.title('Seaquest')
    plt.legend()

    plt.tight_layout()
    plt.savefig('results.png')
    plt.show()
    plt.close()

if __name__ == '__main__':
    plot_graph()

