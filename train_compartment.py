def main():
    no_of_inputs=int(input())    #number of inputs
    list_of_inputs=[]
    for i in range(0,no_of_inputs):    #input seat numbers into list_of_inputs
        list_of_inputs.append(int(input()))
    for i in list_of_inputs:
        seat_finder(i)
def seat_finder(n):
    opposite_seat=seat_function(n)
    opposite_seat_type=opp_seat_type(n)
    print(opposite_seat,opposite_seat_type)
def seat_function(n):
    flag=0
    if (int((n-1)/6))%2==0:  #left side seat test
        return left_side_aisle(n)    
    else:
        return right_side_aisle(n)
def right_side_aisle(n):
    if n%6!=0:
        return (6*(int(n/6)))-(n%6)+1      #right side seat's opposite seat logic
    else:
        return n-11
def left_side_aisle(n):
    if n%6!=0:
        return 6*(int(n/6)+1)+(6-(n%6)+1)      #left side seat's opposite seat logic
    else:
        return n+1
def opp_seat_type(n):      #seat type will be the same as opposite seat's type
    if n%6==0 or n%6==1:
        return 'WS'
    elif n%6==2 or n%6==5:
        return 'MS'
    else:
        return 'AS'
main()
