import ConquistGame as game
from ConquistGame import Graph
from ConquistGame import Platforms
from ConquistGame import Vertex


gamePlatforms = Platforms()

map = [['GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS',  'GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS',
           'GRS', '_HSE|7', 'GRS', '_HSE|9', 'GRS', '_TOW|10', 'GRS', '_NXS|11', 'GRS'],
       ['GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', '_TOW|4', 'GRS', 'GRS',
           'DWR', 'HOR', 'HOR', 'UPT', 'HOR', 'UPT', 'HOR', 'UPT', 'HOR', 'UPL', 'GRS'],
       ['GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'UPR', 'HOR', 'DWT', 'UPT',
           'DWL', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'VER', '_CST|6',
           'VER', 'GRS', '_TOW|8', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS','_NXS|1', 'GRS', '_TOW|2', 'GRS', '_HSE|3', 'GRS', '_HSE|5', 'GRS', 'UPR',
           'CRS', 'UPT', 'HOR', 'UPL', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS','UPR', 'HOR', 'UPT', 'HOR', 'UPT', 'HOR', 'UPT', 'HOR', 'HOR', 'UPL',
           'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS' ],
       ['GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS']]

joust = Graph(1, 11, map)
joust.addVertex(Vertex(1, 5))
joust.addVertex(Vertex(2, 10))
joust.addVertex(Vertex(3, 5))
joust.addVertex(Vertex(4, 10))
joust.addVertex(Vertex(5, 5))
joust.addVertex(Vertex(6, 50))
joust.addVertex(Vertex(7, 5))
joust.addVertex(Vertex(8, 10))
joust.addVertex(Vertex(9, 5))
joust.addVertex(Vertex(10, 10))
joust.addVertex(Vertex(11, 5))
joust.vertList[1].color = 0 
joust.vertList[11].color = 1
joust.addEdge(1, 2)
joust.addEdge(2, 3)
joust.addEdge(3, 5)
joust.addEdge(5, 6)
joust.addEdge(6, 4)
joust.addEdge(6, 8)
joust.addEdge(6, 7)
joust.addEdge(7, 9)
joust.addEdge(9, 10)
joust.addEdge(10, 11)
gamePlatforms.addGame(joust, 'joust')

