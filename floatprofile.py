#pressure limit for profiling (num of max rotations)
#test 1m first, then try 
#for #so main.py would stop running after said limit for loop

def float_profile(sample_time):
    #import urtc
    from time import sleep_ms
    from machine import Pin, I2C, RTC
    import ms5803 # temp & pressure sensor 
    
    import motorcode as mc #motor_run, motor_stop
    
    i2c = I2C(scl=Pin(5), sda = Pin(4))
    #rtc = urtc.DS3231(i2c)
    
    # encoder counts - piston position
    # check depth with encoder counts
    # use encoder counts to set where we want the float to go (proxy for depth since pressure sensor may not be accurate)
       
    #sampling every second 
    
    #give encoder count
    #take pressure & temp at encoder count
    #check if pressure is within range, if not continue (give more encoder counts)
    
    # float profiling function
    # def float():
    #	start motor
    # 	run secondary functions for up and down
    #		vol_increase(max_motortime = 10 seconds ): while time < maxmotortime: motor_run(UP), record pressure + time every 1 sec, else break, stop
    #		vol_decrease(): motor_run(DOWN), record pressure + time every 1 sec, stop
    # 	use 10 secs as benchmark time (need to test out up and down time for now)

    
    datafile = open("pressure_temp_data.csv", "a")

    sample_no = 0 

    for i in range(sample_time):
        import motorcode as mc
        UP     = True
        DOWN    = False
        mc.motor_run(DOWN)
        
        #save pressure & temp values + calculated depth values
        sample_no += 1 # Increment the sample number for each reading
    
        sensor=ms5803.read(i2c=i2c, address=118)
        pressure = sensor[0]
        temp = sensor[1]
        
        #convert pressure into depth (P = rho*g*h)
        rho = 1021.4269 # from mrv buoyancy tests (5/20)
        g = 9.81
        depth = pressure/(rho*g)
    
        # get the time for the measurement
        #t = rtc.datetime()
        #time = str(str(t.year) + '/' + str(t.month) + '/' + str(t.day) + ' ' + str(t.hour) + ':' + str(t.minute) + ':' + str(t.second))
    
        #print(sample_no, ",", time, ",", depth, ",", pressure, ",", temp) # print time + pressure & temp
        
        print(sample_no, ",", depth, ",", pressure, ",", temp) # print time + pressure & temp
        
        #datafile.write(str(sample_no) + ',' + str(time) + ',' + str(depth)+ ',' +
         #              str(pressure)+ ',' + str(temp) + '\n')
        datafile.write(str(sample_no) + ',' + str(depth)+ ',' +
                       str(pressure)+ ',' + str(temp) + '\n')
        
    for i in range(sample_time):
        mc.motor_run(UP)
        
        #save pressure & temp values + calculated depth values
        sample_no += 1 # Increment the sample number for each reading
    
        sensor=ms5803.read(i2c=i2c, address=118)
        pressure = sensor[0]
        temp = sensor[1]
        
        #convert pressure into depth (P = rho*g*h)
        rho = 1021.4269 # from mrv buoyancy tests (5/20)
        g = 9.81
        depth = pressure/(rho*g)
    
        # get the time for the measurement
        #t = rtc.datetime()
        #time = str(str(t.year) + '/' + str(t.month) + '/' + str(t.day) + ' ' + str(t.hour) + ':' + str(t.minute) + ':' + str(t.second))
    
        #print(sample_no, ",", time, ",", depth, ",", pressure, ",", temp) # print time + pressure & temp
        print(sample_no, ",", depth, ",", pressure, ",", temp) # print time + pressure & temp
        #datafile.write(str(sample_no) + ',' + str(time) + ',' + str(depth)+ ',' +
        #               str(pressure)+ ',' + str(temp) + '\n')
        datafile.write(str(sample_no) + ',' + str(depth)+ ',' +
                       str(pressure)+ ',' + str(temp) + '\n')
    
    mc.motor_stop()
    datafile.close() # run this in the shell after you interupt the while loops to finish saving the data

#float_profile(1)