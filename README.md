# FPL API

### Endpoints Used
FPL's api exposes /api/bootstrap-static/ which provides almost all fpl data, we also use /api/fixtures/ to see general prem fixture data.

### Strategy
We started off by sorting the players by **points** and **points/cost**. Both of these are good metrics for picking fpl players - total **points** shows us the high impact players we want to own and captain, and **points/cost** shows us the "value" players that provide good (usually cheap) options to fill out a team.

I'm planning to implement some statistical methods to predict future points, the api provides a lot of data, so I have plenty of options for this. We can obviously use the physical goal/assist/saves/etc. data, but also the probabilistic xG/xA/xCS, as well as fixture and form data.

I'm also thinking of using the fixture data as well as points/cost to have a good metric to compare players over the next N gameweeks - with the end goal of eventually being able to scale this up to comparing whole teams. This is an extremely rich problem space, we could account for player transfers and sub rotations and we obviously have the cost constraint to consider.


