filename="1.txt"
maxd=110
maxr=100
unset border
set polar
set xrange [-maxd:maxd] #make gnuplot to go until 6000
set yrange [-maxd:maxd]
set rrange [0:maxd]
set angles degrees #set gnuplot on degrees instead of radians


set style line 10 lt 1 lc 0 lw 0.3 #redefine a new line style for the grid
set style line 11 lc rgb 'gray80' lt -1

set rtics 0, 20, 100 format '' scale 0#make the ytics go from the center (0) to 6000 with incrment of 1000
set grid polar 30 #set the grid to be displayed every 60 degrees
set grid ls 11

#set xrange [-6000:6000] #make gnuplot to go until 6000
#set yrange [-6000:6000]

set xtics axis #disply the xtics on the axis instead of on the border
set ytics axis
unset ytics
unset xtics
unset raxis
#unset rtics

#set xtics scale 0 #"remove" the tics so that only the y tics are displayed
#set xtics ("" -20, "" -40, "" -60, "" -80, "" -90) #set the xtics only go from 0 to 6000 with increment of1000 but do not display anything. This has to be done otherwise the grid will not be displayed correctly.
#set ytics 0, 20, 90 #make the ytics go from the center (0) to 6000 with incrment of 1000
#set rtics 0, 20, 100 #make the ytics go from the center (0) to 6000 with incrment of 1000

set size square 

#set key lmargin

set_label(x, text) = sprintf("set label '%s' at (1.05*maxd*cos(%f)), (1.05*maxd*sin(%f))     center", text, x, x) #this places a label on the outside

#here all labels are created
eval set_label(0, "360")
eval set_label(30, "30")
eval set_label(60, "60")
eval set_label(90, "90")
eval set_label(120, "120")
eval set_label(150, "150")
eval set_label(180, "180")
eval set_label(210, "210")
eval set_label(240, "240")
eval set_label(270, "270")
eval set_label(300, "300")
eval set_label(330, "330")

set for [i=1:5] label at first maxd*((i/5.5)-0.04),first -maxd*0.07 sprintf("%d", (i*20))
set for [i=0:5] object circle at first maxr*((i/5.0)),first 0 size scr 0.001

set for [i=1:12] arrow from first (0.95*maxd*cos(i*30)), first (0.95*maxd*sin(i*30)) to first (0.9*maxd*cos(i*30)), first (0.9*maxd*sin(i*30)) lc rgb 'gray80' lt -1 nohead
#set for [i=1:10] arrow from (maxd*cos(i*30)), (maxd*sin(i*30)) to  (0.95*maxd*cos(i*30)),  (0.95*maxd*sin(i*30))

set style line 11 lt 1 lw 2 pt 7 ps 1 lc rgb 0xff0000  #set the line style for the plot
set style line 12 lt 1 lw 2 pt 7 ps 1 lc rgb 0x00ff00 #set the line style for the plot

#and finally the plot
plot filename u 1:4 not w lp ls 11,filename u 1:5 not w lp ls 12  
pause -1