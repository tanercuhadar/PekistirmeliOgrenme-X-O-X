"""
Created on Wed Dec 11 14:19:08 2024

@author: Taner Çuhadar
"""


from TicTacToe import TicTacToe
from Agent import Agent

game = TicTacToe()

agent = Agent(game, 'X',discount_factor = 0.6, episode = 100000)

#agent.train_brain_x_byrandom() # Modeli eğitmek için bu kod çalıştırılır

agent.play_with_human() #eğitilmiş model ile oyun oynamak için bu kod çalıştırılır





################Episode analizi için Aşağıdaki kodu çalıştırınız##############

"""

from Agent import Agent
from TicTacToe import TicTacToe
import matplotlib.pyplot as plt

# TicTacToe oyununu başlat
game = TicTacToe()

# Farklı episode değerleri için analiz
episode_values = [1000, 5000, 10000, 50000, 100000,200000,400000]
results = []

for episodes in episode_values:
    print(f"Training with {episodes} episodes...")
    agent = Agent(game, 'X', discount_factor=0.6, episode=episodes)
    agent.train_brain_x_byrandom()
    
    results.append(agent.results)
    print(f"Results for {episodes} episodes: {agent.results}")

# Performansı görselleştir
win_rates = [result['X'] / (result['X'] + result['O'] + result['D']) for result in results]

plt.plot(episode_values, win_rates, marker='o', label='Win Rate')
plt.xlabel('Episode Count')
plt.ylabel('Win Rate')
plt.title('Agent Performance Across Different Episode Counts')
plt.legend()
plt.grid()
plt.show()"""

#########İndirim oranı Analizi Aşağıdaki kodu çalıştırınız##########################

"""

from Agent import Agent
from TicTacToe import TicTacToe
import matplotlib.pyplot as plt

# TicTacToe oyununu başlat
game = TicTacToe()

# Farklı discount faktör değerleri
discount_values = [0.3, 0.5, 0.6, 0.8, 0.9]
results = []

for discount in discount_values:
    print(f"Training with discount factor {discount}...")
    agent = Agent(game, 'X', discount_factor=discount, episode=100000)  
    agent.train_brain_x_byrandom()
    results.append(agent.results)

# Performansı görselleştirme
win_rates = [result['X'] / (result['X'] + result['O'] + result['D']) for result in results]

plt.plot(discount_values, win_rates, marker='o', label='Win Rate')
plt.xlabel('Discount Factor')
plt.ylabel('Win Rate')
plt.title('Agent Performance Across Different Discount Factors')
plt.legend()
plt.grid()
plt.show()
"""
###### ###epsilon değeri analizi için aşağıdaki kodun çalıştırınız####


"""
from Agent import Agent
from TicTacToe import TicTacToe
import matplotlib.pyplot as plt

# TicTacToe oyununu başlat
game = TicTacToe()

# Farklı epsilon başlangıç değerleri için analiz
epsilon_values = [0.1, 0.3, 0.5, 0.7, 0.9]
results = []

for epsilon in epsilon_values:
    print(f"Training with epsilon={epsilon}...")
    agent = Agent(game, 'X', discount_factor=0.6, episode=10000, epsilon=epsilon)
    agent.train_brain_x_byrandom()
    results.append(agent.results)
    print(f"Results for epsilon={epsilon}: {agent.results}")

# Performansı görselleştir
win_rates = [result['X'] / (result['X'] + result['O'] + result['D']) for result in results]

plt.plot(epsilon_values, win_rates, marker='o', label='Win Rate')
plt.xlabel('Epsilon (Exploration Rate)')
plt.ylabel('Win Rate')
plt.title('Agent Performance Across Different Epsilon Values')
plt.legend()
plt.grid()
plt.show()
"""