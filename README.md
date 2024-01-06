# Call of Duty Warzone: Analyzing Projectile Weapons' Success Against Moving Targets in Call of Duty Warzone
* Prior to Call of Duty Warzone 2019 all weapons were hitscan, instantly hitting targets when aimed accurately.
* However, since Call of Duty 2019, players must factor in bullet travel time and potentially lead their targets before firing.
* Created data visualizaions to determine the likelihood of hiting a moving target by simply aiming at centermass at various ranges and bullet velocitys. 

## Function Objectives
* Determine projectile travel times to target at various dinstances
* Various base weapons have specific projectle velocitys
* If a player is running perpendicular to the observers position, will they hit their target by simply aiming at center mass 

## Procedure
* Created an array of custom ranges
* Created an array of custom projectile velocitys
* Created a blank dataframe and populated it using a nested for loop to determine the projectile time to target at each custom range and velocity
* Determined average player sprint speed to be 7.5 meters/second and player width to be 0.6 meters at center mass
* Created a second dataframe to determine how far the player can travel when sprinting post projectile firing
* Created a heat map of the second dataframe to showcase if the projectile will hit its desired target when aiming at the center mass of the target, while target is moving perpendicular to observer
* Green = Hit, Red = Miss

## Screenshot of Graphs Generated
