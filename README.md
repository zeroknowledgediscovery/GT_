# GT_
Ground Truth

## Variable Definitions

+ UID: ID of the individual. 100 different individuals.
Lat & Lon: used to create a imaginary spatial tile to represent this person.
+ Timestep: The time. 5 min increments.
+ myFriends: Number of friends at the site currently being visited.
+ myFriends_ratio: fraction of the number of friends at this site vs number of friends total for this person.
+ fracFriends: fraction of the number of friends at this site vs total number of people at this site
+ meetingPairs: number of "meetings" happening at this site.
+ singles: number of people who are at this site that is not in a meeting. meeting includes those meetings between friends.
+ visitors: total number of people at this site.
+ Dist: travel distance between this site and last different site.
+ PopFrac: Population Fraction. Defined as the number of visitors at this site divided by the total number of visitors in a neighborhood around this site.
+ MeetFrac: Meeting Fraction. Defined as the number of meetings at this site divided by the total number of meetings in a neighborhood around this site.
+ Sitetype: Recreational or restaurants

*A neighborhood is 1/2 times the median of pairwise distances between all the sites visited by an individual. This implies that the neighborhood size changes between individuals.*
