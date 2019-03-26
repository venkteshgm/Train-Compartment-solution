# Train-Compartment-solution

My solution to HackerEarth's Train Compartment problem titled Seating Arrangement
The program is written in Python
Question reads:
The seats are denoted as follows : 

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS
You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

Program Description:
main() - takes in list of inputs, calls in seat_finder() for each input
seat_finder() - calls seat_function() to find opposite seat number and opp_seat_type() to find seat type of opposite seat
seat_function() - checks if seat is left or right facing(right or left side of particular 12 seat block
opp_seat_type() - checks type of opp seat
