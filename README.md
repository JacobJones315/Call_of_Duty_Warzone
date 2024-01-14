# Call of Duty Warzone: Analyzing Projectile Weapons' Success Against Moving Targets in Call of Duty Warzone
* Before the release of Call of Duty Warzone in 2019, all weapons operated on a hitscan system, ensuring instant hits on accurately aimed targets.
* Subsequent to Call of Duty 2019, a significant change occurred where players are now required to consider bullet travel time and potentially lead their targets before pulling the trigger.
* I conducted data visualizations to assess the probability of hitting a moving target by simply aiming at center mass across different ranges and weapon bullet velocities.

## Objectives
* Compute the travel times for projectiles over varied distances using different weapon projectile velocities.
* Evaluate the likelihood of hitting a target in lateral motion, perpendicular to the observer, by aiming at its center mass.

## Parameters
*  Consider the average player sprint speed (7.5 m/s) and player width (0.6 meters at center mass).

## Procedure
* Generate arrays for custom ranges and projectile velocities.
* Utilize nested loops to populate a dataframe with projectile travel times for each custom range and velocity
* Create a second dataframe to analyze how far the player can move while sprinting after firing the projectile.
* Created a heat map of the second dataframe to showcase if the projectile will hit its desired target when aiming at the center mass of the target, while target is moving lateral to observer.
*  Green = Hit, Red = Miss

## Screenshot of Visualizations:
![](/images/COD_SuccessHMfig1.png)
![](/images/COD_BTT_fig3.png)
![](/images/CODBTTfig2.png)






















