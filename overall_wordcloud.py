import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('players_20.csv')

counts = data['overall'].value_counts()
print(type(counts))

counts.index = counts.index.astype(str)
#alter counts data frame value to str

"""
ovr=[]
for player_ovr in data['overall']:
    ovr.append(str(player_ovr))

overall_collect = " ".join(ovr)
print(overall_collect)
"""


wordCloud_result = WordCloud(
    background_color='black',min_font_size=5,max_font_size=256,
    font_path='SoukouMincho.ttf',random_state=50
    ).generate_from_frequencies(counts)
#plt.figure(figsize=(10,5))
plt.imshow(wordCloud_result)
plt.axis("off")
plt.show()