map2 = [['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS',  'GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS',  '_HSE|10',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'DWR',  'RGT','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','_HSE|4', 'GRS', '_TOW|6',  'GRS', '_HSE|8', 'VER', 'VER',  'GRS', 'GRS', 'GRS',  'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'DWR','UPT',  'HOR', 'UPT', 'HOR', 'UPT', 'UPL',  'VER', '_TOW|12',  'GRS', '_NXS|13',  'GRS', '_CST|14', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'VER','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS',  'UPR', 'CRS', 'HOR',  'UPT', 'HOR', 'UPL', 'GRS'],
       ['GRS', '_CST|1', 'GRS', '_NXS|2', 'GRS', '_TOW|3', 'VER','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'VER',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'UPR',  'HOR', 'UPT',  'HOR', 'CRS',  'UPL','GRS',  '_HSE|7', 'GRS', '_TOW|9', 'GRS',  '_HSE|11', 'GRS',  'VER', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'VER',  'GRS',  'DWR', 'UPT',  'HOR', 'UPT', 'HOR', 'UPT','HOR',  'UPL', 'GRS','GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'VER',  '_HSE|5', 'VER','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS','GRS', 'GRS', 'GRS', 'GRS', 'GRS', 'GRS'],
       ['GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'UPR',  'UPT',  'UPL','GRS', 'GRS',  'GRS', 'GRS', 'GRS', 'GRS','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS']]

barrack = Graph(2, 13,map2)
barrack.addVertex(Vertex(1, 50))
barrack.addVertex(Vertex(2, 5))
barrack.addVertex(Vertex(3, 10))
barrack.addVertex(Vertex(4, 5))
barrack.addVertex(Vertex(5, 5))
barrack.addVertex(Vertex(6, 10))
barrack.addVertex(Vertex(7, 5))
barrack.addVertex(Vertex(8, 5))
barrack.addVertex(Vertex(9, 10))
barrack.addVertex(Vertex(10, 5))
barrack.addVertex(Vertex(11, 5))
barrack.addVertex(Vertex(12, 10))
barrack.addVertex(Vertex(13, 5))
barrack.addVertex(Vertex(14, 50))
barrack.vertList[2].color = 0
barrack.vertList[13].color = 1
barrack.addEdge(1, 2)
barrack.addEdge(2, 3)
barrack.addEdge(3, 4)
barrack.addEdge(3, 5)
barrack.addEdge(4, 6)
barrack.addEdge(5, 7)
barrack.addEdge(6, 8)
barrack.addEdge(7, 9)
barrack.addEdge(8, 10)
barrack.addEdge(9, 11)
barrack.addEdge(10, 12)
barrack.addEdge(11, 12)
barrack.addEdge(12, 13)
barrack.addEdge(13, 14)
gamePlatforms.addGame(barrack, 'barrack')


map3 = [[ 'GRS','GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS',  'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS','GRS','GRS'],
       [ 'GRS','DWR',  '_NXS|1', 'GRS',  'DWR', 'HOR',  '_TOW|5','GRS',  'DWR','HOR', '_HSE|9', 'GRS', '_HSE|14',  'HOR', 'DWL',  'GRS', '_TOW|19',  'HOR','DWL',  'GRS', '_NXS|22', 'DWL','GRS'],
       [ 'GRS','VER',  'UPR', 'HOR',  '_HSE|3', 'DWL',  'UPR','HOR',  '_HSE|8', 'GRS', 'UPR','_TOW|11',  'UPL', 'GRS',  '_HSE|16', 'HOR',  'UPL','DWR',  '_HSE|20', 'HOR', 'UPL','VER','GRS'],
       [ 'GRS','_TOW|2',  'GRS', 'GRS',  'VER', 'VER',  'GRS','GRS',  'GRS', 'GRS', 'GRS', 'VER' , 'GRS', 'GRS',  'GRS', 'GRS',  'GRS','VER',  'VER', 'GRS', 'GRS','_TOW|23','GRS'],
       [ 'GRS','GRS',  'GRS', 'GRS',  '_TOW|4', 'UPR',  'HOR','_HSE|6',  'DWL', 'GRS', 'DWR', '_TOW|12',   'DWL', 'GRS',  'DWR', '_HSE|17',  'HOR','UPL',  '_TOW|21', 'GRS', 'GRS','GRS','GRS'],
       [ 'GRS','GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','VER',  'VER', 'GRS', 'VER', 'GRS',  'VER', 'GRS',  'VER', 'VER',  'GRS','GRS',  'GRS', 'GRS', 'GRS','GRS','GRS'],
       [ 'GRS','GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','_TOW|7',  'UPR', 'HOR', '_HSE|10',  'GRS',  '_HSE|15', 'HOR',  'UPL', '_TOW|18',  'GRS','GRS',  'GRS', 'GRS','GRS', 'GRS','GRS'],
       [ 'GRS','GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'VER',  'GRS',  'VER', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS','GRS','GRS'],
       [ 'GRS','GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'UPR', '_TOW|13',   'UPL', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS','GRS','GRS']]

necklace = Graph(1, 22,map3)
necklace.addVertex(Vertex(1, 5))
necklace.addVertex(Vertex(2, 10))
necklace.addVertex(Vertex(3, 5))
necklace.addVertex(Vertex(4, 10))
necklace.addVertex(Vertex(5, 10))
necklace.addVertex(Vertex(6, 5))
necklace.addVertex(Vertex(7, 10))
necklace.addVertex(Vertex(8, 5))
necklace.addVertex(Vertex(9, 5))
necklace.addVertex(Vertex(10, 5))
necklace.addVertex(Vertex(11, 10))
necklace.addVertex(Vertex(12, 10))
necklace.addVertex(Vertex(13, 10))
necklace.addVertex(Vertex(14, 5))
necklace.addVertex(Vertex(15, 5))
necklace.addVertex(Vertex(16, 5))
necklace.addVertex(Vertex(17, 5))
necklace.addVertex(Vertex(18, 10))
necklace.addVertex(Vertex(19, 10))
necklace.addVertex(Vertex(20, 5))
necklace.addVertex(Vertex(21, 10))
necklace.addVertex(Vertex(22, 5))
necklace.addVertex(Vertex(23, 10))
necklace.vertList[1].color = 0
necklace.vertList[22].color = 1
necklace.addEdge(1, 2)
necklace.addEdge(1, 3)
necklace.addEdge(3, 5)
necklace.addEdge(3, 4)
necklace.addEdge(3, 6)
necklace.addEdge(6, 7)
necklace.addEdge(6, 10)
necklace.addEdge(10, 12)
necklace.addEdge(10, 13)
necklace.addEdge(12, 11)
necklace.addEdge(11, 9)
necklace.addEdge(9, 8)
necklace.addEdge(8, 5)
necklace.addEdge(15, 12)
necklace.addEdge(13, 15)
necklace.addEdge(11, 14)
necklace.addEdge(14, 16)
necklace.addEdge(16, 19)
necklace.addEdge(19, 20)
necklace.addEdge(21, 20)
necklace.addEdge(22, 20)
necklace.addEdge(22, 23)
necklace.addEdge(17, 20)
necklace.addEdge(15, 17)
necklace.addEdge(17, 18)
gamePlatforms.addGame(necklace, 'necklace')


map4 = [['GRS','GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS',  'GRS',  'GRS'],
       ['GRS','GRS', 'DWR',  'DWT', '_HSE|4',  'DWT', '_HSE|9',  'HOR','HOR',  '_HSE|16', 'DWT', '_HSE|23', 'DWT', 'DWL',  'GRS',  'GRS'],
       ['GRS','GRS', 'VER',  'LFT', '_HSE|5',  'LFT', '_HSE|10',  'GRS','GRS',  '_HSE|17', 'RGT', '_HSE|24', 'RGT', 'VER',  'GRS',  'GRS'],
       ['GRS','DWR', '_TOW|2',  'RGT', 'DWR',  'CRS', '_HSE|11',  'HOR','HOR',  '_HSE|18', 'CRS', 'DWL', 'LFT', '_TOW|28',  'DWL',  'GRS'],
       ['GRS','_NXS|1', 'GRS',  'LFT', '_HSE|6',  'LFT', '_HSE|12',  'GRS','GRS',  '_HSE|19', 'RGT', '_HSE|25', 'RGT', 'GRS',  '_NXS|30',  'GRS'],
       ['GRS','UPR', '_TOW|3',  'RGT', 'UPR',  'CRS', '_HSE|13',  'HOR','HOR',  '_HSE|20', 'CRS', 'UPL', 'LFT', '_TOW|29',  'UPL',  'GRS'],
       ['GRS','GRS', 'VER',  'LFT', '_HSE|7',  'LFT', '_HSE|14',  'GRS','GRS',  '_HSE|21', 'RGT', '_HSE|26', 'RGT', 'VER',  'GRS',  'GRS'],
       ['GRS','GRS', 'UPR',  'UPT', '_HSE|8',  'UPT', '_HSE|15',  'HOR','HOR',  '_HSE|22', 'UPT', '_HSE|27', 'UPT', 'UPL',  'GRS',  'GRS'],
       ['GRS','GRS', 'GRS',  'GRS', 'GRS',  'GRS', 'GRS',  'GRS','GRS',  'GRS', 'GRS', 'GRS', 'GRS', 'GRS',  'GRS',  'GRS']]
       
ww2 = Graph(1, 30,map4)
ww2.addVertex(Vertex(1, 50))
ww2.addVertex(Vertex(2, 10))
ww2.addVertex(Vertex(3, 10))
ww2.addVertex(Vertex(4, 5))
ww2.addVertex(Vertex(5, 5))
ww2.addVertex(Vertex(6, 5))
ww2.addVertex(Vertex(7, 5))
ww2.addVertex(Vertex(8, 5))
ww2.addVertex(Vertex(9, 5))
ww2.addVertex(Vertex(10, 5))
ww2.addVertex(Vertex(11, 5))
ww2.addVertex(Vertex(12, 5))
ww2.addVertex(Vertex(13, 5))
ww2.addVertex(Vertex(14, 5))
ww2.addVertex(Vertex(15, 5))
ww2.addVertex(Vertex(16, 5))
ww2.addVertex(Vertex(17, 5))
ww2.addVertex(Vertex(18, 5))
ww2.addVertex(Vertex(19, 5))
ww2.addVertex(Vertex(20, 5))
ww2.addVertex(Vertex(21, 5))
ww2.addVertex(Vertex(22, 5))
ww2.addVertex(Vertex(23, 5))
ww2.addVertex(Vertex(24, 5))
ww2.addVertex(Vertex(25, 5))
ww2.addVertex(Vertex(26, 5))
ww2.addVertex(Vertex(27, 5))
ww2.addVertex(Vertex(28, 10))
ww2.addVertex(Vertex(29, 10))
ww2.addVertex(Vertex(30, 50))
ww2.vertList[1].color = 0
ww2.vertList[30].color = 1
ww2.addEdge(1, 2)
ww2.addEdge(3, 1)
ww2.addEdge(4, 2)
ww2.addEdge(6, 2)
ww2.addEdge(3, 6)
ww2.addEdge(3, 8)
ww2.addEdge(4, 5)
ww2.addEdge(5, 6)
ww2.addEdge(7, 6)
ww2.addEdge(7, 8)
ww2.addEdge(4, 9)
ww2.addEdge(6, 11)
ww2.addEdge(13, 6)
ww2.addEdge(15, 8)
ww2.addEdge(15, 14)
ww2.addEdge(14, 13)
ww2.addEdge(13, 12)
ww2.addEdge(11, 12)
ww2.addEdge(11, 10)
ww2.addEdge(10, 9)
ww2.addEdge(16, 9)
ww2.addEdge(11, 18)
ww2.addEdge(13, 20)
ww2.addEdge(15, 22)
ww2.addEdge(16, 17)
ww2.addEdge(17, 18)
ww2.addEdge(18, 19)
ww2.addEdge(19, 20)
ww2.addEdge(21, 20)
ww2.addEdge(21, 22)
ww2.addEdge(27, 22)
ww2.addEdge(20, 25)
ww2.addEdge(18, 25)
ww2.addEdge(16, 23)
ww2.addEdge(23, 24)
ww2.addEdge(25, 24)
ww2.addEdge(25, 26)
ww2.addEdge(26, 27)
ww2.addEdge(27, 29)
ww2.addEdge(29, 25)
ww2.addEdge(28, 25)
ww2.addEdge(23, 28)
ww2.addEdge(29, 30)
ww2.addEdge(28, 30)
gamePlatforms.addGame(ww2, 'WWII')
