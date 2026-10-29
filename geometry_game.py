from random import randrange 

# PC define a point class
class point:    

## PC point has attribute x coordinate and y coordinate
    def __init__( self , x , y ):
        self.x = x
        self.y = y

## PC point has is_in_rectangle function
    def is_in_rectangle( self , rectangle ) :
        return ( rectangle.lower_left_point.x < self.x < rectangle.upper_right_point.y and 
                rectangle.lower_left_point.y < self.y < rectangle.upper_right_point.y )

# PC define a rectangle class
class rectangle:

# PC rectangle has upper right  point and lower left point
    def __init__( self, lower_left_point , upper_right_point ):
        self.lower_left_point = lower_left_point
        self.upper_right_point = upper_right_point

# PC rectangle has method to calculate its area
    def calculate_area( self ):
        return ( self.upper_right_point.x - self.lower_left_point.x ) * \
                    ( self.upper_right_point.y - self.lower_left_point.y )

#PC create a random rectangle and print to user.
rectangle1 = rectangle(point( randrange(0,9) , randrange(0,9) ) , 
                       point( randrange(10,19) , randrange(10,19) )) 
print("The rectangle has a lower left point:  ", rectangle1.lower_left_point.x ," , "
                                                , rectangle1.lower_left_point.y ,
                        "and upper right point: ", rectangle1.upper_right_point.x, " , "
                                                  ,rectangle1.upper_right_point.y, " .")

# PC Ask user for his chosen point coordinates.
point1 = point( float( input( "Select an X for a point inside the rectangle: " ) ), 
               float( input( "Select a Y for point inside the rectangle: " ) ) )

# PC Check chosen point is in rectangle and return result.
print( "Your chosen point is inside the provided rectangle: ", point1.is_in_rectangle( rectangle1 ) )

# PC Guess Area rectangle
rectangle_area_guess_attempt = float( input( "Guess the area of the rectangle: " ) )
print ( " You are off by :" , abs( int( rectangle1.calculate_area()-rectangle_area_guess_attempt ) ) )