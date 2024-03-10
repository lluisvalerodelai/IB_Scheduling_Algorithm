###hello###

----------------------------------------FORMALIZING THE PROBLEM----------------------------------------

First some things need to be defined:

C = {c_1, c_2, c_3, ..., c_q}; c_1 could be for example 'french b'
    each course c_i has l_i lectures per week and s_i students
C -> list of all the classes
q -> total number of classes
    each class gets assigned a number
    'french b' could be assigned number 1


    P = {1, 2, 3, ..., p}
    where p is the number of periods in a week,
    there are 4 available weekdays, each with 6 available time slots for classes to be had
    so total of number of time periods for ish is 6 x 4 = 24. 
    p = 24

    Same for rooms, 
    R = {r_1, r_2, r_3, ..., r_m} 
    where m is the total number of rooms
    each room has a property which is the total number of students it can hold

The solution is of the form of a qxp matrix T (for timetable)
    where t_ik = j, where j is between 1-m (number of rooms)
    t_ik = j => course c_i has class during period k in room r_j
        so the row number (i) is the class, and the column (j) number is the period, then the value of the matrix at that (row,column) is the room it will be held in
    
So the program is going to search for the matrix T such that the following constraints are satisfied
    1. Number of classes (hard constraint)
        the number of classes per week of c_i must be l_i (where L is a list and l_i is the number of classes per week of c_i)
    2. room occupancy (hard constraint)
        no 2 classes can happen in the same room at the same time 
        this means no row (aka period number) can have the same number repeated
    3. Conflicts (hard constraint)
        classes that share students cannot be held at the same time, and classes taught by the same teacher cannot happen at the same time
        define a conflict matric CM of size qxq where cm_iq = 1 if c_i and q_i share a student or teacher and zero is otherwise
    4. Availabilities (hard constraint)
        to work around teachers schedules (some teachers might not be available at some times)
        define availability matrix AM which is qxp such that am_ik = 1 if lecture c_i can be held during period k, and zero if otherwise
    5. Room capacity (soft constraint)
        the number of students s_i of course c_i must be less than or equal to the number of seats in that room
    6. Avoid 2 classes in one day
        the mumber of periods in a week is divisible by 5 days with each day having p/5 periods. 
        each class must not be held more than once in the same day


----------------------------------------BASIC LOCAL ENTITIES----------------------------------------
=> basically the minimum things that are needed to be able to have a search function which finds possible timetables 

Search Space
    The search space is all the timetable matrices T for which the 'number of classes' and 'availabilities' contraints hold
    States for which the room occupancy and conflicts contraints do not hold are allowed but must be significantly penalized

Cost function
    the cost function is a sum of the measure of violation of all constraints
    the hard constraints which can be violated (room occupancy and conflicts) are significantly penalized (say a score of 1000)
    soft constraints are penalized relative to their importance

if the measure of violation of contraint i if f_i(T) and the cost function is denoted F(T) where T is a given timetable then 
    F(T) = 1000(f_2(T) + f_3(T)) + f_4(T) + f_5(T) + f_6(T)

Strategy for generating inital solution

The intial solution is generated at random
    -start with the first class, for each of its classes per week assign it a random period and a random room following the AM matrix (no courses are where teachers cant teach)
    -the intial solution and any solution at a given time point must always satisfy constraints 1 and 4




