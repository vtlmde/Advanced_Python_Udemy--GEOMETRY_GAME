from random import randrange 
import turtle

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

# PC child of point with GUI display method
class gui_point(point):

    # PC GUI display method
    def write_point_on_canva(self,canva, size=5, color='red'):
        canva.penup()
        canva.goto( self.x , self.y )
        canva.pendown()
        canva.dot (size, color)

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

# PC define a child class of rectangle which displays a canva. 
class gui_rectangle( rectangle ):

    # PC define a method to display the rectangle on the canva
    def write_rectangle_on_canva(self, canva ):

        # go to rectangle lower_left_point position without tracing.
        canva.penup()
        canva.goto( self.lower_left_point.x , self.lower_left_point.y )
        canva.pendown()
        

        #Tracing rectangle
        canva.forward( self.upper_right_point.x - self.lower_left_point.x )
        canva.left(90)
        canva.forward( self.upper_right_point.y - self.lower_left_point.y )
        canva.left(90)
        canva.forward( self.upper_right_point.x - self.lower_left_point.x )
        canva.left(90)
        canva.forward( self.upper_right_point.y - self.lower_left_point.y )


#PC create a random rectangle and print to user.
rectangle1 = gui_rectangle(point( randrange(0,100) , randrange(0,100) ) , 
                       point( randrange(101,200) , randrange(101,200) ) 
                       ) 
print("The rectangle has a lower left point:  ", rectangle1.lower_left_point.x ," , "
                                                , rectangle1.lower_left_point.y ,
                        "and upper right point: ", rectangle1.upper_right_point.x, " , "
                                                  ,rectangle1.upper_right_point.y, " .")

# PC Ask user for his chosen point coordinates.
point1 = gui_point( float( input( "Select an X for a point inside the rectangle: " ) ), 
               float( input( "Select a Y for point inside the rectangle: " ) ) )

# PC Check chosen point is in rectangle and return result.
print( "Your chosen point is inside the provided rectangle: ", point1.is_in_rectangle( rectangle1 ) )

# PC Guess Area rectangle
rectangle_area_guess_attempt = float( input( "Guess the area of the rectangle: " ) )
print ( " You are off by :" , abs( int( rectangle1.calculate_area()-rectangle_area_guess_attempt ) ) )

canva = turtle.Turtle()
rectangle1.write_rectangle_on_canva(canva)
point1.write_point_on_canva(canva)

input("finished ?")