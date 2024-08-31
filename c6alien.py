alien_0 = {'color':'green','points':5}

#print(alien_0['color'])
#print(alien_0['points'])

new_points = alien_0['points']
print("you just earned "+str(new_points)+" points!.")
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print("the alien is now "+alien_0['color'])
alien_0['speed'] = 'medium'
print("original x-position: "+str(alien_0['x-position']))
#move the alien to the right
#determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3

#the new position is the old position plus the increment
alien_0['x-position'] = alien_0['x-position'] + x_increment

print("new x-position: "+str(alien_0['x-position']))
