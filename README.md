# Call of Duty Warzone: Analyzing Projectile Weapons' Success Against Moving Targets in Call of Duty Warzone
* Prior to Call of Duty Warzone 2019 all weapons were hitscan, instantly hitting targets when aimed accurately.
* However, since Call of Duty 2019, players must factor in bullet travel time and potentially lead their targets before firing.
* Created data visualizaions to determine the likelihood of hiting a moving target by simply aiming at centermass at various ranges and bullet velocitys. 

## Objectives
* Calculate projectile travel times for various distances based on different projectile velocities.
* Assess the probability of hitting a target moving perpendicular to the observer by aiming at its center mass.

## Parameters
*  Consider the average player sprint speed (7.5 m/s) and player width (0.6 meters at center mass).

## Procedure
* Generate arrays for custom ranges and projectile velocities.
* Utilize nested loops to populate a dataframe with projectile travel times for each custom range and velocity
* Create a second dataframe to analyze how far the player can move while sprinting after firing the projectile.
* Created a heat map of the second dataframe to showcase if the projectile will hit its desired target when aiming at the center mass of the target, while target is moving perpendicular to observer.
*  Green = Hit, Red = Miss

## Screenshot of Visualizations:
![](/images/COD_SuccessHMfig1.png)
![](/images/COD_BTT_fig3.png)
![](/images/CODBTTfig2.png)






















