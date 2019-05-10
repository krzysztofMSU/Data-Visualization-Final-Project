---
layout: post
title:  " The Size of The Universe"
date:   2019-05-05 16:36:55 -0600
categories: jekyll update
author: Brook Beyene, Chris (Krzysztof) Rabka
---
## Data Visualization Final Project, Spring 2019


### *Introduction*

When we look up to the skies, we wonder how vast the universe is.
Here we will explore the size of our known universe. First, we will take a look at the International Space Station (ISS), the Earth and the Moon, then we will compare planets with our Sun in our solar system and see the difference in their trajectory around the Sun, we will check the difference between the distance and velocity of other galaxies vs. our Milky Way, and lastly we will see the difference between mass, size, temperature and luminosity of stars.

### *Earth, International Space Station and the Moon*
Imagine, we are flying out of Earth’s atmosphere on a space shuttle and dock with the International Space Station (ISS). We would be able to see Moon revolving around us and the Earth. This would give us our first view of the whole size of the Earth in relation to the Moon. Below is a screenshot of the end result of 3D interactive visualization generated with [blender](https://www.blender.org/), and in that software it lets us rotate the Moon and ISS around Earth. The ISS is farther from Earth (not to scale - it’s out beyond Earth’s outer atmosphere and its size is enlarged), otherwise the ISS would be the size of a single pixel.

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_assets/_images/earth_moon_iss.png?raw=true)

### *Sizes of celestial bodies in our solar system*

Next, we will move out of the solar system to see all the planets and our Sun.

Sun is the largest and as we move away from it, we see all the planets in order. In this screenshot (below) of the 3D visualization also generated with [blender](https://www.blender.org/), we can see Earth as a small ball, the second object from the Sun (mercury is very small and not visible at this scale). Here our focus is on the size of planets and the distances between planets are arbitrary to focus our attention on their sizes. We don’t show moons here, as they would be too small to see them at this scale. To see a different angle of the planets we can rotate them around the Sun in [blender](https://www.blender.org/).

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_assets/_images/size_solar_system_new.png?raw=true)

### *Speed of Planets and their gravitational forces*

Now let’s check out the speed of planets as they revolve around the Sun.

Another perspective shows us a different dynamic of our solar system. In the animation below written in [Python](https://www.python.org/) and with use of [matplotlib](https://matplotlib.org/) and [Turtle graphics](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#module-turtle), we see first four planets on their way around the Sun (Mercury, Venus, Earth and Mars). We can see the difference in speed. Planets closer to the Sun revolve more frequently because their circumference of their path is shorter. We also notice the elliptical paths. The gravitational interaction of planets distorts the circular shape of the path for all of them. They all revolve in different shapes of ellipses.

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_includes/_gif/palents_eliptical.gif?raw=true){:height="650"width="400"}

### *Velocity of other galaxies away from Earth*

Latest research gave us a lot of data for the relation between distance and velocity of galaxies.

In the figure below also written in [Python](https://www.python.org/) and with use of [matplotlib](https://matplotlib.org/), the distance to other galaxies is measured from our Milky Way, and the velocity with respect to the distance tells us about the expansion. Galaxies relatively close to Milky Way move through space at increasing  rate, and when we compare them with other galaxies that are much farther away from us, their velocities are exponential. For this comparison we consider the speed of light to be constant and we see that the difference in the velocity increases at a very rapid rate.

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_assets/_images/UniverseExpansionBy_Brook_and_Chris.png?raw=true)

### *Hertzsprung-Russell Diagram - Stars temperature and luminosity with respect to mass*

The Hertzsprung-Russell Diagram plots stars according to their surface temperatures and luminosity.
([Python](https://www.python.org/), [matplotlib](https://matplotlib.org/))

The brightness of a star depends on the amount of light it emits into space and its distance from Earth. We can measure it through stellar parallax (apparent shift of position of any nearby star against the background of any other distant object). There are numerous classifications of stars based on their temperature and luminosity. The H-R diagram shows clear pattern between luminosity, temperature and mass. The super giants in the top-right and the smallest white-dwarfs in the lower-left. Our Sun is in the group of the main-sequence stars.

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_assets/_images/H_R_Diagram.png?raw=true)

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_assets/_images/equation_2.png?raw=true)

Below is 3D view of the H-R's size, mass and **temperature** when compared to our Sun. ([Python](https://www.python.org/), [matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/), [NumPy](https://www.numpy.org/), [math](https://docs.python.org/2/library/math.html))

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_includes/_gif/size_mass_temperature_by_Brook_and_Chris.gif?raw=true){:height="650"width="400"}

Below is 3D view of the H-R's size, mass and **luminosity** also compared to our Sun. ([Python](https://www.python.org/), [matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/), [NumPy](https://www.numpy.org/), [math](https://docs.python.org/2/library/math.html))

![](https://github.com/krzysztofMSU/data-visualization-final-project/blob/gh-pages/_includes/_gif/size_mass_lumionsity_by_Brook_and_Chris.gif?raw=true){:height="650"width="400"}

### *Summary*

The static, interactive and 3 Dimensional visualizations help us understand the data. We can see our solar system with difference in sizes between planets, the simulation of the rotation of planets around Sun shows us the difference in planetary orbits. The matplotlib is a great tool to visualize the data for universe expansion and the enormous distances between stars and galaxies.

<!--
> #### link
> ### <https://krzysztofmsu.github.io/data-visualization-final-project/>
-->
