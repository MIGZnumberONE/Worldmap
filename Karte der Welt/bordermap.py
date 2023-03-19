#Importiere die benötigten Bibliotheken
import matplotlib.pyplot as plt # Zur Erstellung von Diagrammen
from mpl_toolkits.basemap import Basemap # Zur Erstellung der Karte

# Karte erstellen, Erstelle eine Figur mit einer Größe von 10x6 Zoll
fig = plt.figure(figsize=(10, 6))
# Erstelle eine Basemap-Karte mit der Mill-Projektion und begrenze sie auf eine Weltkarte
m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
#Zeichne Küstenlinien und Ländergrenzen auf der Karte
m.drawcoastlines()
m.drawcountries()

# Karte anzeigen
plt.show()